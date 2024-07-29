import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти середній бал у групах з певного предмета.

sql = """
SELECT ROUND(AVG(g.grade), 2) AS avg_grade, c.group_number , s.subject_name
FROM grades as g 
LEFT JOIN students as e ON g.student_id = e.id
LEFT JOIN groups as c ON e.group_id = c.id
LEFT JOIN subjects as s ON g.subject_id = s.id
WHERE g.subject_id = 3
GROUP BY e.group_id 
ORDER BY ROUND(AVG(g.grade), 2) DESC
;
"""


print(execute_query(sql))
