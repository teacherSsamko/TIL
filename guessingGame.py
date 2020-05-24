import time
import turtle as t
import random


n = random.randint(1,30)

while True:
    x = int(input("Guess number"))
    if x == n:
        print("correct")
        break

    if x > n:
        print("guess low")

    if x < n:
        print("guess high")
    
