# ������ �������� ������� ������ ��� ��������� ���� � �����������
s = input()

while len(s) > 0:       
    c = s[0]
    sum = 0
    while c == s[0]:
        sum +=1
        s = s[1:]		#����� ��������, ��� ��� �� ����� ������� ����� ��������� � ������ ����� s.count()
        if len(s) == 0:
            break

    print(c, sum, sep='', end='')