import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'J', 'k', 'l', 'm', 'n', 'o',

           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'x', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S',

           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(',')','*','+']
print("Welcome To Password Generator !!!")
n_letters = int(input("How many letter you want to create your password ?\n"))
n_symbols = int(input("How many symbol you want to create your password ?\n"))
n_numbers = int(input("How many number you want to create your password ?\n"))
password = " "
for i in range(1,n_letters+1):
  char = random.choice(letters)
password += char
for i in range(1,n_symbols+1):
   char = random.choice(symbols)
password += char
for i in range(1,n_numbers+1):
   char = random.choice(numbers)
password += char
print(password)
