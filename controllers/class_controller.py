from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.class_repository as class_repo

classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = class_repo.select_all()
    return render_template("classes/show.html", all_classes = classes)