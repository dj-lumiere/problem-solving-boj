from itertools import zip_longest

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    answer = 0
    current = 0
    for i, j in zip_longest(map(int,reversed(str(a))), map(int, reversed(str(b))), fillvalue=0):
        if i+j+current >= 10:
            current = 1
            answer += 1
        else:
            current = 0
    print(answer)