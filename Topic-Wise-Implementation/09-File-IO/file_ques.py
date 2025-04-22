# Create a new file "practice.txt" using python and add the following data init
# Hi Everyone
# we are learning file I/O
# using Java
# i Like programming in java

with open("practice.txt", "w") as f:
    f.write("Hi Everyone\n")
    f.write("we are learning file I/O\n")
    f.write("using Java\n")
    f.write("i Like programming in Java\n")
    f.close()

# Replace All The java with python
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_data)

# Search the word learning exist or not in the file practice
with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print(True)
    else:
        print(False)

# WAF to find in which line of the file does the word "learning" occur first,
# Print -1 if not found
with open("practice.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        if data[i].find("learning") != -1:
            print(i + 1)
            break
        else:
            print(-1)

with open("nums.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    sum = 0
    for num in nums:
        if int(num) % 2 == 0:
            sum += int(num)
    print(sum)
