import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# "Find the 5 students with the highest grade point average in all subjects."

sql = """
SELECT ROUND(AVG(g.grade), 2) AS avg_grade, e.student_name
FROM grades as g
LEFT JOIN students as e ON g.student_id = e.id
GROUP BY e.student_name
ORDER BY ROUND(AVG(g.grade), 2) DESC
LIMIT 5;
"""


print(execute_query(sql))
