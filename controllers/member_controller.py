from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.member_repository as member_repo
from models.member import Member

members_blueprint = Blueprint("members", __name__)


# Lists all from members table in database
@members_blueprint.route("/members")
def members():
    members = member_repo.select_active_members()
    return render_template("members/show.html", all_members = members)


# Displays a form allowing new member input
@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
    return render_template("members/new.html")


# Saves the form details to the members table in database
@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    phone_no = request.form['phone_no']
    new_member = Member(first_name, second_name, phone_no)
    member_repo.save(new_member)
    return redirect('/members')


# Allows user to edit exisiting details via a form
@members_blueprint.route("/members/<id>/edit", methods = ['GET'])
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member = member)


# Updates members table in database with editted member from above form
@members_blueprint.route("/members/<id>", methods = ['POST'])
def update_member(id):
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    phone_no = request.form['phone_no']
    active = request.form['active']
    member = Member(first_name, second_name, phone_no, active, id)
    if active == "no":
        Member.inactive(member)
    else:
        Member.active(member)
    member_repo.update(member)
    return redirect('/members')


# Displays inactive members with edit (allowing to reactivate account)
@members_blueprint.route("/members/inactive")
def inactive_members():
    members = member_repo.select_inactive_members()
    return render_template("members/inactive.html", all_members = members)