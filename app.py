
from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]

        students.append({
            "name": name,
            "status": status
        })

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
