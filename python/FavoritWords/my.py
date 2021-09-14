def update_dictionary_word(dictionary, string):
    sword = string.upper().strip().split()
    for key in set(sword):
        dictionary[key] = sword.count(key)


def get_favorite_word(dictionary):
    fav = ['', -1]
    for key in dictionary:
        if (fav[1] < dictionary[key]) or (fav[1] == dictionary[key] and fav[0] > key):
            fav[0] = key
            fav[1] = dictionary[key]
    return fav


with open(input('Имя файла: '), 'r') as inf, open('result.txt', 'w') as ouf:
    d = {}
    for row in inf:
        update_dictionary_word(d, row)
    f = get_favorite_word(d)
    print('Our favorit is ', f)
    ouf.writelines(f[0] + ' ' + str(f[1]))
