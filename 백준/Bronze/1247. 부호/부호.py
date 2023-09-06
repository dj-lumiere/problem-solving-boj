import sys;input=sys.stdin.readline;s=lambda t:"+"if t>0 else"-"if t<0 else"0"
for _ in range(3):print(s(sum(int(input())for _ in range(int(input())))))