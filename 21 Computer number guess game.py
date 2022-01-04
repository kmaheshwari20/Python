import random
import time

print("This program is for computer to guess the input number");

def computer_guess(x):
    high = x
    n=int(input("Enter your number between 1 to {}".format(x)))
    low = 1
    guess=random.randint(low,high)
    while (n != guess):
        guess = random.randint(low, high)
        if guess < n:
            low=guess
            print (f"Low {low}")
            time.sleep(3)
        elif guess > n:
            print(f"High {high}")
            high=guess
            time.sleep(3)

    print (f"Your number is {guess}")

computer_guess(20)