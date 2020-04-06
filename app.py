from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for,g)
import sqlite3


app = Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/patient", methods=["GET", "POST"] )

def patient():
    conn = get_db()
    c = conn.cursor()
    if request.method == "POST":
       c.execute("""INSERT INTO respondent
                            (gender, age, edu, city,politics)
                                VALUES (?,?,?,?,?)""",
              (
                  request.form.get("gender"),
                  request.form.get("age"),
                  request.form.get("edu"),
                  request.form.get("city"),
                  request.form.get("politics")
              )
       )
       conn.commit()
    # Redirect to some page
       return redirect(url_for("patient_record"))
    return render_template("patient.html")


@app.route("/patient_record",  methods=["GET", "POST"])
def patient_record():
    conn = get_db()
    c = conn.cursor()
    if request.method == "POST":
        c.execute("""INSERT INTO patient_record
                               (hospitalization, drugs, operation, health_service, operation_robot, activities_robot, 
                               disadvantage, telemedicine)
                                   VALUES (?,?,?,?,?,?,?,?)""",
                (
                      request.form.get("hospitalization"),
                      request.form.get("drugs"),
                      request.form.get("operation"),
                      request.form.get("health_service"),
                      request.form.get("operation_robot"),
                      request.form.get("activities_robot"),
                      request.form.get("disadvantage"),
                      request.form.get("telemedicine")
                )
        )
        conn.commit()
    # Redirect to some page
        if request.form.get("telemedicine") == "yes":
            return redirect(url_for("patient_topic"))
        else:
            return redirect(url_for("home"))

    items_from_db = c.execute("""SELECT 
                    i.id, i.gender
                    FROM
                    respondent AS i
                    ORDER BY i.id DESC LIMIT 1
    """)
    respondent = []
    for row in items_from_db:
        respondent = {
            "id": row[0],
            "gender": row[1],
        }
        print(respondent)
        gender=row[1]
        if gender == "male":
            return render_template("patient_record.html",gender="Pan",have="miał",subject="poddałby",subject2="wyraziłby",subject3="korzystał")
        elif gender =="female":
            return render_template("patient_record.html",gender="Pani",have="miała",subject="poddałaby",subject2="wyraziłaby",subject4="korzystała")


    return render_template("patient_record.html")

@app.route("/patient_topic", methods=["GET", "POST"])
def patient_topic():
    conn = get_db()
    c = conn.cursor()
    id = get_id()
    if request.method == "POST":

        c.execute("""INSERT INTO patient_topic
                               (type_telemedicine, how_telemedicine, test_results, visit, computer, attitude, 
                               respondent_id)
                                   VALUES (?,?,?,?,?,?,?)""",
                (
                      request.form.get("type_telemedicine"),
                      request.form.get("how_telemedicine"),
                      request.form.get("test_results"),
                      request.form.get("visit"),
                      request.form.get("computer"),
                      request.form.get("attitude"),
                      id
                )
        )
        conn.commit()
    items_from_db = c.execute("""SELECT 
                       i.id, i.gender
                       FROM
                       respondent AS i
                       ORDER BY i.id DESC LIMIT 1
       """)
    respondent = []
    for row in items_from_db:
        respondent = {
            "id": row[0],
            "gender": row[1],
        }
        print(respondent)
        gender = row[1]
        respondent_id=row[0]
        if gender == "male":
            return render_template("patient_topic.html", gender="Pan", have="miał", subject="poddałby",
                                   subject2="wyraziłby", subject3="korzystał")
        elif gender == "female":
            return render_template("patient_topic.html", gender="Pani", have="miała", subject="poddałaby",
                                   subject2="wyraziłaby", subject4="korzystała")


    return redirect(url_for("home"))

@app.route("/doctor", methods=["GET", "POST"])
def doctor():
    if request.method == "POST":
        # Process the form data
        print("Form data:")
        print("Title: {}, Description: {}".format(
            request.form.get("title"), request.form.get("description")
        ))

        return redirect(url_for("home"))

    return render_template("doctor.html")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db/raim.db')
    return db

def get_id():
    conn = get_db()
    c = conn.cursor()
    items_from_db = c.execute("""SELECT 
                       i.id, i.gender
                       FROM
                       respondent AS i
                       ORDER BY i.id DESC LIMIT 1
       """)
    for row in items_from_db:
        respondent = {
            "id": row[0],
            "gender": row[1],
        }

    respondent_id = row[0]
    return respondent_id

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


