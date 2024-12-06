import logging

def defered_acceptance(students, schools):
    unmatched_students = list(students.values())
    while unmatched_students:
        student = unmatched_students.pop(0)
        school_name = student.propose()
        logging.info(f"{student.name} proposed to {school_name}")
        if not school_name:
            continue

        school = schools[school_name]
        rejected_student = school.accept_proposal(student)
        logging.info(f"{school.name} accepted {student.name} and rejected {rejected_student.name if rejected_student else None}")

        if rejected_student:
            unmatched_students.append(rejected_student)

    return {school.name: [s.name for s in school.current_matches] for school in schools.values()}
