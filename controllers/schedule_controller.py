from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.schedule import Schedule
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo
import repositories.schedule_repository as schedule_repo

schedule_blueprint = Blueprint("schedule", __name__)

@schedule_blueprint.route("/schedule")
def schedule():
    schedule = schedule_repo.select_all()
    return "Hello"