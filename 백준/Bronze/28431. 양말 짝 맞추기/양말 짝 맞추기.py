# A번 - 양말 짝 맞추기

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

result = 0
for _ in range(5):
    sock_number = int(input())
    result ^= sock_number
print(f"{result}")