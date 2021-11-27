from re import search
from collections import Counter
from random import shuffle


BETWEEN = "\[.+\]" # match anything between [ and ]

DAY = 6
DELIM1 = "---"

TESTS = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar///easter"""

DEBUG = True


DICTIONARY = None

LOAD_DICTIONARY = True
if LOAD_DICTIONARY:

    with open("dictionary.txt") as f:
        DICTIONARY = [line.strip() for line in f.readlines()]

        

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

    data = data.split("\n")
    cols = len(data[0])
    words = [Counter() for i in range(cols)]
    for row in data:
        if not row.strip(): continue
        for i in range(cols):

            words[i][row[i]] += 1

    out = ""
    for w in words:
        out += w.most_common()[0][0]
    print(words)
    return out

def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(s, end="")
        print(end)

def check():

    success = True

    for row in TESTS.split(DELIM1):
        if not len(row):    continue

        data, expected = row.split("///")
        print(data, "should get", expected)
        
        outcome = solve(data)
        if str(outcome).strip() == expected.strip():
            print("Test passed")
        else:
            print("Test failed")
            success = False
            print(outcome)

    return success


if __name__ == "__main__":

    if check():
        print("FINAL ANSWER: ", solve(load_puzzle()))
