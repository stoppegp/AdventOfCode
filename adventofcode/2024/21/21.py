from adventofcode.common import run, input_to_grid, input_to_lines
import re
from functools import cache
import math

def puzzle(input, part=1, example=False, *args, **kwargs):

    def key_diff(key, prev):
        keys = {"^": complex(1, 1),
                "A": complex(2, 1),
                "<": complex(0, 0),
                "v": complex(1, 0),
                ">": complex(2, 0)}
        return keys[key]-keys[prev]

    def key_diff_num(key, prev):
        keys = {"7": complex(0, 3),
                "8": complex(1, 3),
                "9": complex(2, 3),
                "4": complex(0, 2),
                "5": complex(1, 2),
                "6": complex(2, 2),
                "1": complex(0, 1),
                "2": complex(1, 1),
                "3": complex(2, 1),
                "0": complex(1, 0),
                "A": complex(2, 0)}
        return keys[key]-keys[prev]

    def cost_press_key_on_num(key, prev, X):
        kd = key_diff_num(key, prev)
        if prev in ["0", "A"] and key in ["1", "4", "7"]:
            paths = ["^"*int(abs(kd.imag))+"<"*int(abs(kd.real))]
        elif key in ["0", "A"] and prev in ["1", "4", "7"]:
            paths = [">"*int(abs(kd.real))+"v"*int(abs(kd.imag))]
        else:
            if kd.real > 0:
                sx = ">"
            else:
                sx = "<"
            if kd.imag > 0:
                sy = "^"
            else:
                sy = "v"
            paths = [sx*int(abs(kd.real)) + sy*int(abs(kd.imag)),
                     sy*int(abs(kd.imag)) + sx*int(abs(kd.real))]
        cost = math.inf
        for path in paths:
            path_cost = 0
            x2 = "A"
            for i in range(len(path)):
                x1 = path[i-1] if i > 0 else "A"
                x2 = path[i]
                path_cost += cost_press_key_onX(x2, x1, X)
            path_cost += cost_press_key_onX("A", x2, X)
            cost = min(cost, path_cost)
        return cost

    @cache
    def cost_press_key_onX(key, prev, X):
        kd = key_diff(key, prev)
        if prev == "<":
            paths = [">"*int(abs(kd.real))+"^"*int(abs(kd.imag))]
        elif key == "<":
            paths = ["v"*int(abs(kd.imag))+"<"*int(abs(kd.real))]
        else:
            if kd.real > 0:
                sx = ">"
            else:
                sx = "<"
            if kd.imag > 0:
                sy = "^"
            else:
                sy = "v"
            paths = [sx*int(abs(kd.real)) + sy*int(abs(kd.imag)),
                     sy*int(abs(kd.imag)) + sx*int(abs(kd.real))]
        cost = math.inf
        for path in paths:
            if X > 1:
                path_cost = 0
                x2 = "A"
                for i in range(len(path)):
                    x1 = path[i-1] if i > 0 else "A"
                    x2 = path[i]
                    path_cost += cost_press_key_onX(x2, x1, X-1)
                path_cost += cost_press_key_onX("A", x2, X-1)
                cost = min(cost, path_cost)
            else:
                path_cost = len(path) + 1
                cost = min(cost, path_cost)
        return cost

    def seq_cost(seq, num_ctl=2, X=2):
        full_cost = 0
        start = "A"
        for y in list(seq):
            min_cost = cost_press_key_on_num(y, start, X)
            start = y
            full_cost += min_cost
        print(f"{seq}: {full_cost}")
        return full_cost

    num_ctl = 2 if part == 1 else 25

    lines = input_to_lines(input)
    final_sum = 0
    for seq in lines:
        cost = seq_cost(seq, num_ctl, num_ctl)
        final_sum += int(seq.replace("A", "")) * cost#


    return final_sum



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)