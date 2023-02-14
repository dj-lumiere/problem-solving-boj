from sys import stdin, stdout

def Turret(x1: int, y1: int, r1:int, x2: int, y2: int, r2: int) -> int:
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        dist = (x1-x2)**2 + (y1-y2)**2
        if (r1-r2)**2 < dist and dist < (r1+r2)**2:
            return 2
        elif (r1+r2)**2 == dist or (r1-r2)**2 == dist:
            return 1
        else:
            return 0

n = int(input())

def loading_list_n_turret(n: int) -> None:
    while n:
        n -= 1
        x1, y1, r1, x2, y2, r2 = list(map(int, stdin.readline().rstrip().split(" ")))
        stdout.writelines(f"{Turret(x1, y1, r1, x2, y2, r2)}\n")

loading_list_n_turret(n)