import click
from rich import print as rprint
from readchar import readchar
import time
import sys
import os
from wordlist import masterList
import random

def color_red(s):
    return f"[bold red]{s}[/bold red]"

def color_green(s):
    return f"[bold green]{s}[/bold green]"

def UpCaseWord(word, n):

    if len(word) > n:
        idxs = random.choices(range(len(word)), k=n)
        word: list[str] = list(word)
        for i in idxs: word[i] = word[i].upper()
        return "".join(word)
    else:
        return word

@click.command()
@click.option('-m', '--mode', 'mode', default='word')
@click.option('-l', '--length', 'wordLength', default=6, type=str)
@click.option('-n', '--number', 'numOfWords', default=30, type=int)
def gen_words(mode, wordLength, numOfWords):
    print(mode, wordLength, numOfWords)
    if mode == 'word':
        words = random.choices(masterList, k=numOfWords)
    elif mode == 'upcaseword':
        # word中随机找两个字母变大写
        words = [
            UpCaseWord(i, 2)
            for i in
            random.choices(masterList, k=numOfWords)
            ]
    else:
        if mode == 'leftsym':
            core = ';\'":,./\\-=_+()'
        elif mode == 'num':
            core = '1234567890'
        elif mode == 'upsym':
            core = "!@#$%^&*"
        else:
            raise Exception("no such mode")
        words = gen_xx_words(wordLength, numOfWords, core) 
    run(words)



def gen_xx_words(wlen, num, ch_set):
    return [''.join(random.choices(ch_set, k=wlen)) for _ in range(num)]
    
def gen_number_words():
    num = 30
    core = '0123456789'
    return gen_xx_words(6, num, core)

def gen_sp_1():
    """
    exercise for special symbols of "()_+-="
    """
    num = 30
    core = "()-=_+"
    return gen_xx_words(6, num, core)
clear = lambda: os.system("clear")
# clear = lambda: sys.stdout.flush()


def run(words):
    you5input = ""
    KeypressTimes = 0
    correct, total = 0, 0
    st = None
    clear()
    correct_words = []

    words2show = 5
    while words:
        # color the word
        wrong = False
        current_word = words[0]
        style_end_idx = min(len(you5input), len(current_word))
        green_end_idx = style_end_idx
        for i in range(style_end_idx):
            # 找到第一个错误的pos pos之前是绿的 
            if you5input[i] != current_word[i]:
                green_end_idx = i
                wrong = True
                break

        words_prompt = color_green(current_word[:green_end_idx])
        if wrong:
            # 把当前word其余部分标红
            words_prompt += color_red(current_word[green_end_idx:])
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
            KeypressTimes,
            "green",
            green_end_idx,
            you5input
        ]

        rprint(*prompt_line, end="\r")
        KeypressTimes += 1

        # change you5input according to read char
        ch = readchar()
        if not st:
            st = time.time()
        if ch in ['\r', '\n', ' ']:
            total += 1
            wd = words.pop(0)
            if you5input == wd:
                correct += 1
                correct_words.append(wd)
            you5input = ""
        elif ch == "\x7f": # backspace
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


if __name__ == "__main__":
    gen_words()
