N = int(input())
changyoung_dice = []
sangduk_dice = []
changyoung_score = 100
sangduk_score = 100
for _ in range(N):
    dice1, dice2 = map(int, input().split())
    changyoung_dice.append(dice1)
    sangduk_dice.append(dice2)
changyoung_score -= sum(v2 if v1 < v2 else 0 for v1, v2 in zip(changyoung_dice, sangduk_dice))
sangduk_score -= sum(v1 if v2 < v1 else 0 for v1, v2 in zip(changyoung_dice, sangduk_dice))
print(changyoung_score, sangduk_score, sep="\n")