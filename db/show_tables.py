import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/raim.db'
print("Options: (respondent, patient_record, patient_topic,  all)")

table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

def show_respondent():
    try:
        respondent = c.execute("""SELECT
                                    c.id, c.gender, c.age, c.edu , c.city, c.politics
                                 FROM
                                    respondent AS c        
        """)

        print("COMMENTS")
        print("#############")
        for row in respondent:
            print("ID:             ", row[0]),
            print("Gender:        ",  row[1]),
            print("Age:           ",  row[2]),
            print("Edu:            ", row[3]),
            print("City:           ", row[4]),
            print("Politics:        ", row[5])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_patientRecord():
    try:
        patient_record = c.execute("""SELECT
                                    c.id, c.hospitalization, c.drugs, c.operation , c.health_service, c.operation_robot,
                                    c.activities_robot, c.disadvantage, c.telemedicine
                                 FROM
                                    patient_record AS c        
        """)

        print("COMMENTS")
        print("#############")
        for row in patient_record:
            print("ID:             ", row[0]),
            print("Hospitalization:        ",  row[1]),
            print("Drugs:           ",  row[2]),
            print("Operation:            ", row[3]),
            print("Health Service Provider:           ", row[4]),
            print("Operation done by robot:        ", row[5]),
            print("Activites robot:        ", row[6]),
            print("Disadvantage:        ", row[7]),
            print("Telemedicine:        ", row[8]),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


def show_patientTopic():
    try:
        patient_topic = c.execute("""SELECT
                                     c.id, c.type_telemedicine, c.how_telemedicine, c.test_results, c.visit, 
                                     c.computer, c.attitude, c.respondent_id
                                  FROM
                                     patient_topic AS c        
         """)

        print("COMMENTS")
        print("#############")
        for row in patient_topic:
            print("ID:             ", row[0]),
            print("TeleMedicine:        ", row[1]),
            print("How Telemedicine:           ", row[2]),
            print("Test Results:            ", row[3]),
            print("Visit:           ", row[4]),
            print("Computer:        ", row[5]),
            print("Attitude:        ", row[6]),
            print("respondent_id:        ", row[7]),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


if table == "respondent":
    show_respondent()
elif table == "patient_record":
    show_patientRecord()
elif table == "patient_topic":
    show_patientTopic()
elif table == "all":
    show_respondent()
    show_patientRecord()
    show_patientTopic()
else:
    print("This option does not exist.")

conn.close()