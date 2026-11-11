import storage
import results
import reports
from student import Student, is_valid_id, is_valid_dob

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
    dob = ask("Date of birth (YYYY-MM-DD): ", is_valid_dob,
              "Use a real past date like 2008-05-21.")

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

def ask_score(subject):
    """Ask for a score until it is a valid number from 0 to 100."""
    while True:
        text = input(f"  {subject} score (0-100): ").strip()
        try:
            return results.validate_score(text)
        except ValueError:
            print("  Invalid. Enter a number from 0 to 100.")


def record_scores(students):
    student_id = input("\nEnter Student ID: ").strip().upper()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
        return

    print(f"Enter scores for {student.name}:")
    for subject in results.DEFAULT_SUBJECTS:
        student.set_score(subject, ask_score(subject))

    while input("Add another subject? (y/n): ").strip().lower() == "y":
        subject = input("  Subject name: ").strip().title()
        if subject != "":
            student.set_score(subject, ask_score(subject))

    print(f"Saved. Average {student.average():.2f}, Grade {student.grade()}.")


def update_score(students):
    student_id = input("\nEnter Student ID: ").strip().upper()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
        return
    if not student.scores:
        print("This student has no scores yet.")
        return

    print("Subjects:", ", ".join(student.scores))
    subject = input("Subject to update: ").strip().title()
    if subject not in student.scores:
        print("Subject not found.")
        return
    student.set_score(subject, ask_score(subject))
    print("Score updated.")


def show_report_card(students):
    student_id = input("\nEnter Student ID: ").strip().upper()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
        return
    print("\n" + reports.report_card(student))

def list_results(students):
    if not students:
        print("No students registered.")
        return
    choice = input("\nSort by (1) average high-to-low or (2) name: ").strip()
    by = "name" if choice == "2" else "average"
    ordered = reports.sort_students(list(students.values()), by)
    print("\n" + reports.student_table(ordered))


def show_statistics(students):
    print("\n" + reports.statistics_text(list(students.values())))


def export_report(students):
    if not students:
        print("Nothing to report.")
        return
    text = reports.full_report(list(students.values()))
    path = reports.save_report(text)
    if path:
        print("Report saved to", path)

def main():
    students = storage.load_students()

    while True:
        print("\n===== STUDENT RESULT SYSTEM =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Record scores")
        print("7. Update a score")
        print("8. Display report card")
        print("9. List results (sorted)")
        print("10. Class statistics")
        print("11. Save report to file")
        print("0. Save and exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            record_scores(students)
        elif choice == "7":
            update_score(students)
        elif choice == "8":
            show_report_card(students)
        elif choice == "9":
            list_results(students)
        elif choice == "10":
            show_statistics(students)
        elif choice == "11":
            export_report(students)
        elif choice == "0":
            storage.save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

        storage.save_students(students)


main()

