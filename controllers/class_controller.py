from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.class_repository as class_repo
from models.gym_class import Class

classes_blueprint = Blueprint("classes", __name__)

# Lists all from classes table in database
@classes_blueprint.route("/classes")
def classes():
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