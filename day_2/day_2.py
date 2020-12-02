from dataclasses import dataclass


def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


@dataclass
class Validation:
    min: int
    max: int
    char: chr
    password: str

    def is_valid_count(self):
        count = self.password.count(char)
        return self.min <= count <= self.max

    def is_valid_idx(self):
        idx_one = self.min - 1
        idx_two = self.max - 1
        if len(self.password) <= idx_two:
            return False
        if self.password[idx_one] == self.char and self.password[idx_two] != self.char:
            return True
        if self.password[idx_one] != self.char and self.password[idx_two] == self.char:
            return True
        return False


def validation_from_raw_string(string):
    split = string.split(" ")
    min_occurrences = int(split[0].split("-")[0])
    max_occurrences = int(split[0].split("-")[1])
    char = split[1].strip(":")
    password = split[2]
    return Validation(min_occurrences, max_occurrences, char, password)


records = file_lines_as_list("day_2_input.txt")
valid_passwords = 0
for el in records:
    validation = validation_from_raw_string(el)
    if validation.is_valid_idx():
        valid_passwords += 1

print(valid_passwords)
