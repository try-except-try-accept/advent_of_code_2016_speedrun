from re import search, findall
from collections import Counter
from random import shuffle


LAZILY = "\[.+?\]" # match anything between [ and ]

DAY = 7
DELIM1 = "---"
TESTS = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn///2"""

DEBUG = False


DICTIONARY = None

LOAD_DICTIONARY = True
if LOAD_DICTIONARY:

    with open("dictionary.txt") as f:
        DICTIONARY = [line.strip() for line in f.readlines()]

        

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def is_abba(chunk):
    if len(chunk) != 4:
        return False
    
    abba = False
    try:
        abba = chunk[0] != chunk[1] and chunk[:2] == "".join(reversed(chunk[2:]))
        bugprint("Testing", chunk)
    except:
        return False
    bugprint(abba)
    buginput()
    return abba
    

def solve(data):
    count = 0
    for ip in data.split("\n"):
        if not ip.strip():    continue
        
        hypernets = findall(LAZILY, ip)
        invalid = False

        bugprint("Testing ip", ip)

        for hypernet in hypernets:
            bugprint("Hyper net is", hypernet)

            for i in range(0, len(hypernet[1:-1])):
                if is_abba(hypernet[1:-1][i:i+4]):
                    bugprint("Invalid")
                    invalid = True

                if invalid:
                    break
                
            if invalid:
                break

        if invalid:
            continue
        
        abba = False
        for chunk in ip.split(hypernet):
            

            for i in range(0, len(chunk)):

                

                if is_abba(chunk[i:i+4]):
                    
                    abba = True
                    break

            if abba:
                break

        if abba:
            count += 1
            bugprint("Valid")
        else:
            bugprint("Invalid")
        buginput()
        
        
            

        

    return count

def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(str(item), end=" ")
        print(end)

def buginput(s=""):
    if DEBUG:
        print(s)
        input()
    

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
