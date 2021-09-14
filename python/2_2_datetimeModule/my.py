import datetime
year, month, day = list(map(int, input().split()))
days = int(input())
date = datetime.date(year, month, day)
days = datetime.timedelta(days)
print((date + days).strftime('%Y %-m %-d'))
