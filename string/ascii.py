import random

string = ""

for _ in range(10):
    string = string + chr(random.randint(1, 5000))

print(string)