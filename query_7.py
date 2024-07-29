import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти оцінки студентів у окремій групі з певного предмета.

sql = """
SELECT g.grade, s.student_name , sj.subject_name, gr.group_number 
FROM grades as g 
LEFT JOIN students as s ON g.student_id = s.id
LEFT JOIN groups as gr ON s.group_id = gr.id
LEFT JOIN subjects as sj ON g.subject_id = sj.id
WHERE g.subject_id = 3 AND gr.id = 2
ORDER BY s.student_name ASC;
"""


print(execute_query(sql))
