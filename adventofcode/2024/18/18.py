from adventofcode.common import run, input_to_grid, input_to_lines
import re

def puzzle(input, part=1, example=False, *args, **kwargs):

    if example:
        len_x = 7
        len_y = 7
    else:
        len_x = 71
        len_y = 71

    lines = input_to_lines(input)

    corrupted_base = []

    for ix, line in enumerate(lines):
        corrupted_base.append((int(line.split(",")[0]), int(line.split(",")[1])))

    def get_neighbors(corrupted, current_node, len_x, len_y):
        x,y = current_node
        pb = set()
        if x > 0 and (x-1, y) not in corrupted:
            pb.add((x-1, y))
        if y > 0 and (x, y-1) not in corrupted:
            pb.add((x, y-1))
        if x < len_x-1 and (x+1, y) not in corrupted:
            pb.add((x+1, y))
        if y < len_y-1 and (x, y+1) not in corrupted:
            pb.add((x, y+1))
        return pb

    def find_path(corrupted, start, target, len_x, len_y):
        cost = {(x, y): None for x in range(len_x) for y in range(len_y)}
        #prev = {(x, y): set() for x in range(len_x) for y in range(len_y)}
        cost[start] = 0
        #prev[start] = {None}
        queue = {start: 0}
        #to_visit_targets = [target]
        visited = []

        no_iter = 0

        while len(queue) > 0:
            no_iter += 1
            current_node = min(queue, key=queue.get)
            if current_node == target:
                return cost[current_node]
            del queue[current_node]
            visited.append(current_node)
            #if current_node in to_visit_targets:
#                del to_visit_targets[to_visit_targets.index(current_node)]

            for neighbor in get_neighbors(corrupted, current_node, len_x, len_y):
                if neighbor in visited:
                    continue
                new_cost = cost[current_node] + 1
                if cost[neighbor] is None or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                queue[neighbor] = cost[neighbor]
        raise Exception()

    if part == 1:
        if example:
            corrupted = corrupted_base[:12]
        else:
            corrupted = corrupted_base[:1024]
        cost = find_path(corrupted, (0,0), (len_x-1, len_y-1), len_x, len_y)
        print(cost)
        return cost

    elif part == 2:
        if example:
            max_byte_no = 12
        else:
            max_byte_no = 1700
        for i in list(reversed(range(max_byte_no, len(corrupted_base)))):
            try:
                cost = find_path(corrupted_base[:i], (0,0), (len_x-1, len_y-1), len_x, len_y)
                return f"{corrupted_base[i][0]},{corrupted_base[i][1]}"
            except:
                pass



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1", part=1)
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)
