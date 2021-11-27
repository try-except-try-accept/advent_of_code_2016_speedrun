DAY = 1

TESTS = """R8, R4, R4, R8///4"""

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):
    x = 0
    y = 0

    visited = []


    dirs = "NESW"
    data = data.split(", ")
    current = 0
    for d in data:
        if d[0] == "R":
            current = (current + 1) % 4
        elif d[0] == "L":
            current = (current - 1) % 4

        move = int(d[1:])

        direction = dirs[current]
        start_x = x
        start_y = y

        if direction == "N":
            y -= move
            start = start_y
            stop = y
            step = -1
            
        elif direction == "E":
            x += move
            start = start_x
            stop = x
            step = 1
            
            
        elif direction == "S":
            y += move
            start = start_y
            stop = y
            step = 1
            
            
            
        elif direction == "W":
            x -= move
            start= start_x
            stop = x
            step -1
            
        for new in range(start, stop, step):
            if direction in "EW":
                new_loc = (new, y)
            else:
                new_loc = (x, new)

            if new_loc in visited:
                return abs(new_loc[0]) + abs(new_loc[1])
            else:
                visited.append(new_loc)

            
            
        
        
        

def check():

    success = True

    for row in TESTS.split("\n"):
        if not len(row):    continue

        data, expected = row.split("///")
        print(data, "should get", expected)
        if expected.isdigit():
            expected = int(expected)
        outcome = solve(data)
        if outcome == expected:
            print("Test passed")
        else:
            print("Test failed")
            success = False
            print(outcome)

    return success


if __name__ == "__main__":

    if check():
        print("FINAL ANSWER: ", solve(load_puzzle()))
