import itertools

def primes():
    a = 1
    nums = []
    while True:
        a += 1
        neg = 0
        for num in nums:
            if a % num == 0:
                neg += 1
        if neg == 0:
            nums.append(a)
            yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))