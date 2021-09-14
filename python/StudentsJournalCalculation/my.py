with open(input('Имя файла: '), 'r', encoding='utf-8') as inf, open('result.txt', 'w', encoding='utf-8') as ouf:
    journal = []
    for student in inf:
        student_sel = [student.strip().split(';')]
        journal += [[name, float(mat), float(phy), float(lng)] for name, mat, phy, lng in student_sel]
    [print((mat + phy + lng) / 3) for name, mat, phy, lng in journal]
    [ouf.write(str((mat + phy + lng) / 3) + '\n') for name, mat, phy, lng in journal]

    [print(sum([mat for name, mat, phy, lng in journal]) / len(journal), end=' ')]
    [print(sum([phy for name, mat, phy, lng in journal]) / len(journal), end=' ')]
    [print(sum([lng for name, mat, phy, lng in journal]) / len(journal), end=' ')]
    [ouf.write(str(sum([mat for name, mat, phy, lng in journal]) / len(journal)) + ' ')]
    [ouf.write(str(sum([phy for name, mat, phy, lng in journal]) / len(journal)) + ' ')]
    [ouf.write(str(sum([lng for name, mat, phy, lng in journal]) / len(journal)) + ' ')]
