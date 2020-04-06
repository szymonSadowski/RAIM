import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/raim.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS respondent")
c.execute("DROP TABLE IF EXISTS patient_record")
c.execute("DROP TABLE IF EXISTS patient_topic")

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
c.executemany("INSERT INTO respondent (gender,age,edu,city,politics) VALUES (?,?,?,?,?)", respondent)

c.execute("""CREATE TABLE patient_record(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    hospitalization            TEXT,
                    drugs    TEXT,
                    operation TEXT,
                    health_service TEXT,
                    operation_robot TEXT,
                    activities_robot TEXT,
                    disadvantage TEXT,
                    telemedicine TEXT
                    
)""")

patient_record = [
    ("yes","yes","yes","private","yes","interview","yes","yes")

]
c.executemany("INSERT INTO patient_record (hospitalization, drugs, operation, health_service, "
              "operation_robot, activities_robot, disadvantage, telemedicine) VALUES (?,?,?,?,?,?,?,?)", patient_record)


c.execute("""CREATE TABLE patient_topic(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    type_telemedicine            TEXT,
                    how_telemedicine    TEXT,
                    test_results,
                    visit TEXT,
                    computer TEXT,
                    attitude TEXT,
                    respondent_id INTEGER,
                    FOREIGN KEY(respondent_id) REFERENCES respondent(id)
)""")

patient_topic = [
    ("diagnosis","phone","no","yes","yes","like",1)

]
c.executemany("INSERT INTO patient_topic (type_telemedicine, how_telemedicine, test_results, visit, computer,"
              " attitude, respondent_id)"
              " VALUES (?,?,?,?,?,?,?)", patient_topic)

conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the tables with the show_tables.py script.")
