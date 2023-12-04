from adventofcode.common import parse_input
input = parse_input("input")

cards = {}

for inline in input:
    cardno = int(inline.split(":")[0].split(" ")[-1])
    winning_numbers_raw = inline.split(":")[1].split("|")[0].strip().split(" ")
    winning_numbers = {int(x) for x in winning_numbers_raw if x.strip() != ""}
    my_numbers_raw = inline.split(":")[1].split("|")[1].strip().split(" ")
    my_numbers = {int(x) for x in my_numbers_raw if x.strip() != ""}
    count_intersection = len(winning_numbers.intersection(my_numbers))
    points = 2**(count_intersection-1) if count_intersection > 0 else 0
    cards[cardno] = {'winning_numbers': winning_numbers, 'my_numbers': my_numbers, 'count_intersection': count_intersection, 'points': points, 'count': 1}

solution_part1 = sum([x['points'] for x in cards.values()])
print(solution_part1)

# part 2

for cardno in sorted(cards.keys()):
    count_intersection = cards[cardno]['count_intersection']
    count = cards[cardno]['count']
    for i in range(cardno+1, cardno+count_intersection+1):
        cards[i]['count'] = cards[i]['count']+count

solution_part2 = sum([x['count'] for x in cards.values()])
print(solution_part2)