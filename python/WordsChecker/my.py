
words = [input().lower() for i in range(int(input()))]
text = [input().split() for j in range(int(input()))]
ntext = []
for str in text:
    ntext += str
a = set([word for word in ntext if word.lower() not in words])
[print(word) for word in a]