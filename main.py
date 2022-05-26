from flask import Flask, render_template, url_for, request, redirect
from studentsdb import Database

app = Flask(__name__)
database = Database()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        database.register_st(name=name, surname=surname)
        return redirect(url_for("home"))
    else:
        data = database.select()
        return render_template('home.html', data= data)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    st_id = int(request.form["student_id"])
    database.delete_student(st_id)
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    student_id = request.form["student_id"]
    data = database.select_user_for_update(student_id)
    return render_template('edit.html', data = data)


@app.route("/main", methods=["GET", "POST"])
def main():
    if request.form["action"] == "UPDATE":
        name = request.form["name"]
        id = int(request.form["stud_id"])
        surname = request.form["surname"]
        math = int(request.form["math"])
        history = int(request.form["history"])
        html = int(request.form["html"])

        database.update_students(student_id=id, name=name, surname=surname, math=math, history=history, html=html)
        return redirect(url_for("home"))
    
    elif request.form['action'] == "EDIT":       
        student_id = int(request.form['student_id'])
        return redirect(url_for('edit', student_id = student_id))

    elif request.form["action"] == "BACK":
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

