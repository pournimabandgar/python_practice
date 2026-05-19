#Number Guessing Game
import random
print("Number Guessing Game")
secret_number = random.randint(1,100)
attempts =10
print("I'm thinking of a number between 1 and 100")
print("You have 10 attempts")
while attempts > 0 :
    guess=int(input(f"Attempts left {attempts} : guess the number"))
    attempts -=1
    if guess < secret_number:
        print("your guess is too low , try higher number.")
    elif guess > secret_number:
        print("guess is too high , try for lower number.")
    else:
        print("Your guess is correct")
        attempts= 0
        break