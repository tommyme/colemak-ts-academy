from rich import print as rprint
from readchar import readchar
import time
import sys
import os
from wordlist import masterList
import random

def gen_symbol_words():
    num = 30
    core = ';\'":,./\\-=_+()'
    return gen_xx_words(6, num, core)

def gen_xx_words(wlen, num, ch_set):
    return [''.join(random.choices(ch_set, k=wlen)) for _ in range(num)]
    
def gen_number_words():
    num = 30
    core = '0123456789'
    return gen_xx_words(6, num, core)

clear = lambda: os.system("clear")
# clear = lambda: sys.stdout.flush()
you5input = ""
if len(sys.argv) > 1:
    option = sys.argv[1]
    if option == 'sym':
        symbols = []
        words = gen_symbol_words()
    elif option == 'num':
        words = gen_number_words()
else:
    words = random.choices(masterList, k=30)
times = 0
correct, total = 0, 0
st = None
clear()
correct_words = []

words2show = 5
while words:
    # color the word
    red = False
    current_word = words[0]
    style_end_idx = min(len(you5input), len(current_word))
    green_end_idx = style_end_idx
    for i in range(style_end_idx):
        if you5input[i] != current_word[i]:
            green_end_idx = i
            red = True
            break

    words_prompt = f"[bold green]{current_word[:green_end_idx]}[/bold green]"
    if red:
        words_prompt += f"[bold red]{current_word[green_end_idx:]}[/bold red]"
    else:
        words_prompt += f"{current_word[green_end_idx:]}"

    # concat the first colored word with other words
    words_prompt += " "
    words_prompt += " ".join(words[1:5])
    prompt_line = [
        f"{correct}/{total}",
        # ":",
        # you5input,
        ">",
        words_prompt,
        "...",
        times,
        "green",
        green_end_idx,
    ]

    rprint(*prompt_line, end="\r")
    times += 1

    # change you5input according to read char
    ch = readchar()
    if not st:
        st = time.time()
    if ch == " " or ch == "\r":
        total += 1
        wd = words.pop(0)
        if you5input == wd:
            correct += 1
            correct_words.append(wd)
        you5input = ""
    elif ch == "\x7f":
        you5input = you5input[:-1]
    elif ch == "\x1b":
        break
    else:
        you5input += ch

time_used = time.time() - st
print("time used:", time_used)
rprint(f"{correct}/{total}")
wpm = len(" ".join(correct_words)) / 5 / (time_used / 60)
print("wpm:", wpm)
print("exit")
