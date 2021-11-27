from re import search, match, findall
from collections import Counter


GREEDY = "\[.+\]" # greedily match anything between [ and ]
LAZY = "\[.+?\]"  # lazily match anything between [ and ]

DAY = 9
DELIM1 = "\n"
TESTS = """ADVENT///6
A(1x5)BC///7
(3x3)XYZ///9
A(2x2)BCD(2x2)EFG///11
(6x1)(1x3)A///6
X(8x2)(3x3)ABCY///18
aslkdj(2x2)oijoij(3x5)fsdfs(2x1)(2x1)///36
"""

DEBUG = False

def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(str(item), end=" ")
        print(end)


def buginput(s=""):
    if DEBUG:
        print(s)
        input()


def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

   #print("DATA IS", data)

    total = 0

    row = data.replace("\n", "")
        

    markers = findall("\(.+?\)", row)



    while len(markers):
        

        m = markers.pop(0)
        bugprint("Processing marker", m)
        compressed_data = row.index(m) + len(m)

        get, reps = map(int, m[1:-1].split("x"))
        
        start = row.index(m) + len(m)
        end = start + get
        compressed_data = row[start:end]

        remove_fake_markers = compressed_data

        fake_markers = findall("\(.+?\)|\(.+", remove_fake_markers)
        #print("Fake markers is", fake_markers)

        for fake_marker in fake_markers:
            
            markers.pop(0)
            
        

        
            
            
        decompressed = compressed_data * reps
        bugprint("decompressed is", decompressed)

        
        
        row = row.replace(m + compressed_data, decompressed, 1)
        bugprint(row)
        #input()

    
        
    return len(row.strip())


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
