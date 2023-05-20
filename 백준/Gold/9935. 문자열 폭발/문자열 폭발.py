# 9935 문자열 폭발

letter_list: list[str] = list(input())
explosion_list: list[str] = list(input())
explosion_length: int = len(explosion_list)
after_explosion: list[str] = []
for i, j in enumerate(letter_list):
    after_explosion.append(j)
    if explosion_list[-1] == j:
        if explosion_list == after_explosion[-len(explosion_list):]:
            for k in range(len(explosion_list)):
                after_explosion.pop()
if after_explosion:
    print(*after_explosion, sep="")
else:
    print("FRULA")