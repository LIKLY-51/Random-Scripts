import random

f = open("char.txt", "a", encoding="utf-8")

for i in range(140000):
    try:
        if (chr(i) == "🊭"):
            continue
        f.write(chr(i) + "\n")
    except UnicodeEncodeError:
        print("oof")
        continue

f.close()