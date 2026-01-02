import csv
from datetime import date
import os

FILE_NAME = "attendance.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Roll No", "Name", "Status"])


def mark_attendance():
    today = date.today()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    status = input("Present / Absent: ").capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid status! Use Present or Absent.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, roll, name, status])

    print("✅ Attendance marked successfully!")


def view_attendance():
    print("\n--- Attendance Records ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def attendance_percentage():
    roll = input("Enter Roll Number: ")
    total = 0
    present = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if row[1] == roll:
                total += 1
                if row[3] == "Present":
                    present += 1

    if total == 0:
        print("❌ No attendance records found.")
    else:
        percentage = (present / total) * 100
        print(f"📊 Attendance Percentage: {percentage:.2f}%")

        if percentage < 75:
            print("⚠️ Warning: Low Attendance")


def menu():
    print("\n===== Smart Attendance Tracker =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Attendance Percentage")
    print("4. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        attendance_percentage()
    elif choice == "4":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice! Try again.")
