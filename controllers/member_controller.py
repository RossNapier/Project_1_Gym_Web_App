from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.member_repository as member_repo
from models.member import Member

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/show.html", all_members = members)

@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
    return render_template("members/new.html")

@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    phone_no = request.form['phone_no']
    new_member = Member(first_name, second_name, phone_no)
    member_repo.save(new_member)
    return redirect('/members')