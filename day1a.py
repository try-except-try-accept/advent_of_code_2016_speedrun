DAY = 1

TESTS = """R2, L3///5
R2, R2, R2///2
R5, L5, R5, R3///12
"""

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):
    x = 0
    y = 0


    dirs = "NESW"
    data = data.split(", ")
    current = 0
    for d in data:
        if d[0] == "R":
            current = (current + 1) % 4
        elif d[0] == "L":
            current = (current - 1) % 4

        move = int(d[1:])

        print(dirs[current])

        if dirs[current] == "N":
            y -= move
        elif dirs[current] == "E":
            x += move
        elif dirs[current] == "S":
            y += move
        elif dirs[current] == "W":
            x -= move
            

        print(x, y)

    return abs(x) + abs(y)

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
