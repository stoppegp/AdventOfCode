from adventofcode.common import run, input_to_grid, input_to_lines
import re
import math
from tqdm import tqdm

def puzzle(input, part=1, example=False, *args, **kwargs):



    def next_secret_no(no):
        a = (no ^ (no*64)) % 16777216
        b = (a ^ int(a / 32)) % 16777216
        return (b ^ (b * 2048)) % 16777216

    def get_sequences(secret_prizes_diffs):
        return {tuple(secret_prizes_diffs[i:i+4]) for i in range(len(secret_prizes_diffs)-4)}

    def get_all_sequences(secret_prizes_all_diffs):
        seqs = set()
        for i in range(len(secret_prizes_all_diffs)):
            seqs.update(get_sequences(secret_prizes_all_diffs[i]))
        return seqs

    def create_seq_lookup(secret_prizes, secret_prizes_diffs):
        ret = {}
        for i in range(len(secret_prizes_diffs)-4):
            seq = tuple(secret_prizes_diffs[i:i+4])
            if seq not in ret.keys():
                ret[seq] = secret_prizes[i+4]
        return ret

    def get_prizes_sum(secret_prizes_all_lookup, seq):
        prizes_sum = 0
        for i in range(len(secret_prizes_all_diffs)):
            if seq in secret_prizes_all_lookup[i].keys():
                prizes_sum += secret_prizes_all_lookup[i][seq]
        return prizes_sum

    lines = input_to_lines(input)

    secret_numbers_all = [[int(x)] for ix, x in enumerate(lines)]

    for ix, no0 in enumerate(secret_numbers_all):
        no = no0[0]
        for i in range(2000):
            no = next_secret_no(no)
            secret_numbers_all[ix].append(no)
    if part == 1:
        return sum([x[-1] for x in secret_numbers_all])

    secret_prizes_all = [[] for i in range(len(secret_numbers_all))]
    for ix, secret_numbers in enumerate(secret_numbers_all):
        secret_prizes_all[ix] = [secret_numbers[i]%10 for i in range(len(secret_numbers))]

    secret_prizes_all_diffs = [[] for i in range(len(secret_numbers_all))]
    for ix, secret_prizes in enumerate(secret_prizes_all):
        secret_prizes_all_diffs[ix] = [secret_prizes[i] - secret_prizes[i-1] for i in range(len(secret_prizes)) if i > 0]

    secret_prizes_all_lookup = [[] for i in range(len(secret_numbers_all))]
    for ix, secret_prizes in enumerate(secret_prizes_all):
        secret_prizes_all_lookup[ix] = create_seq_lookup(secret_prizes_all[ix], secret_prizes_all_diffs[ix])


    seqs = get_all_sequences(secret_prizes_all_diffs)

    max_earn = 0
    max_seq = ""
    for seq in tqdm(seqs):
        max_earn_loc = get_prizes_sum(secret_prizes_all_lookup, seq)
        if max_earn_loc > max_earn:
            max_seq = seq
        max_earn = max(max_earn, max_earn_loc)
    print(max_seq)
    return max_earn

if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example2", solution_file="solution2", part=2)