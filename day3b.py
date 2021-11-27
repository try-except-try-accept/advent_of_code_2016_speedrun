DAY = 3
DELIM1 = "---"
TESTS = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603///6"""

DEBUG = False

def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read()
    return data

def solve(data):

    count = 0

    triangles = []

    data = data.split("\n")

    max_row = len(data)

    for i in range(0, max_row, 3):
        if not data[i].strip(): continue
        row1 = data[i].split(" ")
        row2 = data[i+1].split(" ")
        row3 = data[i+2].split(" ")

        row1 = [s for s in row1 if s.strip()]
        row2 = [s for s in row2 if s.strip()]
        row3 = [s for s in row3 if s.strip()]

        for a, b, c in zip(row1, row2, row3):
            triangles.append(f"{a} {b} {c}")

    for row in triangles:
        
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
