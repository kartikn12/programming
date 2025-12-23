import tkinter as tk
from tkinter import ttk, messagebox
import os
from database_helper import DBHandler
from models import BillingCalculator, ReportGenerator
# from datetime import datetime

class MediTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MediCare Hub - MediTrack")
        self.root.geometry("800x600")
        
        
        try:
            self.db = DBHandler()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not start: {e}")
            self.root.destroy()
            return

        self.user_role = None
        self.login_ui()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_ui(self):
        self.clear_screen()
        tk.Label(self.root, text="MediTrack Login", font=("Arial", 24, "bold")).pack(pady=50)
        self.role_var = tk.StringVar(value="Receptionist")
        ttk.OptionMenu(self.root, self.role_var, "Receptionist", "Receptionist", "Doctor", "Admin").pack(pady=10)
        tk.Button(self.root, text="Login", command=self.dashboard, width=20, bg="#2196F3", fg="white").pack(pady=20)

    def dashboard(self):
        self.user_role = self.role_var.get()
        self.clear_screen()
        tk.Label(self.root, text=f"Role: {self.user_role}", fg="gray").pack(anchor="nw", padx=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=50)

        if self.user_role in ["Admin", "Receptionist"]:
            tk.Button(btn_frame, text="Add New Patient", command=self.patient_registration, width=30, height=2).pack(pady=10)
            tk.Button(btn_frame, text="Search & Billing", command=self.search_ui, width=30, height=2).pack(pady=10)
            
        if self.user_role in ["Admin", "Doctor"]:
            tk.Button(btn_frame, text="Regex Medical Reports", command=self.report_ui, width=30, height=2).pack(pady=10)
            
        tk.Button(btn_frame, text="Logout", command=self.login_ui, width=30, bg="#f44336", fg="white").pack(pady=20)

    def patient_registration(self):
        reg_win = tk.Toplevel(self.root)
        reg_win.title("Patient Registration")
        reg_win.geometry("400x450")

        # Labels and Entries
        tk.Label(reg_win, text="Name:").pack(pady=5)
        name_e = tk.Entry(reg_win, width=35); name_e.pack()
        tk.Label(reg_win, text="Age:").pack(pady=5)
        age_e = tk.Entry(reg_win, width=35); age_e.pack()
        tk.Label(reg_win, text="Contact:").pack(pady=5)
        con_e = tk.Entry(reg_win, width=35); con_e.pack()
        tk.Label(reg_win, text="Disease:").pack(pady=5)
        dis_e = tk.Entry(reg_win, width=35); dis_e.pack()

        def save():
            if self.db.add_patient(name_e.get(), age_e.get(), con_e.get(), dis_e.get()):
                messagebox.showinfo("Success", "Patient Saved!")
                reg_win.destroy()

        tk.Button(reg_win, text="Save", command=save, bg="green", fg="white").pack(pady=20)

    def search_ui(self):
        search_win = tk.Toplevel(self.root)
        search_win.title("Search System")
        search_win.geometry("700x500")

        s_ent = tk.Entry(search_win, width=40); s_ent.pack(pady=10)

        cols = ("ID", "Name", "Age", "Contact", "Disease")
        tree = ttk.Treeview(search_win, columns=cols, show='headings')
        for col in cols: tree.heading(col, text=col)
        tree.pack(fill="both", expand=True, padx=10)

        def perform_search():
            for i in tree.get_children(): tree.delete(i)
            records = self.db.search_patient(s_ent.get())
            for r in records: tree.insert("", "end", values=r)

        tk.Button(search_win, text="Search", command=perform_search).pack(pady=5)
        tk.Button(search_win, text="Generate Bill", command=self.billing_ui).pack()

    def billing_ui(self):
        bill_win = tk.Toplevel(self.root)
        bill_win.title("Billing")
        
        tk.Label(bill_win, text="Consultation:").pack()
        c_ent = tk.Entry(bill_win); c_ent.pack()
        tk.Label(bill_win, text="Meds:").pack()
        m_ent = tk.Entry(bill_win); m_ent.pack()

        def save_bill():
            try:
                total = BillingCalculator.generate_bill(c_ent.get(), m_ent.get())
                if not os.path.exists('reports'): os.makedirs('reports')
                with open("reports/invoice.txt", "w") as f:
                    f.write(f"Total: Rs.{total}")
                messagebox.showinfo("Billed", f"Saved. Total: Rs.{total}")
                bill_win.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(bill_win, text="Finalize Bill", command=save_bill).pack(pady=10)

    def report_ui(self):
        report_win = tk.Toplevel(self.root)
        report_win.title("Regex Reports")
        
        tk.Label(report_win, text="Regex Filter (e.g., 'Fever'):").pack(pady=5)
        p_ent = tk.Entry(report_win, width=40); p_ent.pack()

        lbox = tk.Listbox(report_win, width=60, height=15)
        lbox.pack(pady=10, padx=10)

        def apply_regex():
            lbox.delete(0, tk.END)
            data = self.db.fetch_disease_reports()
            try:
                filtered = ReportGenerator.filter_records(p_ent.get(), data)
                for item in filtered: lbox.insert(tk.END, item)
            except Exception as e:
                messagebox.showerror("Regex Error", str(e))

        tk.Button(report_win, text="Filter Records", command=apply_regex, bg="#673AB7", fg="white").pack(pady=5)


root = tk.Tk()
app = MediTrackApp(root)
root.mainloop()