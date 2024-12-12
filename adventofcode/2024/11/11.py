from adventofcode.common import run, input_to_lines, input_to_grid
from functools import cache
import math

@cache
def blink_one(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        # print(stone)
        half = int(len(str(stone)) / 2)
        # print(len(str(stone)) )
        return [int(str(stone)[:half]), int(str(stone)[half:])]
    else:
        return [stone * 2024]


def count_on(current):
    #ret = {x: 0 for x in next_stones.keys()}
    ret = {}
    for stone, ct in current.items():
        new_stones = blink_one(stone)
        for new_stone in new_stones:
            if new_stone not in ret.keys():
                ret[new_stone] = 0
            ret[new_stone] += 1*ct

    return ret

def part1(input, part):
    stones = [int(x) for x in input.split()]
    stones_cur = {x: stones.count(x) for x in set(stones)}

    if part == 1:
        target_no = 25
    else:
        target_no = 75

    for i in range(target_no):
        print(i)
        stones_cur = count_on(stones_cur)


    return sum(list(stones_cur.values()))


if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)