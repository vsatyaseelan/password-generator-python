#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
password = ""
for char in range(1, nr_letters + 1):
  # random_char = random.choice(letters)
  # password += random_char
  password += random.choice(letters)

for int in range(1, nr_numbers + 1):
  # random_int = random.choice(numbers)
  # password += random_int
  password += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
  # random_sym = random.choice(symbols)
  # password += random_sym
  password += random.choice(symbols)  
print(f"Your simple password is: {password}")


# Complex Level
password_list = []
for char in range(1, nr_letters + 1):
  # random_char = random.choice(letters)
  # password += random_char
  password_list.append(random.choice(letters))

for int in range(1, nr_numbers + 1):
  # random_int = random.choice(numbers)
  # password += random_int
  password_list.append(random.choice(numbers))

for sym in range(1, nr_symbols + 1):
  # random_sym = random.choice(symbols)
  # password += random_sym
  password_list.append(random.choice(symbols))
random.shuffle(password_list)

complex_password = ""
for char in password_list:
  complex_password += char
print(f"Your complex password is: {complex_password}")
