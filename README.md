# Student Management System

A CLI-based Student Management System built with Python that allows you to manage student records efficiently.

## Features

- **Add Student** - Create new student records with unique ID validation
- **Update Student** - Modify existing student information
- **Delete Student** - Remove students with confirmation prompt
- **List Students** - Display all records in a formatted table
- **Find Student** - Search for specific students by ID
- **Data Persistence** - Automatic saving to JSON file
- **Input Validation** - Ensures unique student IDs and required fields

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

2. No additional dependencies required (uses Python standard library)

## Usage

Run the application:
```bash
python student_management_system.py
```

### Menu Options

1. **Add Student** - Enter student ID, name, and grade
2. **Update Student** - Modify name or grade of existing student
3. **Delete Student** - Remove a student record (with confirmation)
4. **List All Students** - View all students in a formatted table
5. **Find Student** - Search for a student by ID
6. **Exit** - Close the application

## Data Storage

Student records are automatically saved to `students.json` in the same directory. The file is created automatically on first use and loaded on subsequent runs.

## Example

```
=================================================
  STUDENT MANAGEMENT SYSTEM
=================================================
1. Add Student
2. Update Student
3. Delete Student
4. List All Students
5. Find Student
6. Exit
=================================================
Enter your choice (1-6): 1

--- Add New Student ---
Enter Student ID: S001
Enter Student Name: John Doe
Enter Student Grade: A
✓ Student 'John Doe' added successfully!
```

## Project Structure

- `student_management_system.py` - Main application file
- `students.json` - Data storage (auto-generated)

## Classes

### Student
Represents a student record with:
- `student_id` - Unique identifier
- `name` - Student's name
- `grade` - Student's grade/class

### StudentManager
Handles all operations:
- CRUD operations (Create, Read, Update, Delete)
- File persistence (JSON format)
- ID validation
- Formatted console output
