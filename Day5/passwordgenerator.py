import random
import string

print("welcome to the password generator.")
lenght = int(input("How long will be password?\n"))
symbols_qty = int(input("How many symbols would you like?\n"))
numbers_qty = int(input("How many numbers would you like?\n"))

all_characters = (32, 126)
numbers_ind = (48, 57)
symbols = []
numbers = []
characters = []

while len(numbers) != numbers_qty: 
    numbers.append(chr(random.randint(*numbers_ind)))
while len(symbols) != symbols_qty:  
    nm = random.randint(*all_characters)
    if (nm < numbers_ind[0]) or (nm > numbers_ind[1]):
        symbols.append(chr(nm))
while len(characters) != lenght - numbers_qty - symbols_qty: 
    characters.append(chr(random.randint(*all_characters)))
password = numbers + symbols + characters
random.shuffle(password)

print(f"Here is your password: " + "".join(password))