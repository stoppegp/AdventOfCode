from adventofcode.common import parse_input
import numpy as np

input = parse_input("input1")

list1 = []
list2 = []
for row in input:
    temp1 = row.split()
    list1.append(int(temp1[0]))
    list2.append(int(temp1[1]))

array1 = np.array(sorted(list1))
array2 = np.array(sorted(list2))

distances = abs(array2 - array1)
print(sum(distances))

#part 2
sim_scores = []
for x in list1:
    sim_scores.append(x*list2.count(x))
print(sum(sim_scores))