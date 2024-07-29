import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Список курсів, які певному студенту читає певний викладач.

sql = """
SELECT sj.subject_name, st.student_name, t.teacher_name
FROM grades as g
LEFT JOIN students as st ON g.student_id = st.id
LEFT JOIN subjects as sj ON g.subject_id = sj.id
LEFT JOIN teachers as t ON sj.teacher_id = t.id
WHERE st.id = 5 AND t.id = 2
GROUP BY sj.subject_name;
"""


print(execute_query(sql))
