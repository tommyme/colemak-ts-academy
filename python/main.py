from rich import print as rprint
from readchar import readchar
import time

import os
from wordlist import masterList
import random

clear = lambda: os.system("clear")
# clear = lambda: sys.stdout.flush()
you5input = ""
words = random.choices(masterList, k=20)
times = 0
correct, total = 0, 0
st = None
clear()
correct_words = []

words2show = 5
while words:
    red = False
    current_word = words[0]
    rprint(f"{correct}/{total}")
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

    words_prompt += " "
    words_prompt += " ".join(words[1:5])
    prompt_line = [">", words_prompt, "...", times, "green", green_end_idx]
    input_line = ["\n:", you5input]

    rprint(*prompt_line, *input_line, end='')
    times += 1
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
    clear()

time_used = time.time() - st
print("time used:", time_used)
rprint(f"{correct}/{total}")
wpm = len(" ".join(correct_words)) / 5 / (time_used / 60)
print("wpm:", wpm)
print("exit")


