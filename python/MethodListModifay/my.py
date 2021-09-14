
def modify_list(arraylist):
    a = []
    for i in arraylist:
        if i % 2 == 0:
            a.append(i//2)
    arraylist.clear()
    arraylist += a


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]
