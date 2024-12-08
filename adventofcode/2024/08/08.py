from adventofcode.common import run, input_to_lines, input_to_grid
import math

def part1(input, part):

    grid = input_to_grid(input)

    antennas = {}
    for y, row in enumerate(grid):
        for x, symbol in enumerate(row):
            if symbol != ".":
                antennas[(x, y)] = symbol

    antennas_by_freq = {}
    for pos, freq in antennas.items():
        if freq not in antennas_by_freq.keys():
            antennas_by_freq[freq] = []
        antennas_by_freq[freq].append(pos)

    antinodes = set()
    for freq, antennas_loc in antennas_by_freq.items():
        antinodes_loc = set()
        for antenna1 in antennas_loc:
            possible_other_antennas = [x for x in antennas_loc if x != antenna1]
            for antenna2 in possible_other_antennas:
                line_vector = (antenna2[0]-antenna1[0], antenna2[1]-antenna1[1])
                if part == 1:
                    antinode_pos = (antenna1[0]+2*line_vector[0], antenna1[1]+2*line_vector[1])
                    if antinode_pos[0] >= 0 and antinode_pos[0] < len(grid[0]) and antinode_pos[1] >= 0 and antinode_pos[1] < len(grid):
                        antinodes_loc.add(antinode_pos)
                else:
                    diag_length = math.floor(math.sqrt(len(grid[0])*len(grid[0])+len(grid)*len(grid)))+1
                    for i in range(-diag_length,diag_length):
                        antinode_pos = (antenna1[0]+i*line_vector[0], antenna1[1]+i*line_vector[1])
                        if antinode_pos[0] >= 0 and antinode_pos[0] < len(grid[0]) and antinode_pos[1] >= 0 and antinode_pos[1] < len(grid):
                            antinodes_loc.add(antinode_pos)
        antinodes.update(antinodes_loc)
    return len(antinodes)

if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)