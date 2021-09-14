# get the size of the side of the square
n = int(input())
size = n

# Init array and other variables
arr = [[0] * n for i in range(n)]
nxn = n ** 2            # max steps
index = 1               # counter (default equals 1)
curX = 0                # current horizontal position in the array
curY = 0                # current vertical position in the array
countX = n              # horizontal steps allowed (default equals n)
countY = 0              # vertical steps allowed (default equals zero)
stepHor = 1             # 0 - forbid to walk, 1 - step right, -1 - step left (default equals 1)
stepVer = 0             # 0 - forbid to walk, 1 - step down,  -1 - step up
countSide = 4           # side counter

# perform array traversal in n cycles
while True:
    # writeIndex
    arr[curY][curX] = index # swap coordinates if you want to change direction
    index += 1
    countX -= stepHor * stepHor
    countY -= stepVer * stepVer

    # conditions
    if index > nxn:
        break
    if countX == 0 and countY == 0:
        if stepHor == 1:
            stepHor = 0     # freeze walking direction
            stepVer = 1     # set the direction DOWN
            n -= 1          # resize steps on the side
            countY = n      # set vertical steps allowed
        elif stepVer == 1:
            stepVer = 0     # freeze walking direction
            stepHor = -1    # set the direction LEFT
            countX = n      # set horizontal steps allowed
        elif stepHor == -1:
            stepHor = 0     # freeze walking direction
            stepVer = -1    # set the direction UP
            n -= 1          # resize steps on the side
            countY = n      # set vertical steps allowed
        elif stepVer == -1:
            stepVer = 0     # freeze walking direction
            stepHor = 1     # set the direction RIGHT
            countX = n

    # make a step
    curX += stepHor
    curY += stepVer

    # # write to out
    # for i in range(size):
    #     for j in range(size):
    #         print(arr[i][j], end=' ')
    #     print()
    #
    # # debug
    # print('index:', index)
    # print('curX', curX)
    # print('curY', curY)
    # print('countX', countX)
    # print('countY', countY)

# write to out
for i in range(size):
    for j in range(size):
        print(arr[i][j], end=' ')
    print()
