import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти середній бал на потоці (по всій таблиці оцінок)

sql = """
SELECT ROUND(AVG(grade), 2) AS avg_grade
FROM grades;
"""


print(execute_query(sql))