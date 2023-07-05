# 2476 주사위 게임


def find_prize(dice: list[int]) -> int:
    if all([i == dice[0] for i in dice]):
        return 10000 + 1000 * dice[0]
    elif sum([i == dice[0] for i in dice]) == 2:
        return 1000 + 100 * dice[0]
    elif sum([i == dice[1] for i in dice]) == 2:
        return 1000 + 100 * dice[1]
    elif sum([i == dice[2] for i in dice]) == 2:
        return 1000 + 100 * dice[2]
    else:
        return max(dice) * 100


N = int(input())
maximum_prize = 0
for _ in range(N):
    dice = list(map(int, input().split(" ")))
    maximum_prize = max(maximum_prize, find_prize(dice))
print(maximum_prize)