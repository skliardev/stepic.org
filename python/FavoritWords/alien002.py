with open('words.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))

��� ����������� �������� �������,������� �������� �� �������� ��������� ��� ������ ������������� ��������. � ������ ������ � ��� ���� ��������� ���������� ���� ,������� ���������� �  �����(��� ���� ���������(set(text) � ������� ����������� ������� max ) � �� ����� ������� ����� ���������� ,������� ���� ����� ����� ����������� � ������. ��������� ��������� ����� key =  �� ����� �������� ����� �������/����� ,� ������ ������ �������� count ���������� �� ������� ���������� ��������� ������� ����� � ������,�������/�� ����� ����������� � ������� �������� ���������.  ��� ��� ������, ��� ������� �� ����� ����� � ��������� �� ��������� (����������������� ) , � �����  ������� �������� �� ��������� ����� int. 

lis = ['1','100','111','2']
print(max(lis))#2
print(max(lis,key = lambda x: int(x)))#111
print(max(lis,key = int))#111