import results


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