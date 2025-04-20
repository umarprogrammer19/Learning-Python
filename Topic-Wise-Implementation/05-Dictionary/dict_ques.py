# store the following meanings in the dictionary
# table: "a peice of furniture", "list of fact & figures"
# cat: "a small animal"

meanings = (
    {
        "table": ["a perice of a furnitue", "list of fact & figure"],
        "cat": "a small animal",
    },
)

print(meanings)

# WAP to enter the marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one, Use Subjects name as keys & marks as value

marks_dict = {}
marks_dict.update({"maths": int(input("Please Enter Your Maths Number: ").strip())})
marks_dict.update({"physics": int(input("Please Enter Your Physics Number: ").strip())})
marks_dict.update({"chemistry": int(input("Please Enter Your Chemisty Number: ").strip())})
print(marks_dict)