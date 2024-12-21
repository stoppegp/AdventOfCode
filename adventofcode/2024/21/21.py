from adventofcode.common import run, input_to_grid, input_to_lines
import re
from functools import cache


def puzzle(input, part=1, example=False, *args, **kwargs):

    state = ("A", "A", "A", "A")

    ctl_pad_keys = {"<", ">", "^", "v", "A"}
    num_pad_keys = {"A", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    @cache
    def get_next_num_pad_key(current, key):
        if key == "A":
            return current
        if current == "A":
            if key in [">", "v"]:
                return None
            elif key == "<":
                return "0"
            elif key == "^":
                return "3"
        if current == "0":
            if key in ["<", "v"]:
                return None
            elif key == ">":
                return "A"
            elif key == "^":
                return "2"
        if current == "1":
            if key in ["<", "v"]:
                return None
            elif key == ">":
                return "2"
            elif key == "^":
                return "4"
        if current == "2":
            if key == "<":
                return "1"
            elif key == ">":
                return "3"
            elif key == "v":
                return "0"
            elif key == "^":
                return "5"
        if current == "3":
            if key == "<":
                return "2"
            elif key == ">":
                return None
            elif key == "v":
                return "A"
            elif key == "^":
                return "6"
        if current == "4":
            if key == "<":
                return None
            elif key == ">":
                return "5"
            elif key == "v":
                return "1"
            elif key == "^":
                return "7"
        if current == "5":
            if key == "<":
                return "4"
            elif key == ">":
                return "6"
            elif key == "v":
                return "2"
            elif key == "^":
                return "8"
        if current == "6":
            if key == "<":
                return "5"
            elif key == ">":
                return None
            elif key == "v":
                return "3"
            elif key == "^":
                return "9"
        if current == "7":
            if key == "<":
                return None
            elif key == ">":
                return "8"
            elif key == "v":
                return "4"
            elif key == "^":
                return None
        if current == "8":
            if key == "<":
                return "7"
            elif key == ">":
                return "9"
            elif key == "v":
                return "5"
            elif key == "^":
                return None
        if current == "9":
            if key == "<":
                return "8"
            elif key == ">":
                return None
            elif key == "v":
                return "6"
            elif key == "^":
                return None

    @cache
    def get_next_ctl_pad_key(current, key):
        if key == "A":
            return current
        if current == "<":
            if key != ">":
                return None
            else:
                return "v"
        if current == ">":
            if key in [">", "v"]:
                return None
            elif key == "^":
                return "A"
            else:
                return "v"
        if current == "^":
            if key in ["<", "^"]:
                return None
            elif key == ">":
                return "A"
            else:
                return "v"
        if current == "v":
            if key in ["v"]:
                return None
            elif key == ">":
                return ">"
            elif key == "<":
                return "<"
            else:
                return "^"
        if current == "A":
            if key in [">", "^"]:
                return None
            elif key == "<":
                return "^"
            else:
                return ">"

    def get_neighbors(current_node):
        nbs = set()
        for key in ctl_pad_keys:
            key1 = key
            key2 = get_next_ctl_pad_key(current_node[1], key1)

            if current_node[1] == "A" and current_node[2] == "A" and key == "A":
                pass

            if key2 is None:
                continue

            if key1 == "A":
                key3 = get_next_ctl_pad_key(current_node[2], key2)
            else:
                key3 = current_node[2]
            if key3 is None:
                continue
            if key1 == "A" and key2 == "A":
                key4 = get_next_num_pad_key(current_node[3], key3)
            else:
                key4 = current_node[3]
            if key4 is None:
                continue
            nbs.add((key1, key2, key3, key4))
        return nbs

    def find_path(start, target_num):
        cost = {}
        prev = {}
        cost[start] = 0
        queue = [start]
        visited = []

        target = ("A", "A", "A", target_num)

        while len(queue) > 0:
            current_node = queue[0]
            del queue[0]
            #if current_node in targets:
                #return cost[current_node], cost, prev
            visited.append(current_node)
            if current_node == target:
                return cost[current_node], prev[current_node]


            for neighbor in get_neighbors(current_node):
                if neighbor in visited:
                    continue
                new_cost = cost[current_node] + 1
                if neighbor not in cost.keys() or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    prev[neighbor] = current_node
                queue.append(neighbor)
        raise Exception()



    s = "029A"

    def get_path(end, prev):
        path = end[0]
        while end in prev.keys():
            path = prev[end][0] + path
            end = prev[end]
        return(path)

    def get_full_path(end, prev):
        path = str(end)
        while end in prev.keys():
            path = str(prev[end]) + "\n" + path
            end = prev[end]
        return(path)



    def get_num_presses(seq):
        full_cost = 0
        start = state
        for y in list(seq):
            min_cost, prev = find_path(start, y)
            start = ("A", "A", "A", y)
            full_cost += min_cost
        print(f"{seq}: {full_cost}")
        return full_cost

    lines = input_to_lines(input)
    final_sum = 0
    for seq in lines:
        cost = get_num_presses(seq)
        final_sum += int(seq.replace("A", "")) * cost

    return final_sum



if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")