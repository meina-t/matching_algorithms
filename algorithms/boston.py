import logging

def boston(students, schools):
    unmatched_students = list(students.values())
    while unmatched_students:
        for student in unmatched_students:
            school_name = student.propose()
            logging.info(f"{student.name} proposed to {school_name}")
            if school_name is None:
                unmatched_students.remove(student)
                continue
            schools[school_name].temp_matches.append(student)
        unmatched_students.clear()
        for school in schools.values():
            rejected_students = school.select_to_q()
            unmatched_students.extend(rejected_students)
            logging.info(f"{school.name} accepted {school.current_matches} and rejected {rejected_students}")
    return {school.name: [s.name for s in school.current_matches] for school in schools.values()}
