DAY = 1

TESTS = """
"""

with open(f"day{DAY}.txt") as f:

    data = f.readlines()

def solve(data):

    pass

def check():

    success = True

    for row in TESTS.split("\n"):

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
        print("FINAL ANSWER: ", solve(data))