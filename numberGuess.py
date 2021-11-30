## This is a guess the number game
import random

count = 0

user = input("Hello, what\'s your name: ")

number = random.randint(1, 30)

print(f"Welcome {user.title()}, I\'m thinking of a number between 1 and 30.")
print("You have only 5 tries to guess it right")

for count in range(1, 6):
    answer = int(input("Take a guess: "))
    if answer < number:
        print(f"Your guess {answer} if too low.")
    elif answer > number:
        print(f"Your guess {answer} is too high.")
    elif answer == number:
        print(f"Great Work {user}. You guessed the number in {count} rounds.")
    else:
        print(f"The number was {number}")