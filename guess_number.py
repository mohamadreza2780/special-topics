
import random

number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")
print("You have 10 attempts.")

for i in range(10):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("OK - You Win!")
        break

    elif guess < number:
        print("The number is bigger.")

    else:
        print("The number is smaller.")

else:
    print("FAIL!")
    print("The correct number was:", number)
