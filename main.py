"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomáš Ferko
email: t.ferry@seznam.cz
"""
import random
print(
    "Hi there!",
    "-" * 46,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game. You have 15 attempts.",
    "-" * 46,
    sep = "\n"
    )

def kontrola(cislo):
    if not cislo.isdigit():
        print("Only digit is allowed!")
        return False
    elif cislo.startswith("0"):
        print("Do not start with zero!")
        return False
    elif len(cislo) != 4:
        print("Use 4 digits!")
        return False
    elif len(set(str(cislo))) != 4:
        print("Use 4 unique digits!")
        return False
    return True

def bulls_and_cows(random_cislo, cislo):
    bulls = 0
    cows = 0

    for index in range(4):
        if cislo[index] == random_cislo[index]:
            bulls += 1
        
    for index in range(4):
        if cislo[index] != random_cislo[index] and cislo[index] in random_cislo:
            cows += 1
    return bulls, cows

def plural_or_not(bulls, cows):
    if bulls == 1 and cows == 1:
        print(f"Bull: {bulls}, Cow: {cows}")
    elif bulls == 1:
        print(f"Bull: {bulls}, Cows: {cows}")
    elif cows == 1:
        print(f"Bulls: {bulls}, Cow: {cows}")
    else:
        print(f"Bulls: {bulls}, Cows: {cows}")


while True:
    random_cislo = random.randint(1000,9999)
    if len(set(str(random_cislo))) == 4:
        break
pokusy = 0

while pokusy < 15:
    pokusy +=1
    print("Attempt nr.: ", pokusy)
    cislo = input("Enter a 4 digit number: ")
    if not kontrola(cislo):
        continue
    print("-" * 46)
    print(">>>", cislo)
    bulls, cows = bulls_and_cows(str(random_cislo), cislo)
    plural_or_not(bulls, cows)
    print("-" * 46)

    if bulls == 4:
        print(f"Correct, you've guessed the number {random_cislo} in {pokusy} guesses!")
        break

print(f"You have not guessed the number {random_cislo} in 15 attempts. You lose!")
print("-" * 46)

    
    
   


        




