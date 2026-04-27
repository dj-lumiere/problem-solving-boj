from itertools import product

n = int(input())
a, b, c = map(int, input().split())
p, q = map(int, input().split())

for i,j,k,l in product(range(n), repeat=4):
    dist_a = abs(i-j)
    dist_b = abs(j-k)
    dist_c = abs(k-i)
    dist_p = abs(i-l)
    dist_q = abs(j-l)
    dist_r = abs(k-l)
    if dist_a > n//2:
        dist_a = n-dist_a
    if dist_b > n//2:
        dist_b = n-dist_b
    if dist_c > n//2:
        dist_c = n-dist_c
    if dist_p > n//2:
        dist_p = n-dist_p
    if dist_q > n//2:
        dist_q = n-dist_q
    if dist_r > n//2:
        dist_r = n-dist_r
    if dist_a == a and dist_b == b and dist_c == c and dist_p == p and dist_q == q:
        print(dist_r)
        break