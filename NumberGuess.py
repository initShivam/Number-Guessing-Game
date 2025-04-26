print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
attempts = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    attempts = 10
    print("You have " + str(attempts) + " attempts remaining to guess the number.")
elif level == "hard":
    print("You have " + str(attempts) + " attempts remaining to guess the number.")
    attempts = 5
else:
    print("Invalid input. Please choose 'easy' or 'hard'.")
import random
random_number = random.randint(1, 100)
Guess = int(input("Make a guess: "))
while attempts > 0:
    if Guess < random_number:
        print("Too low.")
        attempts -= 1
        print("You have " + str(attempts) + " attempts remaining to guess the number.")
        Guess = int(input("Make a guess: "))
    elif Guess > random_number:
        print("Too high.")
        attempts -= 1
        print("You have " + str(attempts) + " attempts remaining to guess the number.")
        Guess = int(input("Make a guess: "))
    elif Guess == random_number:
        print("You got it! The answer was " + str(random_number) + ".")
        break
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print("The number was " + str(random_number) + ".")
        break 