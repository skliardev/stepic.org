key, value = list(input()), list(input())
strd, strc = input(), input()

dc = {}
ddc = {}
for ind in range(len(key)):
    if key[ind] not in dc:
        dc[key[ind]] = value[ind]
    if value[ind] not in ddc:
        ddc[value[ind]] = key[ind]

nstr = ''
for c in strd:
    nstr += dc[c]
print(nstr)

nstr = ''
for c in strc:
    nstr += ddc[c]
print(nstr)
