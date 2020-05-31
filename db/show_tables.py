import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/home/medicalSurveyRAIM/mysite/db//raim.db'
print("Options: (respondent, patient_record, patient_topic, patient_end, respondent_doctor,"
      " doctor_record, doctor_topic, doctor_end,  all)")

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

        print("RESPONDENT")
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

        print("PATIENT RECORD")
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

        print("PATIENT TOPIC")
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

def show_patientEnd():
    try:
        respondent = c.execute("""SELECT
                                    c.id, c.why, c.respondent_id
                                 FROM
                                    patient_end AS c
        """)

        print("PATIENT END")
        print("#############")
        for row in respondent:
            print("ID:             ", row[0]),
            print("Why:        ",  row[1]),
            print("Respondent Id:           ",  row[2]),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_respondentDoctor():
    try:
        respondent_doctor = c.execute("""SELECT
                                    c.id, c.gender, c.age, c.city, c.politics
                                 FROM
                                    respondent_doctor AS c
        """)

        print("RESPONDENT DOCTOR")
        print("#############")
        for row in respondent_doctor:
            print("ID:             ", row[0]),
            print("Gender:        ",  row[1]),
            print("Age:           ",  row[2]),
            print("City:           ", row[3]),
            print("Politics:        ", row[4])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_doctorRecord():
    try:
        doctor_record = c.execute("""SELECT
                                    c.id, c.activities_robot, c.computer, c.disadvantage, c.job, c.telemedicine,
                                    c.respondent_doctor_id
                                 FROM
                                    doctor_record AS c
        """)

        print("DOCTOR RECORD")
        print("#############")
        for row in doctor_record:
            print("ID:             ", row[0]),
            print("activities_robot:        ",  row[1]),
            print("Computer:           ",  row[2]),
            print("Disadvantage:            ", row[3]),
            print("Job:           ", row[4]),
            print("Telemedicine:        ", row[5]),
            print("Doctor ID :        ", row[6]),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


def show_doctorTopic():
    try:
        doctor_topic = c.execute("""SELECT
                                     c.id, c.type_telemedicine, c.how_telemedicine, c.test_results, c.visit,
                                     c.attitude, c.respondent_doctor_id
                                  FROM
                                     doctor_topic AS c
         """)

        print("DOCTOR TOPIC")
        print("#############")
        for row in doctor_topic:
            print("ID:             ", row[0]),
            print("TeleMedicine:        ", row[1]),
            print("How Telemedicine:           ", row[2]),
            print("Test Results:            ", row[3]),
            print("Visit:           ", row[4]),
            print("Attitude:        ", row[5]),
            print("Doctor ID:        ", row[6]),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_doctorEnd():
    try:
        doctor_end = c.execute("""SELECT
                                    c.id, c.why, c.respondent_doctor_id
                                 FROM
                                    doctor_end AS c
        """)

        print("DOCTOR END")
        print("#############")
        for row in doctor_end:
            print("ID:             ", row[0]),
            print("Why:        ",  row[1]),
            print("Doctor Id:           ",  row[2]),
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
elif table == "patient_end":
    show_patientEnd()
elif table == "respondent_doctor":
    show_respondentDoctor()
elif table == "doctor_record":
    show_doctorRecord()
elif table == "doctor_topic":
    show_doctorTopic()
elif table == "doctor_end":
     show_doctorEnd()
elif table == "all":
    show_respondent()
    show_patientRecord()
    show_patientTopic()
    show_patientEnd()
    show_respondentDoctor()
    show_doctorRecord()
    show_doctorTopic()
    show_doctorEnd()
else:
    print("This option does not exist.")

conn.close()