from adventofcode.common import parse_input
import regex as re

input = parse_input("input")

calibration_values = []

for inline in input:
    ma = re.sub("[^0-9]", "", inline)
    calibration_values.append(int(ma[0] + ma[-1]))

solution_part1 = sum(calibration_values)
print(solution_part1)

# part 2

repldict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


# variant 1: overlapping regex
new_calibration_values_var1 = []
for ix, inline in enumerate(input):
    pattern = "[0-9]|" + "|".join(repldict.keys())
    matches = re.findall(pattern, inline, overlapped=True)
    first_match = matches[0]
    if first_match in repldict.keys():
        first_match = repldict[first_match]
    last_match = matches[-1]
    if last_match in repldict.keys():
        last_match = repldict[last_match]
    cal_value = int(first_match + last_match)
    new_calibration_values_var1.append(cal_value)

new_calibration_values_var2 = []

# variant 2 replace 1 with one1one
for inline in input:
    new_inline = inline

    for k, v in repldict.items():
        new_inline = new_inline.replace(k, k+v+k)
    ma = re.sub("[^0-9]", "", new_inline)
    cal_value = int(ma[0] + ma[-1])
    new_calibration_values_var2.append(cal_value)

solution_part1_var1 = sum(new_calibration_values_var1)
solution_part1_var2 = sum(new_calibration_values_var2)
print(solution_part1_var1)
print(solution_part1_var2)