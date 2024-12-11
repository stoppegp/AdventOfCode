from adventofcode.common import run, input_to_lines, input_to_grid
from functools import cache
from scipy import interpolate
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

def part1(input, part):
    stones_base = tuple([int(x) for x in input.split()])
    sum = 0
    for stone in stones_base:
        y0 = 0
        x0 = 0
        x = []
        y = []
        stones = tuple([stone])
        for i in range(30):
            stones = blink(stones)
            print(len(stones))
            if i == 2:
                y0 = math.log(len(stones), 10)
                x0 = i
            if i > 1:
                x.append(i)
                y.append(math.log(len(stones), 10))

        x1 = i
        y1 = math.log(len(stones), 10)

        b = (y1-y0)/(x1-x0)
        c = y1 - b * x1

        if part == 1:
            check = 24
        else:
            check = 74

        f = interpolate.interp1d(x, y, kind='linear', fill_value="extrapolate")

        sum += round(10**f(check))
        #sum += round(10**(b*check+c))
    return sum

if __name__ == '__main__':
    #run(cb1=part1)
    run(cb2=part1)