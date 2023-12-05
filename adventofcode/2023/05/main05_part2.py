from adventofcode.common import parse_input



input = parse_input("input")

mode = "seeds"

main_table = {'seed': []}
map_source = None

input.append("")

for inline in input:
    if inline == "":
        mode = "new-mode"
        if map_source is not None:
            for ix, source_range in enumerate(main_table[map_source]):
                if source_range is None:
                    continue
                main_table[map_dest].append(source_range)
    elif mode == "seeds":
        seeds_raw = [int(x) for x in inline.split(" ")[1:]]
        for i in range(0, int(len(seeds_raw)/2)):
            seedno_start = 2*i
            main_table['seed'].append(range(seeds_raw[seedno_start], seeds_raw[seedno_start]+seeds_raw[seedno_start+1]))
    elif "map" in mode:
        dest_start, source_start, map_length = [int(x) for x in inline.split(" ")]
        map_name = mode[:-4]
        map_source = map_name.split("-")[0]
        map_dest = map_name.split("-")[-1]
        if map_dest not in main_table.keys():
            main_table[map_dest] = []
        print(f"MAP FROM: {map_source} TO: {map_dest}")
        print(f"MAP DEST START: {dest_start}, SOURCE START: {source_start}, LENGHT: {map_length}")
        for ix, source_range in enumerate(main_table[map_source]):
            print("source: " + str(source_range))
            if source_range is None:
                continue
            inters = range(max(source_range.start, source_start), min(source_range.stop, source_start+map_length)) or None
            print("inters: " + str(inters))
            if inters is not None:
                destmap_start = inters.start-source_start+dest_start
                destrange = range(destmap_start, destmap_start+len(inters))
                print("destrange: " + str(destrange))
                main_table[map_dest].append(destrange)
                main_table[map_source][ix] = None
                if inters.start > source_range.start:
                    padding_map1 = range(source_range.start, inters.start)
                    main_table[map_source].append(padding_map1)
                if inters.stop < source_range.stop:
                    padding_map2 = range(inters.stop, source_range.stop)
                    main_table[map_source].append(padding_map2)

    elif mode == "new-mode":
        mode = inline[:-1]


solution_part2 = min([x.start for x in main_table['location']])
print(solution_part2)