from adventofcode.common import parse_input

input = parse_input("input")
games = {}

max_amount = {'green': 13, 'red': 12, 'blue': 14}

for inline in input:
    temp1 = inline.split(":")
    game_id = int(temp1[0].split(" ")[-1])
    games[game_id] = []
    reveals = temp1[1].split(";")
    for reveal in reveals:
        reveal_subs = reveal.strip().split(",")
        reveal_temp = {}
        for reveal_sub in reveal_subs:
            temp_amount = int(reveal_sub.strip().split(" ")[0])
            temp_color = reveal_sub.strip().split(" ")[1]
            reveal_temp[temp_color] = temp_amount
        games[game_id].append(reveal_temp)

# part1

solution_part1 = 0

for game_id, game in games.items():
    game_possible = True
    for reveal in game:
        for color, amount in reveal.items():
            if amount > max_amount[color]:
                game_possible = False
    if game_possible:
        solution_part1 += game_id

print(solution_part1)

# part2

powers = []

for game_id, game in games.items():
    min_colors = {'green': 0, 'red': 0, 'blue': 0}
    for reveal in game:
        for color, amount in reveal.items():
            min_colors[color] = max(min_colors[color], amount)
    power = min_colors['green']*min_colors['red']*min_colors['blue']
    powers.append(power)

solution_part2 = sum(powers)
print(solution_part2)