from adventofcode.common import run, input_to_grid, input_to_lines
import re



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

    def step(in_ct, program, reg_a, reg_b, reg_c):
        opcode = program[in_ct]
        op = program[in_ct+1]

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
        return in_ct, out, reg_a, reg_b, reg_c

    in_ct = 0
    out = []
    i = 0
    while in_ct < len(program):
        i += 1
        in_ct, out_loc, reg_a, reg_b, reg_c = step(in_ct, program, reg_a, reg_b, reg_c)
        if len(out) > 0:
            print(i)
            break
        out.extend(out_loc)
    if step == 1:
        return ",".join(out)

def puzzleB(input, part, example=False, *args, **kwargs):
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
    reg_a = int("000011100101011000000", 2)
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

    def step(in_ct, program, reg_a, reg_b, reg_c):
        opcode = program[in_ct]
        op = program[in_ct+1]

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
        return in_ct, out, reg_a, reg_b, reg_c

    in_ct = 0
    out = []
    i = 0
    while in_ct < len(program):
        i += 1
        in_ct, out_loc, reg_a, reg_b, reg_c = step(in_ct, program, reg_a, reg_b, reg_c)
        if len(out) > 0:
            print(i)
            break
        out.extend(out_loc)
    if step == 1:
        return ",".join(out)

def puzzle2(input, part, example=False, *args, **kwargs):
    lines = input_to_lines(input)

    reg_a = "x"
    reg_b = 0
    reg_c = 0
    program = []
    in_ct = 0

    for line in lines:
        #if "Register A" in line:
            #reg_a = str(int(line.split(" ")[-1]))
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

    def step(in_ct, program, reg_a, reg_b, reg_c):
        opcode = program[in_ct]
        op = program[in_ct+1]

        out = []

        if opcode == 0:
            # adv
            if isinstance(combo(op), int):

            if "x" in str(reg_a) or "x" in str(combo(op)):
                div = 2**combo(op)
                reg_a = f"int(({reg_a})/(2**({combo(op)})))"
            else:
                reg_a = int(reg_a/(2**combo(op)))
            in_ct += 2
        if opcode == 1:
            #bxl
            if "x" in str(reg_b):
                reg_b = f"({reg_b}) ^ ({op})"
            else:
                reg_b = eval(f"{reg_b} ^ {op}")
            in_ct += 2
        if opcode == 2:
            #bst
            if "x" in str(combo(op)):
                reg_b = f"({combo(op)}) % 8"
            else:
                reg_b = combo(op) % 8
            in_ct += 2
        if opcode == 3:
            #jnz
            #if reg_a != 0:
            in_ct = op
#            else:
#                in_ct += 2
        if opcode == 4:
            #bxc
            if "x" in str(reg_b) or "x" in str(reg_c):
                reg_b = f"({reg_b}) ^ ({reg_c})"
            else:
                reg_b = reg_b ^ reg_c
            in_ct += 2
        if opcode == 5:
            #out
            if "x" in str(combo(op)):
                out.append(f"({combo(op)}) % 8")
            else:
                out.append(str(combo(op) % 8))
            in_ct += 2
        if opcode == 6:
            #bdv
            if "x" in str(combo(op)) or "x" in reg_a:
                reg_b = f"int(({reg_a}) / (2 ** ({combo(op)})))"
            else:
                reg_b = int(reg_a / (2 ** combo(op)))
            in_ct += 2
        if opcode == 7:
            # cdv
            if "x" in str(combo(op)) or "x" in reg_a:
                reg_c = f"int(({reg_a}) / (2 ** ({combo(op)})))"
            else:
                reg_c = int(reg_a / (2 ** combo(op)))
            in_ct += 2
        return in_ct, out, reg_a, reg_b, reg_c

    in_ct = 0
    out = []
    i = 0
    while in_ct < len(program):
        i += 1
        in_ct, out_loc, reg_a, reg_b, reg_c = step(in_ct, program, reg_a, reg_b, reg_c)
        out.extend(out_loc)
        if len(out) >= len(program):
            break
    print(out)
    for x in range(0, 117450000):
        found_solution = True
        for i in range(len(out)):
            if eval(out[i].format(x=x)) != program[i]:
                found_solution = False
                break
        if found_solution:
            return x
            print(x)
            break

    if step == 1:
        return ",".join(out)
    else:
        return None

def puzzle2b(input, part, example=False, *args, **kwargs):
    lines = input_to_lines(input)

    reg_a = "x"
    reg_b = 0
    reg_c = 0
    program = []
    in_ct = 0

    for line in lines:
        #if "Register A" in line:
            #reg_a = str(int(line.split(" ")[-1]))
        if "Register B" in line:
            reg_b = int(line.split(" ")[-1])
        if "Register C" in line:
            reg_c = int(line.split(" ")[-1])
        if "Program" in line:
            program = [int(x) for x in line.split(" ")[-1].split(",")]

    out = ['000']
    for p in program:
        out.append('{0:03b}'.format(p))
    return int("".join(reversed(out)),2)

if __name__ == '__main__':
    run(cb1=puzzle2)
    #run(cb2=puzzle2b)