import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("privatekey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://aats-6495e-default-rtdb.firebaseio.com/",
})

ref = db.reference('Students')

data = {
        "eng22cs0126":
        {
            "name": "punith kumar",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-05-29 08:35:34"
        },
        "eng22cs0129":
        {
            "name": "rahul jadvani",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-05-30 08:35:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)