import sys


def size(x):
    res = sys.getsizeof(x)
    print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += size(value)
                res += size(key)
        elif not isinstance(x, str):
            for items in x:
                res += size(items)

    return res
#1
N = 100
a = []
for i in range(N + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= N:
    if a[i] != 0:
        j = i + i
        while j <= N:
            a[j] = 0
            j = j + i
    i += 1
a = set(a)
a.remove(0)
print(a)
print(size(a))

print('***')
#2
n = 100
sieve = set(range(2, n+1))

while sieve:
    prime = min(sieve)
    print(prime, end="\t")
    sieve -= set(range(prime, n+1, prime))

print(size(prime))
print('***')

#3
n = 10
prime = []
a = 2
while len(prime) != n+1:
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        prime.append(a)
        print(prime)
    a += 1

print(size(prime))