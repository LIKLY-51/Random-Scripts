string = ""

for i in range(100):
    for i2 in range(798):
        string = string + "|"

f = open("book.txt", "w", encoding="utf-8")
f.write(string)
f.close()