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
       return redirect(url_for("patient2"))
    return render_template("patient.html")


@app.route("/patient2",  methods=["GET", "POST"])
def patient2():
    conn = get_db()
    c = conn.cursor()
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
            return render_template("patient_record.html",gender="Pan",have="miał",subject="poddałby")
        elif gender =="female":
            return render_template("patient_record.html",gender="Pani",have="miała",subject="poddałaby")


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

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
