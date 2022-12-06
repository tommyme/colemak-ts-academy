import os
from readchar import readchar
clear = lambda : os.system('clear')
you5input = ''

clear()
while(True):
    if you5input:
        print(f'you5input: {you5input}', end='\r')
    ch = readchar()
    you5input += ch
    if ch == '\x1b':
        break
    clear()
