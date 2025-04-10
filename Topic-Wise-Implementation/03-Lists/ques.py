# WAP to ask the user enter names to their 3 favorite movies & store them in a list

list = []
# movies = input("Enter your 3 favorite movie names seperated ,: ").strip().split(",")
# list.append(movies)
print(list)

# WAP to check if a list contains a palindrome of the elements. (Hint Use copy() method)

list = [1, 2, 3]
copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("The List is Palindromic")
else:
    print("The List is Non Palindromic")