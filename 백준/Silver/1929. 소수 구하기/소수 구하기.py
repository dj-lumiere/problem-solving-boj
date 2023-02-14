import sys

m, n = list(map(int, input().split(" ")))

def prime_checker(prime_check: int) -> bool:
    if prime_check == 1:
        return False
    else:
        for i in range(1, int(prime_check ** 0.5) + 1):
            if i == 1:
                continue
            if not prime_check % i and i != 1:
                return False
        return True

def sol(x:int, y:int) -> None:
    prime_list = []
    for i in range(x, y+1):
        if prime_checker(i):
            sys.stdout.writelines(f"{i}\n")

sol(m,n)