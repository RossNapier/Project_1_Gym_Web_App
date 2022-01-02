Issue with displaying classes:

schedule/member.html claims 'classes' is undefined

running console.py with pdb.set_trace() on classes(member) function in schedule_repo returns error:

<frozen importlib._bootstrap>(228)_call_with_frames_removed()->None

Google didn't help

schedule_controller handles the request, as it needs access to both class and member


#############################################################


Solved bugs:

psql would not run - solution: it had stopped running in background, restarted with ```brew services start postgresql```


#############################################################


Future features:

Show classes booked under member details
Cancel bookings
Cancel classes
Search for member
Homepage - next class, no. of members
Premium memberships