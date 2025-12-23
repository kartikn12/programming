import datetime

attendance_records = []

def valid_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def student_exists(roll, date):
    for record in attendance_records:
        if record["roll"] == roll and record["date"] == date:
            return True
    return False

def mark_attendance():
    print("\n--- Mark Attendance ---")
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    course = input("Enter course name: ").strip()
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    date = valid_date(date_str)
    if not date:
        print("Invalid date format! Please use YYYY-MM-DD.")
        return
    if student_exists(roll, date):
        print("Attendance already marked for this student on this date.")
        return
    status = input("Enter status (P/A): ").strip().upper()
    if status not in ["P", "A"]:
        print("Invalid status! Use 'P' for Present or 'A' for Absent.")
        return
    attendance_records.append({
        "name": name,
        "roll": roll,
        "course": course,
        "date": date,
        "status": status
    })
    print("Attendance recorded successfully!")

def generate_student_report():
    print("\n--- Individual Student Report ---")
    roll = input("Enter roll number: ").strip()
    student_records = [r for r in attendance_records if r["roll"] == roll]
    if not student_records:
        print("No attendance found for this student.")
        return
    total_days = len(student_records)
    present_days = sum(1 for r in student_records if r["status"] == "P")
    absent_days = total_days - present_days
    attendance_percent = (present_days / total_days) * 100
    print(f"\nReport for Roll No: {roll}")
    print("-" * 40)
    print(f"Total Days: {total_days}")
    print(f"Present: {present_days}")
    print(f"Absent: {absent_days}")
    print(f"Attendance %: {attendance_percent:.2f}%")
    if attendance_percent < 75:
        print("Defaulter: Attendance below 75%")

def generate_class_report():
    print("\n--- Class Attendance Report ---")
    course = input("Enter course name: ").strip()
    course_records = [r for r in attendance_records if r["course"] == course]
    if not course_records:
        print("No attendance records found for this course.")
        return
    students = {}
    for r in course_records:
        if r["roll"] not in students:
            students[r["roll"]] = {"name": r["name"], "present": 0, "total": 0}
        students[r["roll"]]["total"] += 1
        if r["status"] == "P":
            students[r["roll"]]["present"] += 1
    print(f"\nAttendance Summary for {course}")
    print("-" * 60)
    print(f"{'Roll':<10}{'Name':<20}{'Present':<10}{'Total':<10}{'%' :<8}{'Defaulter'}")
    print("-" * 60)
    for roll, data in students.items():
        percent = (data["present"] / data["total"]) * 100
        defaulter = "Yes" if percent < 75 else "No"
        print(f"{roll:<10}{data['name']:<20}{data['present']:<10}{data['total']:<10}{percent:<8.2f}{defaulter}")
    print("-" * 60)

def main():
    while True:
        print("\n===== EduTrack Attendance System =====")
        print("1. Mark Attendance")
        print("2. Generate Student Report")
        print("3. Generate Class Report")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            generate_student_report()
        elif choice == "3":
            generate_class_report()
        elif choice == "4":
            print("Exiting EduTrack. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
