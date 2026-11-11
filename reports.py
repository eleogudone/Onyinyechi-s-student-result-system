import results
import os
from datetime import datetime


def report_card(student):
    lines = []
    lines.append("=" * 44)
    lines.append("           STUDENT REPORT CARD")
    lines.append("=" * 44)
    lines.append(f"ID     : {student.student_id}")
    lines.append(f"Name   : {student.name}")
    lines.append(f"Class  : {student.class_name}")
    lines.append(f"Gender : {student.gender}")
    lines.append(f"DOB    : {student.dob}")
    lines.append("-" * 44)
    lines.append(f"{'Subject':<26}{'Score':>8}")
    lines.append("-" * 44)
    for subject, score in student.scores.items():
        lines.append(f"{subject:<26}{score:>8.1f}")
    lines.append("-" * 44)
    lines.append(f"{'Total':<26}{student.total():>8.1f}")
    lines.append(f"{'Average':<26}{student.average():>8.2f}")
    lines.append(f"{'Grade':<26}{student.grade():>8}")
    lines.append(f"Results entered: {student.date_entered or 'N/A'}")
    lines.append("=" * 44)
    if len(student.scores) < results.MIN_SUBJECTS:
        lines.append("Note: fewer than 5 subjects recorded.")
    return "\n".join(lines)
def sort_students(students, by="average"):
    """students is a list. Sort by 'average' (high to low) or 'name' (A to Z)."""
    if by == "name":
        return sorted(students, key=lambda s: s.name.lower())
    return sorted(students, key=lambda s: s.average(), reverse=True)


def student_table(students):
    line = "-" * 78
    rows = [line,
            f"{'ID':<9}{'Name':<26}{'Class':<10}{'Total':>8}{'Average':>10}{'Grade':>8}",
            line]
    for s in students:
        rows.append(f"{s.student_id:<9}{s.name[:24]:<26}{s.class_name:<10}"
                    f"{s.total():>8.1f}{s.average():>10.2f}{s.grade():>8}")
    rows.append(line)
    return "\n".join(rows)


def statistics_text(students):
    stats = results.class_statistics(students)
    if stats is None:
        return "No results recorded yet."
    return "\n".join([
        "CLASS STATISTICS",
        f"Students with results : {stats['count']}",
        f"Class average         : {stats['class_average']:.2f}",
        f"Top student           : {stats['top_name']} ({stats['top_average']:.2f})",
        f"Lowest student        : {stats['low_name']} ({stats['low_average']:.2f})",
        f"Highest single score  : {stats['highest_score']:.1f}",
        f"Lowest single score   : {stats['lowest_score']:.1f}",
    ])


def full_report(students):
    ranked = sort_students(students, "average")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return (f"STUDENT RESULT REPORT - generated {stamp}\n\n"
            f"{student_table(ranked)}\n\n"
            f"{statistics_text(students)}\n")


def save_report(text):
    """Save the report text to reports/report_<date-time>.txt. Returns the path."""
    try:
        os.makedirs("reports", exist_ok=True)
        name = datetime.now().strftime("report_%Y%m%d_%H%M%S.txt")
        path = os.path.join("reports", name)
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
    except OSError as error:
        print("Could not save report:", error)
        return None
    else:
        return path