def file_lines_as_matrix(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [list(line.rstrip("\n")) for line in file]


def find_trees(slope, right=3, down=1):
    rows = len(slope)
    cols = len(slope[0])
    c = 0
    trees_encountered = 0
    for r in range(down, rows, down):
        c += right
        c %= cols
        if slope[r][c] == '#':
            trees_encountered += 1
    return trees_encountered


slope = file_lines_as_matrix("day_3_input.txt")
print(f"solution 1: {find_trees(slope)}")

multiplied_trees = 1
for i in range(1, 10, 2):
    d = int(i / 8) + 1
    r = i % 8
    trees = find_trees(slope, r, d)
    print(f"traversing for Right: {r} and Down: {d} - {trees} trees")
    multiplied_trees *= trees

find_trees(slope, 1, 2)
print(f"multiplied trees: {multiplied_trees}")
