# Store Data In Key Value Pair
user = {
    "name": "Umar Farooq",
    "age": None,
    "isAlive": True,
    "subjects": ["Javascript", "Typescript", "Python"],
}

# For Printing Simple One Value
print(user["name"])
print(user["age"])
print(user["isAlive"])
print(user["subjects"])

# For Changing Values
user["name"] = "Ayesha"
user["age"] = 20
print(user["name"])
print(user["age"])

# Nested Dictionary
student = {
    "name": "Anusha",
    "age": 21,
    "subjects": {
        "math": 0,
        "phy": 0,
        "chem": 0,
    },
    "total_score": 0,
}

# Nested Print
print(student["subjects"]["math"])

# Methods Of Dictionaries
# 1) Keys

print(user.keys())  # Return All The Keys Of Current Dictionary
# Output dict_keys(['name', 'age', 'isAlive', 'subjects'])

# If i want in normal list or tuple so i will write print(list(user.keys()));

# 2) values return all the values in it
print(student.values())

# 3) items() return all the key values in form of tuples
print(
    student.items()
)  # dict_items([('name', 'Anusha'), ('age', 21), ('subjects', {'math': 0, 'phy': 0, 'chem': 0}), ('total_score', 0)])

# 4) get return the value (This method is prefered for getting values instead of ["keys"])
print(student.get("name"))  # Anusha

# 5) update add the new pair in the dictionary
student.update({"city": "Karachi"})
print(student.get("city")) # Karachi 
