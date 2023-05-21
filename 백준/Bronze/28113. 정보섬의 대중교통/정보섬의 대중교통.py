# 28113 정보섬의 대중교통

from sys import stdin, stdout

N, A, B = [int(i) for i in stdin.readline().strip().split(" ")]
if A < B:
    stdout.write("Bus")
elif A > B:
    stdout.write("Subway")
else:
    stdout.write("Anything")