from adventofcode.common import run, input_to_grid, input_to_lines
import re
import pickle

def get_neighbors(grid, pos):
    nbs = {}
    if pos[2] == ">":
        if grid[pos[1]-1][pos[0]] != "#":
            nbs[((pos[0], pos[1], "^"))] = 1000
        if grid[pos[1] + 1][pos[0]] != "#":
            nbs[((pos[0], pos[1], "v"))] = 1000
        if grid[pos[1]][pos[0]+1] != "#":
            nbs[((pos[0]+1, pos[1], pos[2]))] = 1
    elif pos[2] == "v":
        if grid[pos[1]][pos[0]-1] != "#":
            nbs[((pos[0], pos[1], "<"))] = 1000
        if grid[pos[1]][pos[0]+1] != "#":
            nbs[((pos[0], pos[1], ">"))] = 1000
        if grid[pos[1]+1][pos[0]] != "#":
            nbs[((pos[0], pos[1]+1, pos[2]))] = 1
    elif pos[2] == "<":
        if grid[pos[1] - 1][pos[0]] != "#":
            nbs[((pos[0], pos[1], "^"))] = 1000
        if grid[pos[1] + 1][pos[0]] != "#":
            nbs[((pos[0], pos[1], "v"))] = 1000
        if grid[pos[1]][pos[0] - 1] != "#":
            nbs[((pos[0]-1, pos[1], pos[2]))] = 1
    elif pos[2] == "^":
        if grid[pos[1]][pos[0]-1] != "#":
            nbs[((pos[0], pos[1], "<"))] = 1000
        if grid[pos[1]][pos[0]+1] != "#":
            nbs[((pos[0], pos[1], ">"))] = 1000
        if grid[pos[1]-1][pos[0] ] != "#":
            nbs[((pos[0], pos[1]-1, pos[2]))] = 1
    return nbs


def find_path(grid, start, targets):
    cost = {(x, y, dir): None for x in range(len(grid[0])) for y in range(len(grid)) for dir in [">", "^", "<", "v"]}
    prev = {(x, y, dir): [] for x in range(len(grid[0])) for y in range(len(grid)) for dir in [">", "^", "<", "v"]}
    cost[(start[0], start[1], ">")] = 0
    queue = {(start[0], start[1], ">"): 0}
    to_visit_targets = [*targets]
    visited = []

    while len(queue) > 0:
        current_node = min(queue, key=queue.get)
        del queue[current_node]
        visited.append(current_node)
        if current_node in to_visit_targets:
            del to_visit_targets[to_visit_targets.index(current_node)]

        for neighbor, inc_val in get_neighbors(grid, current_node).items():
            if neighbor in visited:
                continue
            new_cost = cost[current_node] + inc_val
            if cost[neighbor] is None or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                prev[neighbor] = [current_node]
            elif new_cost == cost[neighbor]:
                prev[neighbor].append(current_node)
            queue[neighbor] = cost[neighbor]

        if len(to_visit_targets) == 0:
            break
    return cost, prev


def get_best_path(end, prev):
    ret = [end]
    for x in prev[end]:
        ret.extend(get_best_path(x, prev))
    return ret

def puzzle(input, part, example=False, *args, **kwargs):
    grid = input_to_grid(input)
    start = ()
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == "S":
                start = (x, y)
            if v == "E":
                target = (x, y)

    cost, prev = find_path(grid, start, [(target[0], target[1], ">"), (target[0], target[1], "^")])
    min_cost = min([v for k, v in cost.items() if k[0] == target[0] and k[1] == target[1]])
    if part == 1:
        return min_cost
    else:
        targets_suc = [k for k, v in cost.items() if k[0] == target[0] and k[1] == target[1] and v == min_cost]
        best_tiles0 = {}
        for target_suc in targets_suc:
            best_tiles0 = {*best_tiles0, *get_best_path(target_suc, prev)}
        best_tiles = {(x, y) for x, y, dir in best_tiles0}
        return len(best_tiles)


if __name__ == '__main__':
    run(cb1=puzzle)
    run(cb2=puzzle)