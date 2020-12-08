def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [line.rstrip("\n") for line in file]
