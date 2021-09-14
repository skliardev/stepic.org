url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get(url + "699991.txt")
while not r.text.startswith("We"):
    r = requests.get(url + r.text)
    print(r.text)
print(r.text)