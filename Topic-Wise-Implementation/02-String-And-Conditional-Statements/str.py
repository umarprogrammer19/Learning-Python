str1 = "Hello"
str2 = "World"

# Concatenation
print(str1 + str2)  # HelloWorld
print(str1 + " " + str2)  # Hello World

# For Line Break
print("We Are Learning Python.\nPython is a best programming language.")

# For Finding Length Of A String
print("The Length Of A str1 is:", len(str1))

# For indexes 
print(str1[0]) # H 
print(str1[-1]) # o Because -1 prints the index of the str  

# str1[0] = "N" # This is not allowed in python

# If I Need The Some Part Of Strings
str3 = "This is string number 3"
print(str3[5:14]) # prints (is string) 
print(str3[:14]) # prints string from index 0 to 14 (This is string)
print(str3[5:]) # prints string from index 5 to last (is string number 3)
print(str3[-8:-1]) # prints string from index -8 to -1 (number)
 