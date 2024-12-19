from adventofcode.common import run, input_to_grid, input_to_lines
from functools import cache

@cache
def test_design(design, patterns):
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            if len(pattern) == len(design):
                return True
            else:
                if test_design(design[len(pattern):], patterns):
                    return True
    return False

@cache
def test_design2(design, patterns):
    no_possibilities = 0
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            if len(pattern) == len(design):
                no_possibilities += 1
            else:
                no_possibilities += test_design2(design[len(pattern):], patterns)
    return no_possibilities

def puzzle(input, part=1, example=False, *args, **kwargs):
    lines = input_to_lines(input)

    patterns = [x.strip() for x in lines[0].split(",")]
    designs = lines[2:]

    ct = 0
    for design in designs:
        if part == 1:
            if test_design(design, tuple(patterns)):
                ct += 1
        else:
            ct += test_design2(design, tuple(patterns))

    return ct



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)