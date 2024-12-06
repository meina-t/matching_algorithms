import logging

def serial_dictatorship(students, schools):
    for student in students.values():
        while student.matched_school is None:
            school_name = student.propose()
            logging.info(f"{student.name} proposed to {school_name}")
            if not school_name:
                break

            school = schools[school_name]
            if school.give_seat(student):
                student.matched_school = school
                logging.info(f"{school.name} accepted {student.name}")
            else:
                logging.info(f"{school.name} rejected {student.name}")

    return {school.name: [s.name for s in school.current_matches] for school in schools.values()}