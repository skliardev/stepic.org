# put your python code here
a = int(input())
b = int(input())

nok = a * b

while(a != b): #looking for nok here
    if(a > b):
        a -= b
    else:
        b -= a
        
print(int(nok / a))