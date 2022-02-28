# CONFIG
limit = 14 # set to how ever long you want the password to be
save = True # save to file
show = False # print to screen
# which arrays to use
use_symbol = True
use_letters = True
use_uppercase = True
use_numbers = True
use_other = True
# END OF CONFIG

import random
from datetime import date,datetime

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '>', '>']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8,', '9', '0']
other = [ ';', ':', "'", '"', ',', '<', '.', '/', '?', '`', '~', '|', '\\']
password = ''
character_array = []

if use_symbol:
    for i in symbol:
        character_array.append(i)
if use_letters:
    for i in letters:
        character_array.append(i)
if use_uppercase:
    for i in upper:
        character_array.append(i)
if use_numbers:
    for i in numbers:
        character_array.append(i)
if use_other:
    for i in other:
        character_array.append(i)
random.shuffle(character_array)

for i in range(1, limit + 1):
    password += character_array[random.randint(1, len(character_array)) - 1]
print('Generated password')

if save:
    print('Writing')
    today = date.today()
    now = datetime.now()
    f = open('passwordgen.txt', 'a').write(today.strftime("%B %d, %Y") + ', ' + now.strftime("%H:%M:%S") + ': ' + password + '\n')

if show:
    print('Password: ' + password)

print('done')