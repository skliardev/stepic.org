with open(input('Enter file name: '), 'r') as inf, open('result.txt', 'w') as ouf:
    dictStudensGrowth = {str(key+1): 0 for key in range(11)}
    dictStudensCount  = {str(key+1): 0 for key in range(11)}
    for student in inf:
        selStudent = student.strip().split()
        key = selStudent[0]         # this key
        growth = selStudent[2]      # this growth of student
        dictStudensGrowth[key] += int(growth)
        dictStudensCount[key] += 1
    for classroom in dictStudensGrowth:
        tmp_num = 0
        if dictStudensGrowth[classroom] != 0:
            tmp_num = dictStudensGrowth[classroom] / dictStudensCount[classroom]
        print(classroom, str(tmp_num if tmp_num > 0 else '-'))
        ouf.write(classroom + ' ' + str(tmp_num if tmp_num > 0 else '-') + '\n')


