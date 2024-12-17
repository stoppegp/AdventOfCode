from adventofcode.common import run, input_to_grid, input_to_lines
import re
first_free_char = 58
next_free_char = first_free_char
char_diff = 32

def puzzle(input, part, example=False, *args, **kwargs):
    lines = input_to_lines(input)

    reg_a = 0
    reg_b = 0
    reg_c = 0
    program = []
    in_ct = 0

    for line in lines:
        if "Register A" in line:
            reg_a = int(line.split(" ")[-1])
        if "Register B" in line:
            reg_b = int(line.split(" ")[-1])
        if "Register C" in line:
            reg_c = int(line.split(" ")[-1])
        if "Program" in line:
            program = [int(x) for x in line.split(" ")[-1].split(",")]


    def combo(op):
        if 0 <= op <= 3:
            return op
        if op == 4:
            return reg_a
        if op == 5:
            return reg_b
        if op == 6:
            return reg_c
        raise Exception()

    def step_it(in_ct, program, reg_a, reg_b, reg_c):
        opcode = program[in_ct]
        op = program[in_ct+1]

        #print(f"Op: {opcode} | {op}")
        #print(f"In: {reg_a:0b} | {reg_b:0b} | {reg_c:0b}")

        out = []

        if opcode == 0:
            # adv
            # shift right by combo(op)
            reg_a = int(reg_a/(2**combo(op)))
            in_ct += 2
        if opcode == 1:
            #bxl
            reg_b = reg_b ^ op
            in_ct += 2
        if opcode == 2:
            #bst
            # 3 bits least sig
            reg_b = combo(op) % 8
            in_ct += 2
        if opcode == 3:
            #jnz
            if reg_a != 0:
                in_ct = op
            else:
                in_ct += 2
        if opcode == 4:
            #bxc
            reg_b = reg_b ^ reg_c
            in_ct += 2
        if opcode == 5:
            #out
            # least sig  3 bits
            out.append(str(combo(op) % 8))
            in_ct += 2
        if opcode == 6:
            #bdv
            # shift by combo(op)
            reg_b = int(reg_a / (2 ** combo(op)))
            in_ct += 2
        if opcode == 7:
            # cdv
            # shift by combo(op)
            reg_c = int(reg_a / (2 ** combo(op)))
            in_ct += 2
        #print(f"In: {reg_a:0b} | {reg_b:0b} | {reg_c:0b}")
        return in_ct, out, reg_a, reg_b, reg_c

    if part == 1:
        in_ct = 0
        out = []
        i = 0
        while in_ct < len(program):
            i += 1
            in_ct, out_loc, reg_a, reg_b, reg_c = step_it(in_ct, program, reg_a, reg_b, reg_c)
            out.extend(out_loc)
        if part == 1:
            return ",".join(out)
    else:
        solutions = []
        search(0, 0, program, solutions)
        return min(solutions)

def search(a, i, program, solutions):
    #print(f"check {a:0b} | {i}")
    if i == len(program):
        solutions.append(a)
        return
    moep = False
    for check in range(8):
        a_check = int(f"{a:0b}{check:03b}",2)
        b = a_check % 8
        b = b ^ 0b111
        c = int(a_check / (2**b))
        b = b ^ c
        b = b ^ 0b111
        b = b % 8
        if a == 60:
            pass
        if str(b) == str(program[-(i+1)]):
            #print(f"found {check}")
            moep = True
            try:
                search(a_check, i+1, program, solutions)
            except:
                pass
    if not moep:
        raise Exception



if __name__ == '__main__':
    run(cb=puzzle, example_file="example1", solution_file="solution1", part=1)
    run(cb=puzzle, part=2)
    #run(cb2=puzzle2b)
