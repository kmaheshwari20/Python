import random
import time

def guess(x):
    print("This program is to guess the random number, generated by Computer between 1 and {}".format(x))
    num=random.randint(1,x)
    guess = 0

    while (guess != num):
            guess=int(input("Guess your number"));
            if guess > num:
                print("Guess is high")
            elif (guess < num):
                print ("Guess is less")
    print("You are correct")

guess(20)