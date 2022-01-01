from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo
import repositories.schedule_repository as schedule_repo

schedule_blueprint = Blueprint("schedule", __name__)


# Creates form to allow assigning member to class
@schedule_blueprint.route("/book")
def book():
    class_repo.check_all_classes()
    members = member_repo.select_active_members()
    classes = class_repo.select_available_classes()
    return render_template("schedule/new.html", members = members, classes = classes)


# Saves assignment from above form
@schedule_blueprint.route("/schedule/new", methods = ['POST'])
def assign_member_to_class():
    member_id = request.form['member_id']
    class_id = request.form['class_id']
    gym_class = class_repo.select(class_id)
    schedule_repo.save_by_id(member_id, class_id)
    class_repo.check_class(gym_class)
    return redirect("/classes")


# Changes route based on whether a class is fully booked or not, presents list of attendees
@schedule_blueprint.route("/schedule/<id>")
def show(id):
    gym_class = class_repo.select(id)
    members = class_repo.members(gym_class)
    if gym_class.fully_booked == False:
        return render_template("schedule/show.html", gym_class = gym_class, members = members)
    else:
        return render_template("schedule/booked.html", gym_class = gym_class, members = members)


# Displays member details with classes booked
@schedule_blueprint.route("/schedule/member/<id>")
def show_member(id):
    member = member_repo.select(id)
    classes = member_repo.classes(member)
    return render_template("schedule/member.html", classes = classes, member = member)