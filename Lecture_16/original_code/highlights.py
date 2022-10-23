# highlights from lecture #16

#import random
from random import randint

target = randint(1,100)

while True:
    guess = int(input("Enter a guess: "))
    if guess < 1 or guess > 100:
        print("Between 1 and 100 please!")
    elif guess > target:
        print("Too high!")
    elif guess < target:
        print("Too low!")
    elif guess == target:
        print("you guessed the number!")
        break