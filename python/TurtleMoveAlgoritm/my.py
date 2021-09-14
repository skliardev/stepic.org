dict = [[key, int(value)] for key, value in [input().split() for _ in range(int(input()))]]
x, y = 0, 0
for key in dict:
    if key[0] == 'север':
        y += key[1]
    elif key[0] == 'юг':
        y -= key[1]
    elif key[0] == 'восток':
        x += key[1]
    else:
        x -= key[1]
print(x, y)
