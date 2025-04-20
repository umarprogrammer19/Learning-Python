# you are given a list of subjects. Assume one classroom in required for one subject how many classrooms are needed by all students
# "python", "java","C++","python","javascript","java","python","java","C++","C"

subjects = {
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C",
}

print(f"{len(subjects)} classrooms are needed by all students")

# figure out a way to store 9 and 9.0 as seperate values in the set, you can take help of built in data types of python

values = {9, 9.0}
print(values) # {9}
values = {9, "9.0"}
print(values)
values = {("int", 9), ("float", 9.0)}
print(values)
