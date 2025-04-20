
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

#delete notes 
del push_ups["notes"]