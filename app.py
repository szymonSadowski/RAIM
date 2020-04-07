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
    gender = get_gender()

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
                      multiple(request.form.getlist("activities_robot")),
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
    gender = get_gender()
    if request.method == "POST":

        c.execute("""INSERT INTO patient_topic
                               (type_telemedicine, how_telemedicine, test_results, visit, computer, attitude, 
                               respondent_id)
                                   VALUES (?,?,?,?,?,?,?)""",
                (
                      multiple(request.form.getlist("type_telemedicine")),
                      multiple(request.form.getlist("how_telemedicine")),
                      request.form.get("test_results"),
                      request.form.get("visit"),
                      request.form.get("computer"),
                      request.form.get("attitude"),
                      id
                )
        )
        conn.commit()
        if request.form.get("attitude") == "like" or request.form.get("attitude") == "concerns":
            return redirect(url_for("patient_end"))
        else:
            return redirect(url_for("home"))
    if gender == "male":
        return render_template("patient_topic.html", gender="Pan", have="miał", subject="poddałby",
                                   subject2="wyraziłby", subject3="korzystał")
    elif gender == "female":
        return render_template("patient_topic.html", gender="Pani", have="miała", subject="poddałaby",
                                   subject2="wyraziłaby", subject4="korzystała")

    return redirect(url_for("home"))


@app.route("/patient_end", methods=["GET" , "POST"])
def patient_end():
    conn = get_db()
    c = conn.cursor()
    id = get_id()
    gender = get_gender()

    if request.method == "POST":
        c.execute("""INSERT INTO patient_end
                               (why, respondent_id)
                                   VALUES (?,?)""",
                (
                      multiple(request.form.getlist("why")),
                      id
                )
        )
        conn.commit()
        return redirect(url_for("home"))
    if gender == "male":
        return render_template("patient_end.html", gender="Pan", have="miał", subject="poddałby",
                                   subject2="wyraziłby", subject3="korzystał", subject5="zdecydował")
    elif gender == "female":
         return render_template("patient_end.html", gender="Pani", have="miała", subject="poddałaby",
                                   subject2="wyraziłaby", subject4="korzystała", subject5="zdecydowała")

    return render_template("patient_record.html")

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

def get_gender():
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

    gender = row[1]
    return gender

def multiple(list):
    str = ""
    for answers in list:
        str = str + ", " + answers

    return str

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


