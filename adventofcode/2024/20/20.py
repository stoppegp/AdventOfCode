from adventofcode.common import run, input_to_grid, input_to_lines
import re
from functools import cache
from tqdm import tqdm

steps = {complex(0,1), complex(1,0), complex(0,-1), complex(-1,0)}

def puzzle(input, part=1, example=False, *args, **kwargs):

    def get_neighbors(walls, current_node, grid):
        nbs = set()
        for step in steps:
            next_node = current_node+step
            if next_node in grid and next_node not in walls:
                nbs.add(next_node)
        return nbs

    def find_path(walls, start, target, grid):
        cost = {x: None for x in grid}
        prev = {x: set() for x in grid}
        cost[start] = 0
        queue = [start]
        visited = []


        while len(queue) > 0:
            current_node = queue[0]
            del queue[0]
            if current_node == target:
                return cost[current_node], cost, prev
            visited.append(current_node)

            for neighbor in get_neighbors(walls, current_node, grid):
                if neighbor in visited:
                    continue
                new_cost = cost[current_node] + 1
                if cost[neighbor] is None or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    prev[neighbor] = current_node
                queue.append(neighbor)
        raise Exception()

    lines = input_to_grid(input)

    walls = set()
    start = None
    end = None
    grid = set()

    for y, row in enumerate(lines):
        for x, v in enumerate(row):
            grid.add(complex(x,y))
            if v == "#":
                walls.add(complex(x, y))
            if v == "S":
                start = complex(x, y)
            if v == "E":
                end = complex(x, y)

    def get_path(start, end, prev, walls):
        current_node = end
        all_nodes = {end}
        while current_node != start:
            current_node = prev[current_node]
            all_nodes.add(current_node)
        return all_nodes

    base_time, base_cost, prev = find_path(walls, end, start, grid)
    path_tiles = get_path(end, start, prev, walls)

    saved_times = []

    cheat_length = 2 if part == 1 else 20

    @cache
    def get_cheat_ends(start, cheat_length):
        possible_ends = set()
        for step in steps:
            if start+step not in grid:
                continue
            if start+step not in walls:
                possible_ends.add(start+step)
            if cheat_length > 1:
                possible_ends.update(get_cheat_ends(start+step, cheat_length-1))
        return possible_ends

    for tile in tqdm(path_tiles):
        cost0 = base_cost[tile]
        possible_ends = get_cheat_ends(tile, cheat_length)
        for possible_end in possible_ends:
            cheat_length_loc = abs((possible_end-tile).real) + abs((possible_end-tile).imag)
            cost1 = base_cost[possible_end]+cheat_length_loc
            saved_times.append(max(cost0 - cost1, 0))
    if example and part == 1:
        return saved_times.count(4)
    elif example and part == 2:
        return len([x for x in saved_times if x >= 50])
    else:
        return len([x for x in saved_times if x >= 100])



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)