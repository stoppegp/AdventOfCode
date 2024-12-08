from adventofcode.common import parse_input
from copy import deepcopy
from tqdm import tqdm

input = parse_input("input")

class OutOfBoundsError(Exception):
    pass

def get_grid(input, pos):
    x = pos[0]
    y = pos[1]
    if x >= len(input[0]) or y >= len(input) or x < 0 or y < 0:
        raise OutOfBoundsError()
    return input[y][x]

def rotate_right(guard_dir):
    if guard_dir == (0, -1):
        return (1, 0)
    if guard_dir == (1, 0):
        return (0, 1)
    if guard_dir == (0, 1):
        return (-1, 0)
    if guard_dir == (-1, 0):
        return (0, -1)

def move(input, guard_pos, guard_dir):
    guard_new_pos = (guard_pos[0]+guard_dir[0], guard_pos[1]+guard_dir[1])
    new_pos_element = get_grid(input, guard_new_pos)
    while new_pos_element == "#":
        guard_dir = rotate_right(guard_dir)
        guard_new_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        new_pos_element = get_grid(input, guard_new_pos)
    return guard_new_pos, guard_dir

len_x = len(input[0])
len_y = len(input)

guard_pos_start = (0,0)
guard_dir_start = (0, -1)
for y in range(len_y):
    for x in range(len_x):
        if input[y][x] == "^":
            guard_pos_start = (x, y)

# part 1
visited = set()
guard_pos = guard_pos_start
guard_dir = guard_dir_start
visited.add(guard_pos)
try:
    while True:
        guard_pos, guard_dir = move(input, guard_pos, guard_dir)
        visited.add(guard_pos)
except OutOfBoundsError:
    print(len(visited))

no_possibilities = 0
for ix, (x, y) in tqdm(enumerate(visited)):
    guard_pos = guard_pos_start
    guard_dir = guard_dir_start
    visited_loc = set()
    visited_loc.add((*guard_pos, *guard_dir))

    input_mod = deepcopy(input)
    if input_mod[y][x] != ".":
        continue
    temp = list(input_mod[y])
    temp[x] = "#"
    input_mod[y] = temp

    try:
        while True:
            guard_pos, guard_dir = move(input_mod, guard_pos, guard_dir)
            if (*guard_pos, *guard_dir) in visited_loc:
                no_possibilities += 1
                break
            visited_loc.add((*guard_pos, *guard_dir))
    except OutOfBoundsError:
        pass
print(no_possibilities)

