from adventofcode.common import run, input_to_lines, input_to_grid

def get_possible_results(left_possibles, remaining_nos, part):
    new_possibles = []
    right = remaining_nos[0]
    for left in left_possibles:
        if part != 2:
            new_possibles.extend([left+right, left*right])
        else:
            new_possibles.extend([left + right, left * right, int(f"{left}{right}")])
    if len(remaining_nos) > 1:
        return get_possible_results(new_possibles, remaining_nos[1:], part)
    else:
        return new_possibles

def part1(input, part):
    input = input.split("\n")
    calibration_result = 0
    for line in input:
        test_value = int(line.split(":")[0])
        numbers = [int(x) for x in line.split(" ")[1:]]
        if test_value in get_possible_results([numbers[0]], numbers[1:], part):
            calibration_result += test_value
    return calibration_result


if __name__ == '__main__':
    run(cb1=part1, cb2=part1)