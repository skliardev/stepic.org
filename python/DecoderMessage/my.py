def decoder(string):
    i = 0
    result = ''
    while i < len(string):
        j = i + 1
        while j < len(string) and string[j].isdigit():
            j += 1
        result += string[i] * int(string[i + 1:j])
        i = j
    return result


name = input('Введите имя файла: ')
arr = ''
with open(name, 'r') as ofile, open('result.txt', 'w') as wfile:
    wfile.write(decoder(ofile.readline().strip()))
