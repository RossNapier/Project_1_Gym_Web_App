from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.class_repository as class_repo
from models.gym_class import Class

classes_blueprint = Blueprint("classes", __name__)

# Lists all from classes table in database
@classes_blueprint.route("/classes")
def classes():
    class_repo.check_all_classes()
    classes = class_repo.select_all()
    return render_template("classes/show.html", all_classes = classes)


# Displays a form allowing new class input
@classes_blueprint.route("/classes/new", methods = ['GET'])
def new_class():
    return render_template("classes/new.html")


# Saves the form details to the classes table in database
@classes_blueprint.route("/classes", methods = ['POST'])
def create_class():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    new_class = Class(name, date, time, duration)
    class_repo.save(new_class)
    return redirect('/classes')


# Allows user to edit existing class details via a form
@classes_blueprint.route("/classes/<id>/edit", methods = ['GET'])
def edit_class(id):
    gym_class = class_repo.select(id)
    return render_template("classes/edit.html", gym_class = gym_class)


# Updates classes table in database with editted class from above form
@classes_blueprint.route("/classes/<id>", methods = ['POST'])
def update_class(id):
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    gym_class = Class(name, date, time, duration, False, id)
    class_repo.update(gym_class)
    return redirect('/classes')