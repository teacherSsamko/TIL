import random
import time


word = ["apple", "banana", "cherry", "cat", "dog", "fox"]
n = 1
print("Enter to start")
input()
start = time.time()

q = random.choice(word)

while n <= 5:
    print("*Question", n)
    print(q)
    x = input()
    if q == x:
        print("correct")

        n = n + 1
        q = random.choice(word)
    else:
        print("retry")

end = time.time()
et = end - start
et = format(et, ".2f")
print("type time:", et, "sec")

