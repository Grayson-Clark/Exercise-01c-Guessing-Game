#!/usr/bin/env python3
import sys, random, time
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

number = random.randrange(1,11)
guess = input("Guess a number from 1 to 10: ")
while guess != number:
    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Great job! You got it!")
            break
        elif guess > number:
            print("Your guess was higher than the number")
        elif guess < number:
            print("Your guess was lower than the number")
    else:
        print("Make sure your guess is a number!")
    guess = input("Guess a number from 1 to 10: ")


time.sleep(3)