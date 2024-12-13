from adventofcode.common import run, input_to_grid
import re
from tqdm import tqdm


def part1_bf(input, part):
    machines = [{}]

    for row in input.split("\n"):
        if "Button A" in row:
            machines[-1]['a'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Button B" in row:
            machines[-1]['b'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Prize" in row:
            machines[-1]['prize'] = int(re.search(r"X=(\d+)", row).groups()[0]), int(re.search(r"Y=(\d+)", row).groups()[0])
        if row.strip() == "":
            machines.append({})

    def step(pos, step):
        return (pos[0]+step[0], pos[1]+step[1])
    tokens = 0
    for machine in machines:
        a = machine['a']
        b = machine['b']
        prize = machine['prize']
        paths = []
        tokens_loc = 0
        for i_a in range(101):
            test_pos_a = (i_a*a[0], i_a*a[1])
            if test_pos_a[0] > prize[0]:
                break
            if test_pos_a[1] > prize[1]:
                break
            for i_b in range(101):
                test_pos = (i_a*a[0] + i_b*b[0], i_a*a[1] + i_b*b[1])
                if test_pos_a[0] > prize[0]:
                    break
                if test_pos_a[1] > prize[1]:
                    break
                if test_pos == prize:
                    paths.append((i_a, i_b))
                    break
        if len(paths) > 0:
            tokens_loc = [i_a*3+i_b for i_a, i_b in paths]
            tokens += min(tokens_loc)

    return tokens

def bf_opt_stillnotworking(input, part):
    machines = [{}]

    if part == 2:
        offset = 10000000000000
    else:
        offset = 0
    for row in input.split("\n"):
        if "Button A" in row:
            machines[-1]['a'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Button B" in row:
            machines[-1]['b'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Prize" in row:
            machines[-1]['prize'] = int(re.search(r"X=(\d+)", row).groups()[0])+offset, int(re.search(r"Y=(\d+)", row).groups()[0])+offset
        if row.strip() == "":
            machines.append({})

    def step(pos, step):
        return (pos[0]+step[0], pos[1]+step[1])
    tokens = 0
    for ix, machine in enumerate(machines):
        a = machine['a']
        b = machine['b']
        prize = machine['prize']
        paths = []
        tokens_loc = 0
        max_i_a = int(min(prize[0]/a[0], prize[1]/a[1]))
        for i_a in range(max_i_a):
            test_pos_a = (i_a*a[0], i_a*a[1])
            if test_pos_a[0] > prize[0]:
                break
            if test_pos_a[1] > prize[1]:
                break
            remaining_x = prize[0] - test_pos_a[0]
            remaining_y = prize[1] - test_pos_a[1]
            remaining_i_x = remaining_x/b[0]
            remaining_i_y = remaining_y / b[1]
            if int(remaining_i_x) != remaining_i_x or remaining_i_x != remaining_i_y:
                continue
            else:
                paths.append((i_a, remaining_i_x))
        if len(paths) > 0:
            print(paths)
            tokens_loc = [i_a*3+i_b for i_a, i_b in paths]
            tokens += min(tokens_loc)

    return int(tokens)

def simple_math(input, part):
    machines = [{}]

    if part == 2:
        offset = 10000000000000
    else:
        offset = 0
    for row in input.split("\n"):
        if "Button A" in row:
            machines[-1]['a'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Button B" in row:
            machines[-1]['b'] = int(re.search(r"X\+(\d+)", row).groups()[0]), int(re.search(r"Y\+(\d+)", row).groups()[0])
        if "Prize" in row:
            machines[-1]['prize'] = int(re.search(r"X=(\d+)", row).groups()[0])+offset, int(re.search(r"Y=(\d+)", row).groups()[0])+offset
        if row.strip() == "":
            machines.append({})

    def step(pos, step):
        return (pos[0]+step[0], pos[1]+step[1])
    tokens = 0
    for ix, machine in enumerate(machines):
        a = machine['a']
        b = machine['b']
        prize = machine['prize']
        i_a_num = prize[0] / a[0] - prize[1] * b[0] / b[1] / a[0]
        i_a_den = 1 - a[1] * b[0] / b[1] / a[0]
        i_a = round(i_a_num / i_a_den)
        i_b = round(prize[1] / b[1] - i_a * a[1] / b[1])
        print(i_a)
        print(i_b)
        if i_a*a[0]+i_b*b[0] == prize[0] and i_a*a[1]+i_b*b[1] == prize[1]:
            tokens_loc = i_a*3+i_b
            tokens += tokens_loc

    return int(tokens)

if __name__ == '__main__':
    run(cb1=simple_math)
    run(cb2=simple_math)