import random
import string

letters = string.ascii_letters
digits = string.digits
special_characters = "!@#$%^&*()_+-=[]{}|;:\"'<>,.?/"

random_string = ''.join(random.choice(letters + digits + special_characters) for _ in range(12))
print(random_string)
