def defered_acceptance(students, schools):
    unmatched_students = list(students.values())
    while unmatched_students:
        student = unmatched_students.pop(0)
        school_name = student.propose()
        if not school_name:
            continue

        school = schools[school_name]
        rejected_student = school.accept_proposal(student)

        if rejected_student:
            unmatched_students.append(rejected_student)

    return {school.name: [s.name for s in school.current_matches] for school in schools.values()}
