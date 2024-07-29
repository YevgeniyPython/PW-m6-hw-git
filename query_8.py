import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти середній бал, який ставить певний викладач зі своїх предметів.

sql = """
SELECT ROUND(AVG(g.grade), 2) as avg_grade, t.teacher_name , s.subject_name
FROM grades as g
LEFT JOIN subjects as s ON g.subject_id = s.id
LEFT JOIN teachers as t ON s.teacher_id = t.id
WHERE t.id = 3
GROUP BY g.subject_id;
"""


print(execute_query(sql))
