import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def add_student(data):
    roll_no = input("Enter Roll Number: ")
    if roll_no in data:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    subjects = input("Enter Subjects (comma-separated): ").split(",")
    
    data[roll_no] = {"name": name, "age": age, "marks": marks, "subjects": [s.strip() for s in subjects]}
    save_data(data)
    print("Student added successfully!")

def view_students(data):
    if not data:
        print("No student records found.")
        return
    for roll, info in data.items():
        print(f"Roll No: {roll} | Name: {info['name']} | Age: {info['age']} | Marks: {info['marks']} | Subjects: {', '.join(info['subjects'])}")

def update_student(data):
    roll_no = input("Enter Roll Number to update: ")
    if roll_no not in data:
        print("Student not found!")
        return
    
    print("Leave blank to keep current value.")
    name = input(f"Enter New Name ({data[roll_no]['name']}): ") or data[roll_no]['name']
    age = input(f"Enter New Age ({data[roll_no]['age']}): ") or data[roll_no]['age']
    marks = input(f"Enter New Marks ({data[roll_no]['marks']}): ") or data[roll_no]['marks']
    
    data[roll_no].update({"name": name, "age": age, "marks": marks})
    save_data(data)
    print("Student updated successfully!")

def delete_student(data):
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in data:
        del data[roll_no]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def main():
    data = load_data()
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1': add_student(data)
        elif choice == '2': view_students(data)
        elif choice == '3': update_student(data)
        elif choice == '4': delete_student(data)
        elif choice == '5': break
        else: print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
