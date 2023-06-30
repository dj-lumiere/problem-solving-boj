# 2576 홀수

answer = 0
minimal_odd_number = 100000
while True:
    try:
        number = int(input())
        if number % 2:
            answer += number
            minimal_odd_number = min(minimal_odd_number, number)
    except:
        break
if answer == 0:
    print(-1)
else:
    print(answer, minimal_odd_number, sep="\n")