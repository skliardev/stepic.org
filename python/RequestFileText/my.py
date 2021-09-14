import requests
with open(input('Имя файла: '), 'r') as inf, open('result.txt', 'w') as ouf:
    req = requests.get(inf.read().strip())
    s = len(req.text.splitlines())
    print(s)
    print(req.text.splitlines())
    ouf.write(str(s))
