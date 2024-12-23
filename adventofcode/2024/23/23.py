from adventofcode.common import run, input_to_grid, input_to_lines
import re


def puzzle(input, part=1, example=False, *args, **kwargs):

    connections = []
    all_pcs = {}
    lines = input_to_lines(input)
    for line in lines:
        pcs = line.split("-")
        pc0 = pcs[0]
        pc1 = pcs[1]
        connections.append({pc0, pc1})

        if pc0 not in all_pcs.keys():
            all_pcs[pc0] = set()
        if pc1 not in all_pcs.keys():
            all_pcs[pc1] = set()
        all_pcs[pc0].add(pc1)
        all_pcs[pc1].add(pc0)

    triplets = set()
    for pc0 in all_pcs.keys():
        for pc1 in all_pcs.keys():
            if pc1 in all_pcs[pc0]:
                for pc2 in all_pcs.keys():
                    if pc2 in all_pcs[pc1] and pc2 in all_pcs[pc0]:
                        triplets.add(frozenset([pc0, pc1, pc2]))

    def expand_clusters(clusters, all_pcs):
        new_clusters = set()
        for cluster in clusters:
            new_set = None
            for pc in cluster:
                if new_set is None:
                    new_set = all_pcs[pc]
                else:
                    new_set = new_set.intersection(all_pcs[pc])
            for new_pc in new_set:
                new_clusters.add(frozenset([*cluster, new_pc]))
        return new_clusters

    if part == 1:
        return len([x for x in triplets if list(x)[0][0] == "t" or list(x)[1][0] == "t" or list(x)[2][0] == "t"])

    clusters = triplets
    while True:
        new_clusters = expand_clusters(clusters, all_pcs)
        if len(new_clusters) > 0:
            clusters = new_clusters
        else:
            break

    if len(clusters) == 1:
        return ",".join(sorted(list(clusters)[0]))
    else:
        raise Exception()


if __name__ == '__main__':
    run(cb=puzzle, example_file="example", solution_file="solution1")
    run(cb=puzzle, example_file="example", solution_file="solution2", part=2)