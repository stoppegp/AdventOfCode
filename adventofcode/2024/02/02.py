from adventofcode.common import parse_input

input = parse_input("input")

no_safe = 0


def check_safe(levels):
    prev = None
    no_safe_inc = 0
    no_safe_dec = 0
    no_unsafe = 0
    for x in levels:
        if prev is not None:
            if abs(x-prev) > 3:
                no_unsafe += 1
                break
            if abs(x-prev) == 0:
                no_unsafe += 1
                break
            if x-prev > 0:
                no_safe_inc += 1
            else:
                no_safe_dec += 1
        prev = x
    return no_unsafe + min(no_safe_inc, no_safe_dec) == 0

for row in input:
    levels = [int(x) for x in row.split()]
    if check_safe(levels):
        no_safe += 1
    else:
        # part 2
        for i in range(0,len(levels)):
            new_levels = [x for j, x in enumerate(levels) if j != i]
            if check_safe(new_levels):
                no_safe += 1
                break


print(no_safe)