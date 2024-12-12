from adventofcode.common import run, input_to_grid



def part1(input, part):

    areas = []

    grid = input_to_grid(input)
    rows_no = len(grid)
    cols_no = len(grid[0])

    def get_next_points(point):
        x, y = point
        ret = []
        if x > 0:
            ret.append((x-1, y))
        if y > 0:
            ret.append((x, y-1))
        if x < cols_no-1:
            ret.append((x+1, y))
        if y < rows_no-1:
            ret.append((x, y+1))
        return ret

    def find_area(start_point, v, current_area, grid):
        next_points = get_next_points(start_point)
        for next_point in next_points:
            if next_point in current_area:
                continue
            x, y = next_point
            if grid[y][x] == v:
                current_area.add(next_point)
                current_area.update(find_area(next_point, v, current_area, grid))
        return current_area

    def get_perimeter(area, grid):
        rows_no = len(grid)
        cols_no = len(grid[0])
        perimeter = 0
        for x, y in area:
            if x == 0 or (x-1, y) not in area:
                perimeter += 1
            if y == 0 or (x, y-1) not in area:
                perimeter += 1
            if x == cols_no-1 or (x+1, y) not in area:
                perimeter += 1
            if y == rows_no-1 or (x, y+1) not in area:
                perimeter += 1
        return perimeter

    def get_no_sides(area, grid):
#        print(area)
        rows_no = len(grid)
        cols_no = len(grid[0])
        no_corners = 0

        def is_left_edge(x, y):
            return x == 0 or (x-1, y) not in area
        def is_top_edge(x, y):
            return y == 0 or (x, y-1) not in area
        def is_right_edge(x, y):
            return x == cols_no-1 or (x+1, y) not in area
        def is_bottom_edge(x, y):
            return y == rows_no-1 or (x, y+1) not in area
        def is_inner_corner_bl(x, y):
            if x == 0:
                return False
            if y == rows_no-1:
                return False
            if (x-1, y+1) not in area and (x-1, y) in area and (x, y+1) in area:
                return True
            return False

        def is_inner_corner_br(x, y):
            if x == cols_no-1:
                return False
            if y == rows_no-1:
                return False
            if (x + 1, y + 1) not in area and (x + 1, y) in area and (x, y + 1) in area:
                return True
            return False

        def is_inner_corner_tr(x, y):
            if x == cols_no-1:
                return False
            if y == 0:
                return False
            if (x + 1, y - 1) not in area and (x + 1, y) in area and (x, y - 1) in area:
                return True
            return False

        def is_inner_corner_tl(x, y):
            if x == 0:
                return False
            if y == 0:
                return False
            if (x - 1, y - 1) not in area and (x - 1, y) in area and (x, y - 1) in area:
                return True
            return False



        for x, y in area:
            # print(f"{x}|{y}")
            # print(is_left_edge(x, y))
            # print(is_top_edge(x, y))
            # print(is_right_edge(x, y))
            # print(is_bottom_edge(x, y))
            if is_left_edge(x, y) and is_top_edge(x, y):
                no_corners += 1
            if is_left_edge(x, y) and is_bottom_edge(x, y):
                no_corners += 1
            if is_right_edge(x, y) and is_top_edge(x, y):
                no_corners += 1
            if is_right_edge(x, y) and is_bottom_edge(x, y):
                no_corners += 1

            if is_inner_corner_bl(x, y):
                no_corners += 1
            if is_inner_corner_br(x, y):
                no_corners += 1
            if is_inner_corner_tl(x, y):
                no_corners += 1
            if is_inner_corner_tr(x, y):
                no_corners += 1
            #print(no_corners)

        return no_corners


    to_check = {(x, y) for y in range(rows_no) for x in range(cols_no)}

    while len(to_check) > 0:
        start_point = list(to_check)[0]
        x, y = start_point
        v = grid[y][x]
        new_area = find_area(start_point, v, {start_point}, grid)
        areas.append(new_area)
        to_check = to_check - new_area
        if len(to_check) == 0:
            break

    result_sum = 0

    for area in areas:
        if part == 1:
            result_sum += len(area)*get_perimeter(area, grid)
        else:
            no_sides = get_no_sides(area, grid)
            result_sum += len(area) * no_sides

    return result_sum


if __name__ == '__main__':
    run(cb1=part1)
    run(cb2=part1)