import requests
with open(input('Имя файла: '), 'r') as inf, open('result.txt', 'w') as ouf:
    name = inf.read().strip()
    name = requests.get(name)
    name = name.text.strip()
    host = 'https://stepic.org/media/attachments/course67/3.6.3/'

    while 'We' not in name:
        print(name)
        name = requests.get(host + name)
        name = name.text.strip()
    print(name)
    ouf.write(str(name))
