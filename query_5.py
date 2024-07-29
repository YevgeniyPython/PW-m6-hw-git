import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти які курси читає певний викладач.

sql = """
SELECT s.subject_name, t.teacher_name 
FROM subjects as s
LEFT JOIN teachers as t ON s.teacher_id = t.id
WHERE t.id = 2
"""


print(execute_query(sql))
