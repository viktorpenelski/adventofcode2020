def file_lines_as_list(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        # list(str) returns a char array :O
        return [line.rstrip("\n") for line in file]

x = file_lines_as_list("day_4_input.txt")


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


class ByrValidatable():
    def short(self): return "byr"
    def valid(self, byr):
        return len(byr) == 4 and byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002

class IyrValidatable():
    def short(self): return "iyr"
    def valid(self, iyr):
        return len(iyr) == 4 and iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020

class EyrValidatable():
    def short(self): return "eyr"
    def valid(self, eyr):
        return len(eyr) == 4 and eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030

class HgtValidatable():
    def short(self): return "hgt"
    def valid(self, hgt):
        if hgt.endswith("cm"):
            cm = int(hgt.split("cm")[0])
            return cm >= 150 and cm <= 193
        elif hgt.endswith("in"):
            inches = int(hgt.split("in")[0])
            return inches >= 59 and inches <= 76
        else:
            return False

class HclValidatable():
    def short(self): return "hcl"
    def valid(self, hcl):
        if not hcl.startswith('#'):
            return False
        if not len(hcl) == 7:
            return False
        import string
        return all(c in string.hexdigits for c in hcl.split('#')[1])

class EclValidatable():
    def short(self): return "ecl"
    def valid(self, ecl):
        valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        return ecl in valid_eye_colors

class PidValidatable():
    def short(self): return "pid"
    def valid(self, pid):
        return len(pid) == 9 and pid.isdigit()


class Validator():

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

for line in x:
    if line != "":
        add_to_passport(line, passport)
    else:
        all_passports.append(passport)
        passport = {}

# append the last passport
all_passports.append(passport)

validator = Validator([ByrValidatable(),\
                     IyrValidatable(),\
                    EyrValidatable(),\
                    HgtValidatable(),\
                    HclValidatable(),\
                    EclValidatable(),\
                    PidValidatable(),\
])

mandatory_fields_passports = [p for p in all_passports if mandatory_fields_present(p)]
print(f"mandatory fields present: {len(mandatory_fields_passports)}")

valid_passports = [p for p in all_passports if validator.validate(p)]
print(f"validated passports: {len(valid_passports)}")
