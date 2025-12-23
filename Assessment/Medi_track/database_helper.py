import mysql.connector
from tkinter import messagebox

class DBHandler:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="kartik", 
                database="meditrack_db"
            )
            self.cursor = self.db.cursor(buffered=True)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Could not connect: {e}")

    def add_patient(self, name, age, contact, disease):
        try:
            query = "INSERT INTO patients (name, age, contact, disease) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, age, contact, disease))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error adding patient: {e}")
            return False

    def search_patient(self, search_term):
        
        if not search_term:
            query = "SELECT id, name, age, contact, disease FROM patients"
            self.cursor.execute(query)
        else:
            query = "SELECT id, name, age, contact, disease FROM patients WHERE id = %s OR name LIKE %s OR disease LIKE %s"
            self.cursor.execute(query, (search_term, f"%{search_term}%", f"%{search_term}%"))
        return self.cursor.fetchall()

    def fetch_disease_reports(self):
        
        try:
            self.cursor.execute("SELECT name, disease FROM patients")
            rows = self.cursor.fetchall()
            return [f"{row[0]}: {row[1]}" for row in rows]
        except Exception as e:
            print(f"Error fetching reports: {e}")
            return []