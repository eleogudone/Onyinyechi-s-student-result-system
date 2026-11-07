import storage
from student import Student, is_valid_id

def ask(prompt, check, error_message):
    """"Keep asking until the answer passes the check."""
    while True:
        value = input(prompt).strip()
        if check(value):
            return value
        print(error_message)
def add_student(students):
    print("\n--- Add Student ---")
    student_id = ask("Student ID (e.g. STU001): ",
                     lambda v: is_valid_id(v.upper()),
                     "ID must look like STU001.").upper()

    if student_id in students:
        print("That ID already exists.")
        return

    name = ask("Full name: ", lambda v: len(v) >= 2,
               "Name is too short.").title()
    class_name = ask("Class/Form (e.g. SS2): ", lambda v: v != "",
                     "Cannot be empty.").upper()
    gender = ask("Gender (M/F): ", lambda v: v.upper() in ("M", "F"),
                 "Enter M or F.").upper()
    dob = ask("Date of birth (YYYY-MM-DD): ", lambda v: len(v) == 10,
              "Use the format 2008-05-21.")

    students[student_id] = Student(student_id, name, class_name, gender, dob)
    print(f"Student {name} added.")
def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students registered.")
        return
    for student in students.values():
        print(student)


def search_students(students):
    term = input("\nSearch by ID or name: ").strip().lower()
    found = False
    for student in students.values():
        if term == student.student_id.lower() or term in student.name.lower():
            print(student)
            found = True
    if not found:
        print("No match found.")


def delete_student(students):
    student_id = input("\nEnter ID to delete: ").strip().upper()
    if student_id not in students:
        print("Student not found.")
        return
    confirm = input(f"Delete {students[student_id].name}? (y/n): ").lower()
    if confirm == "y":
        del students[student_id]
        print("Student deleted.")
    else:
        print("Cancelled.")
def update_student(students):
    student_id = input("\nEnter ID to update: ").strip().upper()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{student.name}]: ").strip()
    class_name = input(f"Class [{student.class_name}]: ").strip()

    if name != "":
        student.name = name.title()
    if class_name != "":
        student.class_name = class_name.upper()
    print("Student updated.")