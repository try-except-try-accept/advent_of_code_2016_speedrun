from re import search, match, findall
from collections import Counter


GREEDY = "\[.+\]" # greedily match anything between [ and ]
LAZY = "\[.+?\]"  # lazily match anything between [ and ]

DAY = 8
DELIM1 = "---"
TESTS = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1///6"""

DEBUG = True

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
    WIDTH = 50
    HEIGHT = 6
    screen = [["." for i in range(WIDTH)] for j in range(HEIGHT)]

    for instruction in data.split("\n"):
        if not instruction.strip(): continue
        print(instruction)

        if "rect" in instruction:
            width, height = instruction.split("x")
            width = width[5:]
            width = int(width)
            height = int(height)

            for y in range(height):
                for x in range(width):
                    screen[y][x] = "#"

        elif "rotate" in instruction:
            column, row = None, None
            if "column" in instruction:
                column, shift = instruction.split(" by ")
                column = column.replace("rotate column x=", "")
                column, shift = int(column), int(shift)
            else:
                row, shift = instruction.split(" by ")
                row = row.replace("rotate row y=", "")
                row, shift = int(row), int(shift)

            if row is not None:
                new_row = list(screen[row])
                for i, pixel in enumerate(screen[row]):
                    new_index = (i + shift) % WIDTH
                    new_row[new_index] = pixel
                screen[row] = new_row
            else:
                col = [screen[y][column] for y in range(0, HEIGHT)]
                new_col = list(col)
                for i, pixel in enumerate(col):
                    new_index = (i + shift) % HEIGHT
                    new_col[new_index] = pixel

                for y, change in enumerate(new_col):
                    screen[y][column] = change
                    

    for row in screen:
        for pixel in row:
            print(pixel, end="")
        print()


    

    return sum([row.count("#") for row in screen])


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
