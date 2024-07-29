import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти список курсів, які відвідує студент.

sql = """
SELECT st.student_name , sj.subject_name
FROM grades as g
LEFT JOIN students as st ON g.student_id = st.id
LEFT JOIN subjects as sj ON g.subject_id = sj.id
WHERE st.id = 2
GROUP BY sj.subject_name;
"""


print(execute_query(sql))
