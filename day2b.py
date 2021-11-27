DAY = 2

TESTS = """ULL
RRDDD
LURDL
UUUUD///5DB3"""

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

    keys = '''00100
02340
56789
0ABC0
00D00'''.split("\n")

    x, y = 0, 2
    print("start at", keys[y][x])
    code = ""
    for row in data.split("\n"):
        if not row.strip():    continue
        

        
        for move in row:
            #print(move, end= "")
    
            if move == "U":
                if y > 0 and keys[y-1][x] != '0':
                    #print("up")
                    y -= 1
            elif move == "D":
                if y < 4 and keys[y+1][x] != '0':
                    #print("Down")
                    y += 1
            elif move == "R":
                if x < 4 and keys[y][x+1] != '0':
                    #print("right")
                    x += 1
            elif move == "L":
                if x > 0 and keys[y][x-1] != '0':
                    #print("left")
                    x -= 1
          

        code += str(keys[y][x])
        #print(code)
    return code

def check():

    success = True

    for row in TESTS.split("---"):
        if not len(row):    continue

        data, expected = row.split("///")
        print(data, "should get", expected)
        
        
        outcome = solve(data)
        if str(outcome.strip()) == expected.strip():
            print("Test passed")
        else:
            print("Test failed")
            success = False
            print(outcome)

    return success


if __name__ == "__main__":

    if check():
        print("FINAL ANSWER: ", solve(load_puzzle()))
