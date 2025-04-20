
push_ups = {
    "push-up": 2, 
    "sets": 3,
    "reps": 10,
    "rest": 90, #seconds
    "notes": "Really focus on form!",
}

#print out each key in the dictionary
keys = push_ups.keys()
print(keys)

#update the sets of the exercise
push_ups["sets"] = 2
print(push_ups["sets"])

#delete notes 
del push_ups["notes"]


#add a new key to the dictionary
push_ups["notes"] = "Really focus on form!"
print(push_ups)

workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}
