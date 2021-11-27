DAY = 1

TESTS = """a,a///aa
"""

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.readlines()
    return data

def solve(data):

    pass

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
