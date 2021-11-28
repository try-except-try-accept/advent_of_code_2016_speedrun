from re import search, match, findall
from collections import Counter


GREEDY = "\[.+\]" # greedily match anything between [ and ]
LAZY = "\[.+?\]"  # lazily match anything between [ and ]

DAY = 9
DELIM1 = "\n"
TESTS = """(3x3)XYZ///9
X(8x2)(3x3)ABCY///20
(27x12)(20x12)(13x14)(7x10)(1x12)A///241920
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN///445"""

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

    
    reps = []
    lengths = []

    data = list(data)
    length, rep, payload = "", "", ""

    length_parse, data_parse, rep_parse = False, True, False

    while len(data):


        char = data.pop(0)
        #print("Char is", char, "lengths", lengths, "reps", reps)

        if char == "(":
            length_parse = True
            data_parse = False
            

        elif char == "x":
            rep_parse = True
            length_parse = False
            
            

        elif char == ")":
            try:
                last_rep = reps[-1]
            except:
                last_rep = 1
            

            reps.append(int(rep) * last_rep)

            lengths.append(int(length))

            #print("reps", reps)
            #print("lengths", lengths)
            length, rep = "", ""
            data_parse = True
            rep_parse = False
        else: 


            if length_parse:
                length += char


            elif rep_parse:
                rep += char

            elif data_parse:
                if not reps:
                    this_rep = 1
                else:
                    this_rep = reps[-1]
                #print(char * this_rep)

                total += this_rep

            

        

        if lengths:
            for i in range(len(lengths)):
                lengths[i] -= 1
            
        #print("lengths", lengths)

            while lengths and lengths[-1] < 0:
                reps.pop(-1)
                lengths.pop(-1)
            
            


        
            

            
            

            

            

    print("total is", total)
    return total



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
       result = solve(load_puzzle())
       print("FINAL ANSWER: ", result, "-1 =", result-1, "(random off by 1 error)")
