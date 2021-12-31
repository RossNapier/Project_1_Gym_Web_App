Running the App

Clone the files from my Github and cd into the root directory in terminal.

Create the database: In terminal, type ```createdb gym_app```
Then type:```psql -d gym_app -f db/gym_app.sql```

To seed the database, if desired: In temrinal, type ```python3 console.py```
This creates several instances of gym classes and members.

Finally, to run the app, in terminal type ```python3 flask run``` (some can omit the 'pyhton3'), which will run the app in your browser at http://localhost:5000/

Brief:

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
The app should allow the gym to create and edit Members The app should allow the gym to create and edit Classes The app should allow the gym to book members on specific classes The app should show a list of all upcoming classes The app should show all members that are booked in for a particular class Inspired By Glofox, Pike13

Possible Extensions
Classes could have a maximum capacity, and users can only be added while there is space remaining. The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours. The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

Technologies used:
Python3, Flask, Jinja, CSS, HTML, PostgresQL