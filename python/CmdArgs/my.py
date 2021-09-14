import sys
[print(sys.argv[i], end = ' ') for i in range(len(sys.argv)) if i != 0]