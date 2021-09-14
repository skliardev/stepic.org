def update_dict(d, key, wins, draw, defeat, score):
    if key not in d:
        d[key] = [0, 0, 0, 0, 0]
    d[key] = [d[key][0] + 1, d[key][1] + wins, d[key][2] + draw, d[key][3] + defeat, d[key][4] + score]


n = int(input())
dict = {}
while n > 0:
    # Get match
    key1, goal1, key2, goal2 = input().strip().split(';')
    wins1, wins2 = int(goal1 > goal2), int(goal2 > goal1)
    draw = int(goal2 == goal1)
    defeat1, defeat2 = wins2, wins1
    score1, score2 = int(3 * (wins1) or draw or 0), int(3 * (wins2) or draw or 0)

    # Update dictionary
    update_dict(dict, key1, wins1, draw, defeat1, score1)
    update_dict(dict, key2, wins2, draw, defeat2, score2)

    n -= 1
for team in dict:
    print(team + ':', end='')
    print(*dict[team])
