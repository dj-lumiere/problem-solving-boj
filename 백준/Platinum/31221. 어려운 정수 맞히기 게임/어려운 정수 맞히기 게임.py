# 31221 어려운 정수 맞히기 게임


# sqrt(x)의 값을 [0, 10**9] 중 정수 범위로 확정지은 뒤 a at [0,2b+1)를 확정짓는다
def query():
    # check int(x**0.5)
    b_start = 0
    b_end = 10**9 + 1
    b = 0
    while b_start + 1 < b_end:
        b_mid = (b_start + b_end) // 2
        print(f"? 0 {b_mid}", flush=True)
        result = input()
        if result == "+":
            b_start = b_mid
        elif result == "-":
            b_end = b_mid
        else:
            b = b_mid
            break
    else:
        b = b_start
    # check residual part (x - int(x**0.5) ** 2)
    a_start = 0
    a_end = 2 * b + 1
    a = 0
    while a_start + 1 < a_end:
        a_mid = (a_start + a_end) // 2
        print(f"? {a_mid} {b}", flush=True)
        result = input()
        if result == "+":
            a_start = a_mid
        elif result == "-":
            a_end = a_mid
        else:
            a = a_mid
            break
        pass
    x = b**2 + a
    print(f"! {x}", flush=True)
    return


n = int(input())
for _ in range(n):
    query()