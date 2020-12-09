def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [line.rstrip("\n") for line in file]


unique_chars = set()
sum_of_answers = 0

all_lines = file_lines_as_list("day_6_input.txt")
for line in all_lines:
    if line != "":
        for c in line:
            unique_chars.add(c)
    else:
        sum_of_answers += len(unique_chars)
        unique_chars = set()

sum_of_answers += len(unique_chars)

print(f"sum of all answers: {sum_of_answers}")


all_answers = set()
unique_chars = set()
sum_of_correct_answers = 0
reset = True
for line in all_lines:
    if line != "":
        unique_chars = set()
        for c in line:
            unique_chars.add(c)
        if reset:
            reset = False
            all_answers = unique_chars
        else:
            all_answers = all_answers.intersection(unique_chars)

    else:
        reset = True
        sum_of_correct_answers += len(all_answers)
        all_answers = set()
        unique_chars = set()

sum_of_correct_answers += len(all_answers)


print(f"sum of correct answers: {sum_of_correct_answers}")
