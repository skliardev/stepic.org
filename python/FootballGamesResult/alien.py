def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1,
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]
dct = {}

for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))