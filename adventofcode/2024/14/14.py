from adventofcode.common import run, input_to_grid, input_to_lines
import re
from functools import cache

def robot_move(pos, vel, t, len_x, len_y):
    x_new = (pos[0]+vel[0]*t) % len_x
    y_new = (pos[1]+vel[1]*t) % len_y
    return (x_new, y_new)

def count_quadrants(robots_pos, len_x, len_y, part=1):
    quadrants = [(0, 0, int((len_x-1)/2)-1, int((len_y-1)/2)-1),
    (int((len_x - 1) / 2) + 1, 0, len_x-1, int((len_y - 1) / 2) - 1),
    (0, int((len_y - 1) / 2) + 1, int((len_x - 1) / 2) - 1, len_y-1),
    (int((len_x - 1) / 2) + 1, int((len_y - 1) / 2) + 1, len_x-1, len_y-1)]


    quadrant_counts = []
    for q in quadrants:
        no_robots_in_q = 0
        for x, y in robots_pos:
            if (q[0] <= x <= q[2]) and (q[1] <= y <= q[3]):
                no_robots_in_q += 1
        quadrant_counts.append(no_robots_in_q)
    if part == 1:
        safety_factor = 1
        for q in quadrant_counts:
            safety_factor *= q
        return safety_factor
    else:
        return min(quadrant_counts) == max(quadrant_counts)

@cache
def gen_v_lines(line_len, len_x, len_y):
    vlines = []
    for x in range(len_x):
        for y0 in range(len_y-line_len-1):
            vlines.append({(x, y) for y in range(y0, y0+line_len)})
    return tuple(vlines)

def check_v_line(robots_pos, len_x, len_y, v_lines):
    for v_line in v_lines:
        if v_line.issubset(robots_pos):
            return True
    return False

def print_robots(robot_pos, len_x, len_y):
    for y in range(len_y):
        for x in range(len_x):
            if (x, y) in robot_pos:
                print("X", end="")
            else:
                print(".", end="")
        print("\n", end="")

def var(x):
    mean = sum(x)/len(x)
    return sum([(a-mean)**2 for a in x])/len(x)

def part1(input, part, example=False):

    if part == 2 and example:
        return False

    input_lines = input_to_lines(input)

    len_x = 11 if example else 101
    len_y = 7 if example else 103

    robots = []
    for line in input_lines:
        m = re.match(r"p=(\d+),(\d+) v=([-\d]+),([-\d]+)", line)
        pos = (int(m.groups()[0]), int(m.groups()[1]))
        vel = (int(m.groups()[2]), int(m.groups()[3]))
        robots.append((pos, vel))

    sim_time = 100 if part == 1 else 100000

    v_lines = gen_v_lines(30, len_x, len_y)
    print(len(v_lines))

    print("")
    robots_pos = [x[0] for x in robots]
    var_x_avg = 0
    var_y_avg = 0
    for t in range(1,1+sim_time):
        print(f"{t}s", end="\r")
        for ix, robot in enumerate(robots):
            robots_pos[ix] = robot_move(robot[0], robot[1], t, len_x, len_y)

        if part == 2:
            var_x = var([x[0] for x in robots_pos])
            var_y = var([x[1] for x in robots_pos])
            if t <= 10:
                #print(var_this)
                var_x_avg += var_x/10
                var_y_avg += var_y / 10
            if t == 10:
                print(f"var x avg: {var_x_avg}")
                print(f"var y avg: {var_y_avg}")
            if t > 10 and var_x < var_x_avg*0.7 and var_y < var_y_avg*0.7:
                print("bingo")
                print(var_x)
                print(var_y)
                print_robots(robots_pos, len_x, len_y)
                return t



    if part == 1:
        return count_quadrants(robots_pos, len_x, len_y)



if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)