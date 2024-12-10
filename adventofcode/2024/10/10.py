from adventofcode.common import run, input_to_lines, input_to_grid
import math


def peaks_from_here(grid, pos, grid_scores, skip_storage = False):
    x, y = pos
    if grid_scores[y][x] is not None and skip_storage == False:
        return grid_scores[y][x]
    val = grid[y][x]
    if val == 9:
        grid_scores[y][x] = [pos]
        return {pos}
    peaks = set()
    # up
    if y > 0 and grid[y-1][x] == val+1:
        peaks.update(peaks_from_here(grid, (x, y-1), grid_scores, skip_storage))
    #left
    if x > 0 and grid[y][x-1] == val+1:
        peaks.update(peaks_from_here(grid, (x-1, y), grid_scores, skip_storage))
    # down
    if y < len(grid)-1 and grid[y+1][x] == val+1:
        peaks.update(peaks_from_here(grid, (x, y+1), grid_scores, skip_storage))
    # right
    if x < len(grid[0]) - 1 and grid[y][x+1] == val+1:
        peaks.update(peaks_from_here(grid, (x+1, y), grid_scores, skip_storage))
    grid_scores[y][x] = list(peaks)
    return peaks

def trails_from_here(grid, pos, grid_scores, skip_storage = False):
    x, y = pos
    if grid_scores[y][x] is not None and skip_storage == False:
        return grid_scores[y][x]
    val = grid[y][x]
    if val == 9:
        grid_scores[y][x] = 1
        return 1
    trails = 0
    # up
    if y > 0 and grid[y-1][x] == val+1:
        trails += trails_from_here(grid, (x, y-1), grid_scores, skip_storage)
    #left
    if x > 0 and grid[y][x-1] == val+1:
        trails += trails_from_here(grid, (x-1, y), grid_scores, skip_storage)
    # down
    if y < len(grid)-1 and grid[y+1][x] == val+1:
        trails += trails_from_here(grid, (x, y+1), grid_scores, skip_storage)
    # right
    if x < len(grid[0]) - 1 and grid[y][x+1] == val+1:
        trails += trails_from_here(grid, (x+1, y), grid_scores, skip_storage)
    grid_scores[y][x] = trails
    return trails

def part1(input, part):
    grid = input_to_grid(input)
    grid = [[int(y) for y in x] for x in grid]

    trailheads = []

    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == 0:
                trailheads.append((x, y))
    print(trailheads)

    grid_scores = [[None for y in x] for x in grid]
    grid_scores2 = [[None for y in x] for x in grid]

    sum = 0
    for x, y in trailheads:
        if part == 1:
            peaks_from_here(grid, (x, y), grid_scores, True)
            sum += len(grid_scores[y][x])
        else:
            trails_from_here(grid, (x, y), grid_scores2, True)
            sum += grid_scores2[y][x]
    return sum

if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)