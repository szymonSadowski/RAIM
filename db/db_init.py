import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/raim.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS respondent")

c.execute("""CREATE TABLE respondent(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    gender            TEXT,
                    age    TEXT,
                    edu TEXT,
                    city TEXT,
                    politics TEXT
)""")

respondent = [
    ("MALE","40-60","higer","over500","right")

]
c.executemany("INSERT INTO respondent (gender,age,edu,city) VALUES (?,?,?,?,?)", respondent)

conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the tables with the show_tables.py script.")
