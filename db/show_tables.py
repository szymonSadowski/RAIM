import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/raim.db'
print("Options: (respondent, all)")

table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

def show_respondent():
    try:
        respondent = c.execute("""SELECT
                                    c.id, c.gender, c.age, c.edu , c.city
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
            print("City:           ", row[4])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


if table == "respondent":
    show_respondent()
elif table == "all":
    show_respondent()
else:
    print("This option does not exist.")

conn.close()