def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [line.rstrip("\n") for line in file]


raw_input_lines = file_lines_as_list("day_4_input.txt")


def add_to_passport(line, passport):
    fields = line.split(" ")
    for field in fields:
        kv = field.split(":")
        passport[kv[0]] = kv[1]


def mandatory_fields_present(passport):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in mandatory_fields:
        if field not in passport.keys():
            return False
    return True


class ByrValidatable:
    @staticmethod
    def short(): return "byr"

    def valid(self, byr):
        return len(byr) == 4 and byr.isdigit() and 1920 <= int(byr) <= 2002


class IyrValidatable:
    @staticmethod
    def short(): return "iyr"

    def valid(self, iyr):
        return len(iyr) == 4 and iyr.isdigit() and 2010 <= int(iyr) <= 2020


class EyrValidatable:
    @staticmethod
    def short(): return "eyr"

    def valid(self, eyr):
        return len(eyr) == 4 and eyr.isdigit() and 2020 <= int(eyr) <= 2030


class HgtValidatable:
    @staticmethod
    def short():
        return "hgt"

    def valid(self, hgt):
        if hgt.endswith("cm"):
            cm = int(hgt.split("cm")[0])
            return cm >= 150 and cm <= 193
        elif hgt.endswith("in"):
            inches = int(hgt.split("in")[0])
            return 59 <= inches <= 76
        else:
            return False


class HclValidatable:
    @staticmethod
    def short():
        return "hcl"

    def valid(self, hcl):
        if not hcl.startswith('#'):
            return False
        if not len(hcl) == 7:
            return False
        import string
        return all(c in string.hexdigits for c in hcl.split('#')[1])


class EclValidatable:
    @staticmethod
    def short(): return "ecl"

    def valid(self, ecl):
        valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        return ecl in valid_eye_colors


class PidValidatable:
    @staticmethod
    def short(): return "pid"

    def valid(self, pid):
        return len(pid) == 9 and pid.isdigit()


class Validator:

    def __init__(self, validatables):
        self.validatables = validatables

    def validate(self, dict):
        for v in self.validatables:
            if v.short() not in dict.keys():
                return False
            if not v.valid(dict[v.short()]):
                return False
        return True


passport = {}
all_passports = []

for line in raw_input_lines:
    if line != "":
        add_to_passport(line, passport)
    else:
        all_passports.append(passport)
        passport = {}

# append the last passport
all_passports.append(passport)

validator = Validator([ByrValidatable(),
                       IyrValidatable(),
                       EyrValidatable(),
                       HgtValidatable(),
                       HclValidatable(),
                       EclValidatable(),
                       PidValidatable(),
                       ])

mandatory_fields_passports = [p for p in all_passports if mandatory_fields_present(p)]
print(f"mandatory fields present: {len(mandatory_fields_passports)}")

valid_passports = [p for p in all_passports if validator.validate(p)]
print(f"validated passports: {len(valid_passports)}")
