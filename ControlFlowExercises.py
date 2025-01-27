print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in x:
    if i % 2 == 0:
        print(i)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for i in x[:5]:
    if i % 2 != 0:
        print(i)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
another_list_letters = []
for i in names:
    another_list_letters.append(i[0])

print(another_list_letters)


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
another_list_indices = []
for i in names:
    another_list_indices.append(i.index(' '))
print(another_list_indices)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
first_last = []
for i in names:
    f = i[0]
    l = i[i.index(' ')+1]
    initial = f + l
    first_last.append(initial)
print(first_last)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

for i in list_of_lists:
    if (len(set(i)) == len(i)):
        print(i)

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
def find_divisors (user_input):
    list_of_divisors = []
    for i in range(1, user_input+1):
        if user_input % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

while True:
    try:
        user_number = int(input("Enter a number greater than 100: "))
    except ValueError:
        print("This is not right. Try again.\n")
        continue
    if (user_number <= 100):
        print("This is not right. Try again.\n")
        continue
    elif (len(find_divisors(user_number)) <= 2):
        print("Prime.")
        break
    else:
        print("Not prime")
        break


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b: Added a function above.





