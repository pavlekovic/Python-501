
print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
user_input = int(input("Enter a number: "))

def find_divisors (user_input):
    list_of_divisors = []
    for i in range(1, user_input+1):
        if user_input % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

print('f(%d) =' % (user_input), find_divisors(user_input))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
int_1 = int(input("Enter the first number: "))
int_2 = int(input("Enter the second number: "))

def is_it_factor (int_1, int_2):
    divisors_int1 = find_divisors(int_1)
    divisors_int2 = find_divisors(int_2)

    if int_1 in divisors_int2 or int_2 in divisors_int1:
        return True
    else:
        return False

print(is_it_factor(int_1, int_2))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
letter = str(input("Enter a letter: "))

def letter_position (letter):
    return (alphabet.index(letter)+1)

print(letter_position(letter))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
name = str(input("Enter a name: "))

def generate_id_number (name):
    list_of_letters = list(name)
    id_number = []
    joined_letters = ''
    for i in range(len(list_of_letters)):
        id_number.append(letter_position(list_of_letters[i]))
    for j in id_number:
        joined_letters += str(j)
    return joined_letters

print(generate_id_number(name))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def generate_password(id):
    list_of_digits = list(id)
    sum_digits = 0
    for i in list_of_digits:
        sum_digits += int(i)
    return (int(id) - sum_digits)

print('This is your password:', generate_password(generate_id_number(name)))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def check_input(message):
    while True:
        try:
            user_input_q3 = int(input(message))
        except ValueError:
            print("User input is not an integer. Try again.\n")
            continue
        else:
            return user_input_q3
            break

def is_prime():
    if len(find_divisors(user_input_q3)) > 2:
        return True
    else:
        return False

user_input_q3 = check_input("Enter a number: ")

print(is_prime())

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
#check the check_input function above
# -------------------------------------------------------------------------------------- #






