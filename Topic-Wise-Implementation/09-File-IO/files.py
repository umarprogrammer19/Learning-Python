# File IO (I/O => Input And Output)
import os
# r => read
file = open("demo.txt", "r")
data = file.read()
print(data)  # prints the file data
file.close()

# a append add new text in the file
file = open("demo.txt", "a+")
file.write("\nThis is a new Text From The Code File")
print(file.read(), end="")
file.close()

# w add new text in the file overwrite the previous
file = open("write.txt", "w+")
file.write("\nThis is a new Text From The Code File")
print(file.read(), end="")
file.close()

with open("write.txt", "r") as f:
    data = f.read()
    print(data, end="")

os.remove("demo.txt")