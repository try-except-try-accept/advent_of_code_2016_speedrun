DAY = 3
DELIM1 = "\n"
TESTS = """5 10 25///0
17 13 29///1"""

DEBUG = False

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

    count = 0

    for row in data.split("\n"):
        if not row.strip(): continue
        bugprint(row)
        sides = list(map(int, [s for s in row.split(" ") if s.strip()]))

        biggest = max(sides)

        sides.remove(biggest)

        if sum(sides) > biggest:
            count += 1

    return count

def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(s, end="")
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
        print("FINAL ANSWER: ", solve(load_puzzle()))
