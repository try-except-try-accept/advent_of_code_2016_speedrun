DAY = 4
DELIM1 = "\n"
TESTS = """aaaaa-bbb-z-y-x-123[abxyz]///123
a-b-c-d-e-f-g-h-987[abcde]///987
not-a-real-room-404[oarel]///404
totally-real-room-200[decoy]///0"""

DEBUG = False

from re import search
from collections import Counter
from random import shuffle


def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):
    
    checksum = search("\[.+\]", data).group()
    sector_id = search("\d+", data).group()

    payload = data.replace(checksum, "").replace(sector_id, "").replace("-", "")
    checksum = list(checksum[1:-1])

    counts = Counter(payload)

    count_to_item = {}

    for occurrences in counts.values():
        
        for item in counts:

            if counts[item] == occurrences:

                try:
                    if item not in count_to_item[occurrences]:
                        count_to_item[occurrences].append(item)
                except:
                    count_to_item[occurrences] = [item]
                    
            
    bugprint(count_to_item)
    for occ in sorted(count_to_item.keys(), reverse=True):

        items = list(count_to_item[occ])

        count = 0 # dodgy
        while len(items):
            
            for item in items:
                bugprint("Checking", item)
                if item == checksum[0]:
                    bugprint(checksum)
                    checksum.pop(0)
                    items.remove(item)
                    
                    

                    if not len(checksum):
                        return int(sector_id)


                    
            count += 1

            if count > 500:
                return 0
            

    



def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(str(item), end="")
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
        tot = 0
        for room in load_puzzle().split("\n"):
            if room.strip():
                tot += solve(room)
        print("FINAL ANSWER", tot)
