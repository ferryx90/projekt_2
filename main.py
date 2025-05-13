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


def generate_random_num() -> int:
    """
    Generates a random 4-digit number with unique digits.
    Ensures that:
        - the number does not begin with 0,
        - all digits are unique.
    Returns:
        int: A 4-digit integer with non-repeating digits and a non-zero first digit.
    """
    number_one = random.sample(range(10), 5)
    random_number = number_one[0:4]
    if number_one[0] == 0:
        random_number = number_one[1:5]
    return int("".join(map(str, random_number)))
          

def check_number(number : str) -> bool:
    """Checks if the number is correct to play bulls and cows game.
    Paremeter:
        (str) The user's 4-digit guess with unique digits.
    Returns:
         True or False """
    if not number.isdigit():
        # Checks if there are only numbers.
        print("Only digit is allowed!")
        return False
    elif number.startswith("0"):
        # Checks if number does not start with zero.
        print("Do not start with zero!")
        return False
    elif len(number) != 4:
        # Checks if player uses exactly 4 numbers.
        print("Use 4 digits!")
        return False
    elif len(set(str(number))) != 4:
        # Checks if there are not duplicates.
        print("Use 4 unique digits!")
        return False
    return True

def bulls_and_cows(random_number : str, number: str) -> tuple[int, int]:
    """
    Compares two 4-digit numbers and returns the count of bulls and cows.
    A "bull" is a digit that is correct in value and position.
    A "cow" is a digit that is correct in value but in the wrong position.
    Parameters:
        random_number (str): The secret 4-digit number with unique digits.
        number (str): The user's 4-digit guess with unique digits.
    Returns:
        tuple[int, int]: A tuple containing the number of bulls and cows.
    """
    bulls = 0
    cows = 0

    for index in range(4):
        if number[index] == random_number[index]:
            bulls += 1
        elif number[index] != random_number[index] and number[index] in random_number:
            cows += 1
    return bulls, cows

def plural_or_not(bulls : int, cows: int) -> None:
    """
    Prints the number of bulls and cows using correct singular or plural form.
    Parameters:
        bulls (int): The number of bulls (correct digits in the correct position).
        cows (int): The number of cows (correct digits in the wrong position).
    Returns:
        None
    """
    if bulls == 1 and cows == 1:
        print(f"Bull: {bulls}, Cow: {cows}")
    elif bulls == 1:
        print(f"Bull: {bulls}, Cows: {cows}")
    elif cows == 1:
        print(f"Bulls: {bulls}, Cow: {cows}")
    else:
        print(f"Bulls: {bulls}, Cows: {cows}")

def play_game(random_number: str) -> None:
    """
    Runs the game loop for a single round of the Bulls and Cows game.
    The player has up to 15 attempts to guess a 4-digit number with unique digits.
    For each guess, the number of "bulls" (correct digit in the correct position)
    and "cows" (correct digit in the wrong position) is counted and displayed.
    Parameters:
        random_number (str): The randomly generated 4-digit number with unique digit.
    Returns:
        None
    """
    attempts = 0
    while attempts < 15:
        attempts +=1
        print("Attempt nr.: ", attempts)
        number = input("Enter a 4 digit number: ")
        if not check_number(number):
            # If the guess is not correctly written down it is not counted like a lost guess.
            attempts -= 1
            continue
        print("-" * 46)
        print(">>>", number)
        bulls, cows = bulls_and_cows(str(random_number), number)
        plural_or_not(bulls, cows)
        print("-" * 46)

        if bulls == 4:
            print(f"Correct, you've guessed the number {random_number} in {attempts} guesses!")
            return

    print(f"You have not guessed the number {random_number} in 15 attempts. You lose!")

if __name__ == "__main__":
    random_number = generate_random_num()
    play_game(random_number)   
    print("-" * 46)



    
