import math

boarding_pass = "FFFBBBFRRR"


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


find_row(boarding_pass)