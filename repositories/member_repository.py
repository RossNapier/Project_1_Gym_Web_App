from db.run_sql import run_sql

from models.gym_class import Class
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, second_name, phone_no) VALUES (%s, %s, %s) RETURNING *"
    values = [member.first_name, member.second_name, member.phone_no]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member