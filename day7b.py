from re import search, findall
from collections import Counter
from random import shuffle


LAZILY = "\[.+?\]" # match anything between [ and ]

DAY = 7
DELIM1 = "---"
TESTS = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb///3"""

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

def is_abba(chunk, aba_mode=False):
    mid1 = 2
    mid2 = 2
    if aba_mode:
        mid1 = 2
        mid2 = 1
    
    if len(chunk) != 3 if aba_mode else 4:
        return False
    
    abba = False
    try:
        abba = chunk[0] != chunk[1] and chunk[:mid1] == "".join(reversed(chunk[mid2:]))
        bugprint("Testing", chunk)
    except:
        return False
    bugprint(abba)
    buginput()

    if abba:
        if aba_mode:
            return chunk[1] + chunk[0] + chunk[1]
        else:
            return True
    else:
        return False


    
    

def solve(data):
    count = 0
    for ip in data.split("\n"):
        if not ip.strip():    continue
        
        hypernets = findall(LAZILY, ip)

        supernets = []

        parse_ip = ip

        for hypernet in hypernets:

            fixed, parse_ip = parse_ip.split(hypernet)

            supernets.append(fixed)

        supernets.append(parse_ip)
        
        bugprint("Testing ip", ip)
        bugprint("supernets", supernets)
        bugprint("hypernets", hypernets)

        buginput()
        invalid = False

        aba = False

        for supernet in supernets:
            

            for i in range(0, len(supernet)):
                bab_for_aba = is_abba(supernet[i:i+3], aba_mode=True)

                
                    
                if bab_for_aba:
                    bugprint("Found aba", supernet[i:i+3])
                    bugprint("Can I find bab", bab_for_aba)
                    if bab_for_aba in "".join(hypernets):
                        bugprint("Found")
                        count += 1
                        aba = True
                        break
            if aba:
                break
                        
                    

        
                    
                    

        

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
