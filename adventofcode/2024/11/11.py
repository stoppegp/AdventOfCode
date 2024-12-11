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

@cache
def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(blink_one(stone))
    return tuple(new_stones)

def count_on(current, next_stones):
    #ret = {x: 0 for x in next_stones.keys()}
    ret = {}
    for stone, ct in current.items():
        if stone in next_stones.keys():
            for st, ct2 in next_stones[stone].items():
                if st not in ret.keys():
                    ret[st] = 0
                ret[st] += ct*ct2
        else:
            new_stones = blink_one(stone)
            #next_stones[stone] = {}
            for new_stone in new_stones:
                if new_stone not in ret.keys():
                    ret[new_stone] = 0
                ret[new_stone] += 1*ct
                #if new_stone not in next_stones[stone].keys():
                #    next_stones[stone][new_stone] = 0
                #next_stones[stone][new_stone] += 1

    return ret, next_stones

def part1(input, part):
    stones = tuple([int(x) for x in input.split()])
    #for stone in stones_base:
    y0 = 0
    x0 = 0

    if part == 1:
        target_no = 25
    else:
        target_no = 75

    final_no = 0


    #stones = tuple([stone])
    # for i in range(target_no):
    #     print(f"initial scan: {i}")
    #     stones_set = set(stones)
    #     stones = blink(stones)
    #     print(len(set(stones)))
    #     if set(stones) == stones_set:
    #         break
    #
    # if i == target_no-1:
    #     final_no += len(stones)
    #     return final_no
    #
    # next_stones = {x: {} for x in stones_set}
    # for stone in stones_set:
    #     new_stones = blink_one(stone)
    #     for test_stone in stones_set:
    #         next_stones[stone][test_stone] = new_stones.count(test_stone)
    # #print(next_stones)
    #
    # current_no = i


    current_no = 0
    stones_cur = {x: stones.count(x) for x in set(stones)}
    next_stones = {}
    print(current_no)
    for i in range(current_no, target_no):
        print(i)
        print(stones_cur)
        stones_cur, next_stones = count_on(stones_cur, next_stones)
        print(next_stones)
        print(sum(list(stones_cur.values())))
        print()

    #f = interpolate.interp1d(x, y, kind='linear', fill_value="extrapolate")

    #sum += round(10**f(check))

    return sum(list(stones_cur.values()))


if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)