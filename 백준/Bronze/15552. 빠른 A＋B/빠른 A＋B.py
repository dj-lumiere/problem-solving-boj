from sys import stdin, stdout

N = int(input())
for i in range(N):
    A, B = list(map(int, stdin.readline().rstrip().split(" ")))
    stdout.writelines(f"{A+B}\n")