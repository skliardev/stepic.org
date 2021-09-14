# put your python code here
m = []
s = input()
while(s != 'end'):
    m.append([int(i) for i in s.split()])
    s = input()


mresult = list([] for i in range(len(m)))
for i in range(len(m)):
    for j in range(len(m[i])):
        mresult[i].append(0)

for i in range(len(m)):
    for j in range(len(m[i])):
        mresult[i][j] = m[i-1][j] + m[(i+1)%len(m)][j] + m[i][j-1] + m[i][(j+1)%len(m[i])]


for i in range(len(mresult)):
    for j in range(len(mresult[i])):
        print(mresult[i][j], end = ' ')
    print()