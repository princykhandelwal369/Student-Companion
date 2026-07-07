from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    student={"name":"Princy Khandelwal","course":"B.Tech","year":2,"cgpa":8.5}
    stats={"attendance":85,"assignments_pending":3,"days_to_exam":12}
    schedule = [
        {"time": "9:00 AM", "subject": "Data Structures", "room": "Lab 3"},
        {"time": "11:00 AM", "subject": "Mathematics", "room": "Room 201"},
        {"time": "2:00 PM", "subject": "Python Programming", "room": "Lab 1"},
    ]

    return render_template("home.html",
        student=student,
        stats=stats,
        schedule=schedule
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


