from adventofcode.common import run, input_to_grid, input_to_lines
import re

def robot_move(robot, boxes, walls, len_x, len_y, move):
    robot_x, robot_y = robot
    boxes_to_move = []
    move_it = True
    if move == "<":
        if robot_x == 1:
            return robot, boxes
        for x in list(reversed(range(0, robot_x))):
            if (x, robot_y) in boxes:
                boxes_to_move.append((x, robot_y))
            elif (x, robot_y) in walls:
                move_it = False
                break
            else:
                break
        if not move_it:
            return robot, boxes
        for box in boxes_to_move:
            del boxes[boxes.index(box)]
            boxes.append(((box[0]-1), box[1]))
        robot = (robot_x-1, robot_y)
        return robot, boxes
    if move == ">":
        if robot_x == len_x-2:
            return robot, boxes
        for x in range(robot_x+1, len_x):
            if (x, robot_y) in boxes:
                boxes_to_move.append((x, robot_y))
            elif (x, robot_y) in walls:
                move_it = False
                break
            else:
                break
        if not move_it:
            return robot, boxes
        for box in boxes_to_move:
            del boxes[boxes.index(box)]
            boxes.append(((box[0]+1), box[1]))
        robot = (robot_x+1, robot_y)
        return robot, boxes
    if move == "^":
        if robot_y == 1:
            return robot, boxes
        for y in list(reversed(range(0, robot_y))):
            if (robot_x, y) in boxes:
                boxes_to_move.append((robot_x, y))
            elif (robot_x, y) in walls:
                move_it = False
                break
            else:
                break
        if not move_it:
            return robot, boxes
        for box in boxes_to_move:
            del boxes[boxes.index(box)]
            boxes.append(((box[0]), box[1]-1))
        robot = (robot_x, robot_y-1)
        return robot, boxes
    if move == "v":
        if robot_y == len_y-2:
            return robot, boxes
        for y in range(robot_y+1, len_y):
            if (robot_x, y) in boxes:
                boxes_to_move.append((robot_x, y))
            elif (robot_x, y) in walls:
                move_it = False
                break
            else:
                break
        if not move_it:
            return robot, boxes
        for box in boxes_to_move:
            del boxes[boxes.index(box)]
            boxes.append(((box[0]), box[1]+1))
        robot = (robot_x, robot_y+1)
        return robot, boxes

def movable(pos, boxes, walls, move, robot = True):
    x, y = pos
    boxes_map = {**{(x+1, y): (x, y) for x, y in boxes}, **{(x, y): (x, y) for x, y in boxes}}
    boxes_pad = [(x+1, y) for x, y in boxes]
    boxes_check = [*boxes, *boxes_pad]
    if move == "<":
        check_poss = [(x-1, y)]
    elif move == ">":
        if robot:
            check_poss = [(x + 1, y)]
        else:
            check_poss = [(x+2, y)]
    elif move == "v":
        if robot:
            check_poss = [(x, y + 1)]
        else:
            check_poss = [(x, y+1), (x+1, y+1)]
    else:
        if robot:
            check_poss = [(x, y - 1)]
        else:
            check_poss = [(x, y - 1), (x+1, y - 1)]
    ret = {(x, y)}
    for check_pos in check_poss:
        if check_pos in walls:
            return {}
        elif check_pos in boxes_check:
            box_movable = movable(boxes_map[check_pos], boxes, walls, move, False)
            if len(box_movable) == 0:
                return {}
            else:
                ret = {*ret, *box_movable}
    return ret

def robot_move2(robot, boxes, walls, move):
    boxes_to_move = movable(robot, boxes, walls, move)
    new_robot = robot
    if len(boxes_to_move) > 0:
        for box in boxes_to_move:
            #print(boxes_to_move)
            x, y = box
            if move == "<":
                new_pos = (x - 1, y)
            elif move == ">":
                new_pos = (x + 1, y)
            elif move == "v":
                new_pos = (x, y + 1)
            else:
                new_pos = (x, y - 1)
            if box == robot:
                new_robot = new_pos
            else:
                del boxes[boxes.index(box)]
                boxes.append(new_pos)
    return new_robot, boxes

def boxes_gps(boxes):
    res = 0
    for box in boxes:
        res += 100*box[1]+box[0]
    return res

def print_it(robot, boxes, walls, len_x, len_y):
    for y in range(len_y):
        for x in range(len_x):
            if (x, y) in boxes:
                print("O", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print("\n", end="")

def print_it2(robot, boxes, walls, len_x, len_y):
    boxes_pad = [(x+1, y) for x, y in boxes]
    for y in range(len_y):
        for x in range(len_x):
            if (x, y) in boxes:
                print("[", end="")
            elif (x, y) in boxes_pad:
                print("]", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print("\n", end="")

def puzzle(input, part, example=False, *args, **kwargs):

    in_grid = True
    moves = []
    boxes = []
    walls = []
    robot = (0,0)
    len_x = 0
    len_y = 0
    for line in input_to_lines(input):
        if line == "":
            in_grid = False
        if not in_grid:
            moves.extend(list(line))
        else:
            len_y += 1
            len_x = len(line)
            for x, v in enumerate(list(line)):
                if v == "O":
                    boxes.append((x, len_y-1))
                if v == "@":
                    robot = (x, len_y-1)
                if v == "#":
                    walls.append((x, len_y-1))

    for move in moves:
        robot, boxes = robot_move(robot, boxes, walls, len_x, len_y, move)
        #print(f"Move {move}:")
        #print_it(robot, boxes, walls, len_x, len_y)

    return boxes_gps(boxes)

def puzzle2(input, part, example=False, *args, **kwargs):

    in_grid = True
    moves = []
    boxes = []
    walls = []
    robot = (0,0)
    len_x = 0
    len_y = 0
    for line in input_to_lines(input):
        if line == "":
            in_grid = False
        if not in_grid:
            moves.extend(list(line))
        else:
            len_y += 1
            len_x = len(line)*2
            x = 0
            for _, v in enumerate(list(line)):
                if v == "O":
                    boxes.append((x, len_y-1))
                if v == "@":
                    robot = (x, len_y-1)
                if v == "#":
                    walls.append((x, len_y-1))
                    walls.append((x+1, len_y - 1))
                x += 2

    for move in moves:
        robot, boxes = robot_move2(robot, boxes, walls, move)
        #print(f"Move {move}:")
        #print_it2(robot, boxes, walls, len_x, len_y)

    return boxes_gps(boxes)

if __name__ == '__main__':
    run(cb1=puzzle)
    run(cb2=puzzle2)