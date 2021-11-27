DAY = 2

TESTS = """ULL
RRDDD
LURDL
UUUUD///1985"""

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

    keys = [ [1,2,3], [4,5,6], [7,8,9]]

    x, y = 1, 1    
    code = ""
    for row in data.split("\n"):
        if not row.strip():    continue
        


        for move in row:
            
            
            if move == "U":
                if y > 0:
                    y -= 1
            elif move == "D":
                if y < 2:
                    y += 1
            elif move == "R":
                if x < 2:
                    x += 1
            elif move == "L":
                if x > 0:
                    x -= 1

            #print(x, y)
            

        code += str(keys[y][x])
        print(code)
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
