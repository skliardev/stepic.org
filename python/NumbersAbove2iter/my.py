# put your python code here
arr = [int(i) for i in input().split()]
arr.sort()

while len(arr) > 0:       
    n = arr[0]
    if arr.count(n) > 1:
        print(n, end=' ')
    while n == arr[0]:
        arr = arr[1:]	#можно улучшить, так как мы знаем сколько таких элементов в списке
        if len(arr) == 0:
            break