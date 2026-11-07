import storage
from student import Student

students = storage.load_students()

records = [
    ("STU001", "Ada Obi", "SS2", "F", "2008-05-21"),
    ("STU002", "John Bello", "SS2", "M", "2007-01-10"),
    ("STU003", "Grace Adeyemi", "SS1", "F", "2009-03-15"),
    ("STU004", "Samuel Okafor", "SS3", "M", "2006-11-02"),
    ("STU005", "Fatima Yusuf", "SS2", "F", "2008-08-30"),
]

for student_id, name, class_name, gender, dob in records:
    if student_id not in students:
        students[student_id] = Student(student_id, name, class_name, gender, dob)

storage.save_students(students)
print(len(students), "students in the system.")