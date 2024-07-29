from datetime import datetime
import faker
from random import randint
import sqlite3


NUMBER_GROUPS = 3
NUMBER_STUDENTS = 45
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers) -> tuple():
    fake_groups = [] 
    fake_students = [] 
    fake_teachers = []  
    fake_subjects = ["subject_1", "subject_2", "subject_3", "subject_4", "subject_5", "subject_6", "subject_7", "subject_8" ]
    # fake_subjects = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.numerify())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # for _ in range(number_subjects):
    #     fake_subjects.append(fake_data.company())

    return fake_groups, fake_students, fake_subjects, fake_teachers



def prepare_data(groups, students, subjects, teachers) -> tuple():
    for_groups = []

    for group in groups:
        for_groups.append((group, ))

    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = []

    for student in range(1, NUMBER_STUDENTS + 1):
        for x in range(randint(15, 20)):
            grade_date = datetime(2024, randint(1, 12), randint(1, 28)).date()
            for_grades.append((student, randint(1, NUMBER_SUBJECTS), randint(2, 5), grade_date))

    return for_groups, for_students, for_teachers, for_subjects, for_grades


def insert_data_to_db(groups, students, teachers, subjects, grades) -> None:

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_number)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(student_name, group_id)
                            VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_teachers ="""INSERT INTO teachers(teacher_name)
                               VALUES (?)"""
        
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                               VALUES (?, ?)"""
        
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_of)
                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    groups, students, teachers, subjects, grades = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS))
    insert_data_to_db(groups, students, teachers, subjects, grades)
