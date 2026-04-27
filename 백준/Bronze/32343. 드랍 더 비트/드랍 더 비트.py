from itertools import product

def bit_count(x, n):
    return sum(x&(1<<i)!=0 for i in range(n))


n = int(input())
a, b = map(int, input().split())
print(max(i^j for i,j in product(range(1<<n), repeat=2) if bit_count(i, n) == a and bit_count(j, n) == b))