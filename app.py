import random
import string

letters = string.ascii_letters #alphabet including capitalized letters
digits = string.digits #0 to 9
special_characters = "!@#$%^&*()_+-=[]{}|;:\"'<>,.?/" #backward slash let's double quotation marks be a string
length = int(input("How many characters do you want the password to have? "))

random_string = ''.join(random.choice(letters + digits + special_characters) for _ in range(length))
#''.join -- compiles the result into a string
#for _ in range(12) -- generates a sequence of 'length' number of random characters by calling the choice() function inside a for loop. The loop runs 'length' many times.


print(random_string)
