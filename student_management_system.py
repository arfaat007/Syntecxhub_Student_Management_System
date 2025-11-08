import json
import os
from typing import List, Optional


class Student:
    
    
    def __init__(self, student_id: str, name: str, grade: str):
        self.student_id = student_id
        self.name = name
        self.grade = grade
    
    def to_dict(self) -> dict:
        return {
            'student_id': self.student_id,
            'name': self.name,
            'grade': self.grade
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            student_id=data['student_id'],
            name=data['name'],
            grade=data['grade']
        )
    
    def __str__(self) -> str:
        return f"ID: {self.student_id:<10} | Name: {self.name:<25} | Grade: {self.grade}"


class StudentManager:
    
    def __init__(self, filename: str = 'students.json'):
        self.filename = filename
        self.students: List[Student] = []
        self.load_students()
    
    def load_students(self) -> None:
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    self.students = [Student.from_dict(student) for student in data]
                print(f"✓ Loaded {len(self.students)} student(s) from {self.filename}")
            except json.JSONDecodeError:
                print(f"⚠ Error reading {self.filename}. Starting with empty records.")
                self.students = []
        else:
            print(f"⚠ No existing file found. Starting fresh.")
            self.students = []
    
    def save_students(self) -> None:
        try:
            with open(self.filename, 'w') as file:
                data = [student.to_dict() for student in self.students]
                json.dump(data, file, indent=2)
            print(f"✓ Records saved successfully to {self.filename}")
        except Exception as e:
            print(f"✗ Error saving records: {e}")
    
    def validate_unique_id(self, student_id: str, exclude_id: Optional[str] = None) -> bool:
        for student in self.students:
            if student.student_id == student_id and student.student_id != exclude_id:
                return False
        return True
    
    def add_student(self, student_id: str, name: str, grade: str) -> bool:
        if not student_id.strip() or not name.strip() or not grade.strip():
            print("✗ Error: All fields are required and cannot be empty.")
            return False
        
        if not self.validate_unique_id(student_id):
            print(f"✗ Error: Student ID '{student_id}' already exists.")
            return False
        
        student = Student(student_id.strip(), name.strip(), grade.strip())
        self.students.append(student)
        self.save_students()
        print(f"✓ Student '{name}' added successfully!")
        return True
    
    def update_student(self, student_id: str, name: Optional[str] = None, 
                      grade: Optional[str] = None) -> bool:
        student = self.find_student(student_id)
        if not student:
            print(f"✗ Error: Student with ID '{student_id}' not found.")
            return False
        
        if name and name.strip():
            student.name = name.strip()
        if grade and grade.strip():
            student.grade = grade.strip()
        
        self.save_students()
        print(f"✓ Student '{student_id}' updated successfully!")
        return True
    
    def delete_student(self, student_id: str) -> bool:
        student = self.find_student(student_id)
        if not student:
            print(f"✗ Error: Student with ID '{student_id}' not found.")
            return False
        
        self.students.remove(student)
        self.save_students()
        print(f"✓ Student '{student_id}' deleted successfully!")
        return True
    
    def find_student(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def list_students(self) -> None:
        if not self.students:
            print("\n📋 No students found in the system.\n")
            return
        
        print("\n" + "=" * 70)
        print(f"{'STUDENT RECORDS':^70}")
        print("=" * 70)
        print(f"{'ID':<10} | {'Name':<25} | {'Grade'}")
        print("-" * 70)
        
        for student in self.students:
            print(student)
        
        print("=" * 70)
        print(f"Total Students: {len(self.students)}\n")


def display_menu() -> None:
    print("\n" + "=" * 50)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. List All Students")
    print("5. Find Student")
    print("6. Exit")
    print("=" * 50)


def main():
    manager = StudentManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add New Student ---")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            grade = input("Enter Student Grade: ").strip()
            manager.add_student(student_id, name, grade)
        
        elif choice == '2':
            print("\n--- Update Student ---")
            student_id = input("Enter Student ID to update: ").strip()
            student = manager.find_student(student_id)
            
            if student:
                print(f"Current details: {student}")
                name = input(f"Enter new name (press Enter to keep '{student.name}'): ").strip()
                grade = input(f"Enter new grade (press Enter to keep '{student.grade}'): ").strip()
                manager.update_student(
                    student_id, 
                    name if name else None, 
                    grade if grade else None
                )
            else:
                print(f"✗ Error: Student with ID '{student_id}' not found.")
        
        elif choice == '3':
            print("\n--- Delete Student ---")
            student_id = input("Enter Student ID to delete: ").strip()
            student = manager.find_student(student_id)
            
            if student:
                print(f"Student found: {student}")
                confirm = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    manager.delete_student(student_id)
                else:
                    print("✗ Deletion cancelled.")
            else:
                print(f"✗ Error: Student with ID '{student_id}' not found.")
        
        elif choice == '4':
            manager.list_students()
        
        elif choice == '5':
            print("\n--- Find Student ---")
            student_id = input("Enter Student ID to search: ").strip()
            student = manager.find_student(student_id)
            
            if student:
                print("\n✓ Student found:")
                print("-" * 70)
                print(student)
                print("-" * 70)
            else:
                print(f"✗ Error: Student with ID '{student_id}' not found.")
        
        elif choice == '6':
            print("\n👋 Thank you for using Student Management System!")
            print("Goodbye!\n")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
