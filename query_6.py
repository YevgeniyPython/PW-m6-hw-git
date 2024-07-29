import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти список студентів у певній групі.

sql = """
SELECT s.student_name, g.group_number 
FROM students AS s
LEFT JOIN groups AS g ON s.group_id = g.id 
WHERE group_id = 3
"""


print(execute_query(sql))
