from flask import Flask, render_template
from controllers.member_controller import members_blueprint
from controllers.class_controller import classes_blueprint
from controllers.schedule_controller import schedule_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(schedule_blueprint)

# Homepage for app
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)