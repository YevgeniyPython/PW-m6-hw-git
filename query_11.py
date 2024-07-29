import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Середній бал, який певний викладач ставить певному студентові.

sql = """
SELECT ROUND(AVG(g.grade), 2) as avg_grade, st.student_name, t.teacher_name
FROM grades as g
LEFT JOIN students as st ON g.student_id = st.id
LEFT JOIN subjects as sj ON g.subject_id = sj.id
LEFT JOIN teachers as t ON sj.teacher_id = t.id
WHERE st.id = 14 AND t.id = 2
GROUP BY st.id;
"""


print(execute_query(sql))
