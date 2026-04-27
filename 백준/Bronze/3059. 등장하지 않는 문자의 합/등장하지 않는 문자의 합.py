from string import ascii_uppercase

N = int(input())
for _ in range(N):
    s = input()
    print(sum(map(ord, ascii_uppercase))-sum(map(ord, set(list(s)))))