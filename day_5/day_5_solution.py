import math


# turns out that if I have a folder `foo` and file named `foo.py`,
# there is a conflict when importing in another file within the same folder

def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [line.rstrip("\n") for line in file]


def find_row(bpass):
    lo = 0
    hi = 127
    for i in range(0, 7):
        difference = math.ceil((hi - lo) / 2)
        if 'F' == bpass[i]:
            hi -= difference
        elif 'B' == bpass[i]:
            lo += difference
        else:
            raise Exception("first 7 chars of the boarding pass should be either 'F' or 'B'!")
    return lo


def find_col(bpass):
    lo = 0
    hi = 7
    for i in range(7, 10):
        difference = math.ceil((hi - lo) / 2)
        if 'L' == bpass[i]:
            hi -= difference
        elif 'R' == bpass[i]:
            lo += difference
        else:
            raise Exception("last 3 chars of the boarding pass should be either 'R' or 'L'!")
    return lo


def find_id(row, col):
    return row * 8 + col


all_passes = file_lines_as_list("day_5_input.txt")

all_ids = [find_id(find_row(x), find_col(x)) for x in all_passes]
all_ids.sort()
max_id = all_ids[len(all_ids) - 1]
print(f"max seat id: {max_id}")

# some of the seats at the very front and back of the plane don't exist on this aircraft,
# so they'll be missing from your list as well.
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
# based on that description, that means our seat *must* be between two valid ids,
# where they are adjacent and missing a single seat id  in between
for i in range(1, len(all_ids)):
    if all_ids[i] - all_ids[i - 1] == 2:
        print(f"seat id: {all_ids[i] - 1}")
