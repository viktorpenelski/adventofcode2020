from file_reader import file_lines_as_list


def find_first_invalid_num(data, preamble=25):
    # "the two numbers will have different values", hence we can treat the numbers as a set
    s = {data[i]: i for i in range(0, preamble)}
    for i in range(preamble, len(data)):
        sum_to_look_for = data[i]
        match = False
        for j in range(i - preamble, i):
            diff = sum_to_look_for - data[j]
            if diff in s and s[diff] != j:
                match = True
                break
        if not match:
            return sum_to_look_for
        num_to_remove = data[i - preamble]
        del s[num_to_remove]
        s[data[i]] = i


def find_sequence_summing_to(num, data):
    for i in range(0, len(data)):
        summed = data[i]
        j = i + 1
        while summed <= x and j < len(data):
            summed += data[j]
            if summed == num:
                return i, j
            j += 1
    raise Exception("could not find a sequence, should have found one by problem definition")


lines = file_lines_as_list("input.txt")
nums = [int(num) for num in lines]
x = find_first_invalid_num(nums)
print(f"first num with no two sum in preamble: {x}")
start, end = find_sequence_summing_to(x, nums)
min_seq_num = min(nums[start:end + 1])
max_seq_num = max(nums[start:end + 1])
print(f"sum of the min and max numbers within the sequence are is: {min_seq_num + max_seq_num}")
