# endswith checks if the string ends with a given value it return true otherwise false
str = "I am a programmer."
print(str.endswith("programmer.")) # True
print(str.endswith("coder.")) # False

# capitalize it capitals the first chatracter of string
str2 = "umar"
print(str2.capitalize()) # Umar

# replace (it replaces all the given value)
str3 = "I have a old mobile and old laptop"
print(str3.replace("old","new")) # I have a new mobile and new laptop

# find it returns the first index of a given word or char etc
print(str3.find("old")) # prints 9
# If the word or letter not in the current string this will returns -1
print(str3.find("coder")) # prints -1

# count this will count the number of words letters given in the string
print(str3.count("old")) # prints 2