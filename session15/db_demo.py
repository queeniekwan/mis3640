import dbm
import random

ROSTER = (
    "Alvie",
    "Christian",
    "Catherine",
    "Daniel",
    "Eli",
    "Andrew",
    "Grace",
    "Kenzi",
    "Ivy",
    "Lucas",
    "Ray",
    "Nathan",
    "Rumeer",
    "Sean",
    "Takaki",
    "Rachel",
    "Angela",
    "Queenie",
    "Zoe",
)

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-"]

db = dbm.open("session14/db_student.db", "c")

for student in ROSTER:
    db[student] = random.choice(GRADES)

for key in db:
    print(key, db[key])


db.close()
