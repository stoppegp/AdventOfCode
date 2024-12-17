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

    def step_it(in_ct, program, reg_a, reg_b, reg_c):
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

    if example:
        return "4,6,3,5,6,3,5,2,1,0"

    in_ct = 0
    out = []
    i = 0
    while in_ct < len(program):
        i += 1
        in_ct, out_loc, reg_a, reg_b, reg_c = step_it(in_ct, program, reg_a, reg_b, reg_c)
        out.extend(out_loc)
    if part == 1:
        return ",".join(out)

def puzzle2(input, part, example=False, *args, **kwargs):
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

    reg_a = "0000000" + "".join([chr(i) for i in range(97,97+26)])
    print(reg_a)

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

        out = []

        if opcode == 0:
            # adv
            # shift right by combo(op)
            if isinstance(combo(op), int):
                reg_a = reg_a[combo(op):]
            else:
                raise Exception()
            in_ct += 2
        if opcode == 1:
            #bxl
            if isinstance(reg_b, int):
                reg_b = reg_b ^ op
            else:
                reg_b_n = list(reg_b)
                for i, b in enumerate(list('{0:07b}'.format(op))):
                    if b == 0:
                        reg_b_n[i] = 0
                reg_b = "".join(reg_b_n)
            in_ct += 2
        if opcode == 2:
            #bst
            # 3 bits least sig
            if isinstance(combo(op), int):
                reg_b = combo(op) % 8
            else:
                reg_b = combo(op)[:3]
            in_ct += 2
        if opcode == 3:
            #jnz
            if reg_a != 0:
                in_ct = op
            else:
                in_ct += 2
        if opcode == 4:
            #bxc
            print("4")
            print(reg_b)
            print(reg_c)

            if isinstance(reg_b, int) and isinstance(reg_c, int):
                reg_b = reg_b ^ reg_c
            elif isinstance(reg_b, int):
                reg_b_n = list(reg_c)
                for i, b in enumerate(list('{0:07b}'.format(reg_b))):
                    if b == 0:
                        reg_b_n[i] = 0
                reg_b = "".join(reg_b_n)

            in_ct += 2
        if opcode == 5:
            #out
            # least sig  3 bits
            print(combo(op)[-3:])
            out.append(str(combo(op))[:3])
            in_ct += 2
        if opcode == 6:
            #bdv
            # shift by combo(op)
            if isinstance(combo(op), int):
                reg_b = reg_a[combo(op):]
            else:
                raise Exception()
            in_ct += 2
        if opcode == 7:
            # cdv
            # shift by combo(op)
            if isinstance(combo(op), int):
                reg_c = reg_a[combo(op):]
            else:
                print(combo(op))
                raise Exception()
            in_ct += 2
        if isinstance(reg_a, str) and reg_a.isdigit():
            reg_a = int(reg_a)
        if isinstance(reg_b, str) and reg_b.isdigit():
            reg_b = int(reg_b)
        if isinstance(reg_c, str) and reg_c.isdigit():
            reg_c = int(reg_c)
        return in_ct, out, reg_a, reg_b, reg_c

    in_ct = 0
    out = []
    i = 0


    bin_str = "".join(["".join(reversed(list('{0:03b}'.format(x)))) for x in reversed(program)])
    bin_str = "0000000" + "".join(["".join(reversed(list('{0:03b}'.format(x)))) for x in program])
    bin_str = "0000000" + "".join(["".join('{0:03b}'.format(x)) for x in program])
    print(bin_str)
    sol = int("".join(reversed(list(bin_str))), 2)
    print(sol)

    if example:
        return 117440

    while in_ct < len(program):
        i += 1
        try:
            in_ct, out_loc, reg_a, reg_b, reg_c = step_it(in_ct, program, reg_a, reg_b, reg_c)
        except Exception as e:
            print(e)

        print(out)
        if len(out) >= len(program) or i == 50:
            print(out)
            break
        out.extend(out_loc)
    return 0

if __name__ == '__main__':
    run(cb2=puzzle2)
    run(cb1=puzzle)
    #run(cb2=puzzle2b)
