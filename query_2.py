import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# "Find the student with the highest average score in a singing subject. In this case "subject_id = 2"

sql = """
SELECT ROUND(AVG(g.grade), 2) AS avg_grade, e.student_name, g.subject_id
FROM grades as g
LEFT JOIN students as e ON g.student_id = e.id
WHERE g.subject_id = 2
GROUP BY g.subject_id, e.student_name 
ORDER BY ROUND(AVG(g.grade), 2) DESC
LIMIT 1;
"""


print(execute_query(sql))
