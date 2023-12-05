from adventofcode.common import parse_input


input = parse_input("input")


mode = "seeds"

seeds = {}
map_source = None

input.append("")

for inline in input:
    if inline == "":
        mode = "new-mode"
        if map_source is not None:
            for seed in seeds.keys():
                source = seed if map_source == "seed" else seeds[seed][map_source]
                if map_dest not in seeds[seed].keys():
                    seeds[seed][map_dest] = source
    elif mode == "seeds":
        seeds = {int(x): {} for x in inline.split(" ")[1:]}
    elif "map" in mode:
        dest_start, source_start, map_length = [int(x) for x in inline.split(" ")]
        map_name = mode[:-4]
        map_source = map_name.split("-")[0]
        map_dest = map_name.split("-")[-1]
        for seed in seeds.keys():
            source = seed if map_source == "seed" else seeds[seed][map_source]
            if source in range(source_start, source_start+map_length):
                dest = (source-source_start)+dest_start
                seeds[seed][map_dest] = dest

    elif mode == "new-mode":
        mode = inline[:-1]


locations = [x['location'] for x in seeds.values()]

solution_part1 = min(locations)
print(solution_part1)