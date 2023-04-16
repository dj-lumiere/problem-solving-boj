# G번

N, K = map(int, input().split(" "))
answer = 0

for i in range(1, N + 1):
    if i < 10:
        answer = (answer * 10 + i) % K
    elif i < 100:
        answer = (answer * 100 + i) % K
    elif i < 1000:
        answer = (answer * 1000 + i) % K
    elif i < 10000:
        answer = (answer * 10000 + i) % K
    elif i < 100000:
        answer = (answer * 100000 + i) % K
    elif i < 1000000:
        answer = (answer * 1000000 + i) % K
    elif i < 10000000:
        answer = (answer * 10000000 + i) % K
    else:
        answer = (answer * 100000000 + i) % K
print(answer)