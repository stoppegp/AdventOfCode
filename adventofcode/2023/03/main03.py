from adventofcode.common import parse_input
import re

input = parse_input("input")



numbers = []

for x, inline in enumerate(input):
    matches = re.finditer("[0-9]+", inline)
    for match in matches:
        numbers.append((x, match.start(), int(match.group())))

part_numbers = []

for nrrow, nrcol, nr in numbers:
    is_part_nr = False
    last_line_index = len(input[0])-1
    last_nr_index = nrcol+len(str(nr))-1

    if nrcol > 0 and input[nrrow][nrcol-1] != ".":
        is_part_nr = True
    if last_nr_index < last_line_index and input[nrrow][last_nr_index+1] != ".":
        is_part_nr = True
    if nrrow >0:
        for i in range(max(0,nrcol-1), min(last_nr_index+2, last_line_index+1)):
            if input[nrrow-1][i] != ".":
                is_part_nr = True
    if nrrow < len(input)-1:
        for i in range(max(0,nrcol-1), min(last_nr_index+2, last_line_index+1)):
            if input[nrrow+1][i] != ".":
                is_part_nr = True
    if is_part_nr:
        part_numbers.append(nr)

solution_part1 = sum(part_numbers)
print(solution_part1)

#part2

gears = {}

for x, inline in enumerate(input):
    matches = re.finditer("\*", inline)
    for match in matches:
        gears[(x, match.start())] = []

for nrrow, nrcol, nr in numbers:
    last_line_index = len(input[0])-1
    last_nr_index = nrcol+len(str(nr))-1

    if nrcol > 0 and input[nrrow][nrcol-1] == "*":
        gears[(nrrow, nrcol-1)].append(nr)
        continue
    if last_nr_index < last_line_index and input[nrrow][last_nr_index+1] == "*":
        gears[(nrrow, last_nr_index+1)].append(nr)
        continue
    if nrrow >0:
        for i in range(max(0,nrcol-1), min(last_nr_index+2, last_line_index+1)):
            if input[nrrow-1][i] == "*":
                gears[(nrrow-1, i)].append(nr)
                continue
    if nrrow < len(input)-1:
        for i in range(max(0,nrcol-1), min(last_nr_index+2, last_line_index+1)):
            if input[nrrow+1][i] == "*":
                gears[(nrrow+1, i)].append(nr)
                continue

gear_ratios = []

for gear in gears.values():
    if len(gear) == 2:
        gear_ratios.append(gear[0]*gear[1])

solution_part2 = sum(gear_ratios)
print(solution_part2)