# put your python code here
arr = [int(i) for i in input().split()]
arr.sort()

while len(arr) > 0:       
    n = arr[0]
    if arr.count(n) > 1:
        print(n, end=' ')
    while n == arr[0]:
        arr = arr[1:]	#����� ��������, ��� ��� �� ����� ������� ����� ��������� � ������
        if len(arr) == 0:
            break