from adventofcode.common import parse_input


with open("input") as f:
    input = f.read().split("\n\n")

rules = [[int(x.split("|")[0]), int(x.split("|")[1])] for x in input[0].split("\n")]
updates = [[int(y) for y in x.split(",")] for x in input[1].split("\n")]


sum = 0
for update in updates:
    rules_ok = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not update.index(rule[0]) < update.index(rule[1]):
                rules_ok = False
    if rules_ok:
        middle_no = update[int((len(update)+1)/2)-1]
        sum += middle_no
print(sum)

sum = 0
updates_fixed = updates.copy()
for ix in range(len((updates_fixed))):
    rules_ok = True
    for i in range(3):
        for rule in rules:
            update = updates_fixed[ix]
            if rule[0] in update and rule[1] in update:
                r0_ix = update.index(rule[0])
                r1_ix = update.index(rule[1])
                if not update.index(rule[0]) < update.index(rule[1]):
                    rules_ok = False
                    updates_fixed[ix] = [*update[0:r1_ix], update[r0_ix], update[r1_ix], *update[r1_ix+1:r0_ix], *update[r0_ix+1:]]
    if not rules_ok:
        middle_no = updates_fixed[ix][int((len(update)+1)/2)-1]
        sum += middle_no
print(sum)