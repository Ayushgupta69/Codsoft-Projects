import random
import string

#lenght of password 
length = int(input("How many characters do you want in your password? "))

#different characters
characters = string.ascii_letters + string.digits + string.punctuation

#password by picking random characters
password = ''.join(random.choice(characters) for _ in range(length))
print("Your new password is:", password)
