import random

print("        Welcome to the Number Guessing Game! \nYou got 5 attempts to guess the number between 50 and 100 \nLet's start the game!")


number_to_guess = random.randrange(50 , 100)

chances = 5

number_of_guesses = 0

while number_of_guesses < chances:
    number_of_guesses += 1
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print(f"Congratulations!! The number is {number_to_guess} \nYou guessed the right number in {number_of_guesses} attempts")
            #  "f" is used as back ticks in python
        break
    elif number_of_guesses == chances:
        print(f"Sorry! The number is {number_to_guess} Better luck next time!")
    elif guess < number_to_guess:
        print("Your guess is too low! Try again..")
    elif guess > number_to_guess:
        print("Your guess is too high! Try again..")
