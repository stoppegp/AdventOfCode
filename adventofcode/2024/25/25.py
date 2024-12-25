from adventofcode.common import run, input_to_lines

def puzzle(input, part=1, example=False, *args, **kwargs):

    lines = input_to_lines(input)

    keys = []
    locks = []

    for row, line in enumerate(lines):
        if line == "#####" and (row == 0 or lines[row-1].strip() == ""):
            current_type = "lock"
            current_lock = [0,0,0,0,0]
        elif line.strip() != "" and (row == 0 or lines[row-1].strip() == ""):
            current_type = "key"
            current_key = [-1,-1,-1,-1,-1]
        elif line.strip() == "":
            if current_type == "lock":
                locks.append(current_lock)
            else:
                keys.append(current_key)
        elif current_type == "lock":
            for i, v in enumerate(list(line)):
                if v == "#":
                    current_lock[i] += 1
        elif current_type == "key":
            for i, v in enumerate(list(line)):
                if v == "#":
                    current_key[i] += 1
        if row == len(lines) - 1:
            if current_type == "lock":
                locks.append(current_lock)
            else:
                keys.append(current_key)

    fitting_keys = 0
    ts = 5
    for key in keys:
        for lock in locks:
            test_val = [key[i]+lock[i]<=ts for i in range(len(key))]

            if sum(test_val) == 5:
                fitting_keys += 1
    return fitting_keys



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")