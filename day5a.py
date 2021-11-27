from re import search
from collections import Counter
from random import shuffle
from hashlib import md5


BETWEEN = "\[.+\]" # match anything between [ and ]

DAY = 5
DELIM1 = "\n"
TESTS = """abc///18f47a30"""

DEBUG = True


DICTIONARY = None

LOAD_DICTIONARY = True
if LOAD_DICTIONARY:

    with open("dictionary.txt") as f:
        DICTIONARY = [line.strip() for line in f.readlines()]

        

def load_puzzle():
    
    return "reyedfim"

def solve(data):

    password = ""

    
    i = 0
    while len(password) < 8:
        index = data+str(i)
        hashed = md5(index.encode("utf-8")).hexdigest()
        i += 1
        if hashed.startswith("00000"):
            password += hashed[5]
            print(password)
            

            
        
    

    return password

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
