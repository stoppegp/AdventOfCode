from adventofcode.common import run, input_to_lines, input_to_grid
import math

def checksum(file_pos):
    cs = 0
    for ix, val in enumerate(file_pos):
        if val != False:
            cs += ix*val
    return cs

def checksum2(file_pos):
    cs = 0
    for file_id, file_block in file_pos.items():
        for i in range(file_block[0], file_block[0]+file_block[1]):
            cs += i*file_id
    return cs

def fb_repr(file_block):
    repr = []
    for file_id, (file_pos, file_len) in file_block.items():
        file_end = file_pos + file_len -1
        while file_end >= len(repr):
            repr.extend(["."])
        for i in range(file_pos, 1+file_end):
            repr[i] = str(file_id)
    #print(repr)
    return "".join(repr)

def part1(input, part):

    free_pos = []
    file_pos = []

    current_pos = 0
    file_id = 0
    is_file = True
    for val_str in input:
        val = int(val_str)
        if is_file:
            file_pos.extend([file_id]*val)
            is_file = False
            file_id += 1

        else:
            free_pos.extend(list(range(current_pos, current_pos+val)))
            file_pos.extend([False] * val)
            is_file = True
        current_pos += val

    #print(file_pos)
    #print(free_pos)

    while len(free_pos) > 0:
        #print(free_pos)
        next_free = free_pos[0]
        for ix, val in enumerate(reversed(file_pos)):
            if val != False:
                next_val = val
                next_ix = len(file_pos)-ix-1
                break
        if next_ix <= next_free:
            break
        file_pos[next_free] = next_val
        file_pos[next_ix] = False
        del free_pos[0]
        free_pos.append(next_ix)
        free_pos.sort()
    return checksum(file_pos)

def part2(input, part):

    free_pos = []
    file_pos = {}

    current_pos = 0
    file_id = 0
    is_file = True
    for val_str in input:
        val = int(val_str)
        if is_file:
            #file_pos.extend([file_id]*val)
            file_pos[file_id] = (current_pos, val)
            is_file = False
            file_id += 1

        else:
            free_pos.extend(list(range(current_pos, current_pos+val)))
            #file_pos.extend([False] * val)
            is_file = True
        current_pos += val

    print(file_pos)
    print(free_pos)
    print(fb_repr(file_pos))


    for i, file_block in enumerate(reversed(file_pos.values())):
        file_id = list(file_pos.keys())[len(file_pos)-i-1]
        file_block_len = file_block[1]

        #print(file_id)
        #print(file_block_len)

        next_free = free_pos[0]
        next_free_len = 1
        for v in free_pos[1:]:
            if next_free_len >= file_block_len:
                break
            if v == next_free+next_free_len:
                next_free_len += 1
            else:
                next_free = v
                next_free_len = 1
            if next_free_len >= file_block_len:
                break
        #print(next_free_len)
        #print(next_free)

        if file_block_len <= next_free_len and next_free < file_block[0]:
            file_pos[file_id] = (next_free, file_block_len)
            for i in range(next_free, next_free+file_block_len):
                #print(i)
                del_index = free_pos.index(i)
                del free_pos[del_index]
            free_pos.extend(list(range(file_block[0], file_block[0]+file_block_len)))
        free_pos.sort()
        #print(fb_repr(file_pos))
        #print(free_pos)
        #print()

    return checksum2(file_pos)

if __name__ == '__main__':
    #run(cb1=part1)
    run(cb2=part2)