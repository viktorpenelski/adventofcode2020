from dataclasses import dataclass
from enum import Enum

from file_reader import file_lines_as_list


def parse_line(line):
    split = line.split(" ")
    instruction = Instruction(split[0])
    value = int(split[1])
    return Input(instruction, value)


class Instruction(Enum):
    no_op = "nop"
    accumulate = "acc"
    jump = "jmp"


@dataclass
class Input:
    instruction: Instruction
    value: int


def try_solve(input_lines):
    accum = 0
    lines_seen = set()
    idx = 0
    while True:
        if idx == len(input_lines):
            return accum, True
        if idx in lines_seen:
            return accum, False
        lines_seen.add(idx)
        instruction_line = input_lines[idx]
        if instruction_line.instruction == Instruction.no_op:
            idx += 1
        elif instruction_line.instruction == Instruction.accumulate:
            accum += instruction_line.value
            idx += 1
        elif instruction_line.instruction == Instruction.jump:
            idx += instruction_line.value


lines = file_lines_as_list("input.txt")
parsed = [parse_line(x) for x in lines]
print(f"first loop leaves accumulator at: {try_solve(parsed)[0]}")

for idx, instr in enumerate(parsed):
    original_instruction = instr.instruction
    if instr.instruction == Instruction.jump:
        parsed[idx].instruction = Instruction.no_op
    elif instr.instruction == Instruction.no_op:
        parsed[idx].instruction = Instruction.jump
    solution, no_loop = try_solve(parsed)
    if no_loop:
        print(f"found a solution with no loop by changing idx {idx} from {original_instruction} - {solution}")
        break
    parsed[idx].instruction = original_instruction
