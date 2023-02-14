# 27162 Yacht Dice
hand_str = input()
# 각 패별로 사용 가능한지 여부에 대한 리스트 확인
hand_list = [False] + [hand_str[i] == "Y" for i in range(12)]
dice_list = list(map(int, input().split(" ")))
counter = [0 for j in range(0, 6 + 1)]
for i in dice_list:
    counter[i] += 1
score_list = [0 for i in range(0, 12 + 1)]
little_straight = [i for i in range(1, 5 + 1)]
big_straight = [i for i in range(2, 6 + 1)]
# Ones ~ Sixes의 경우 나머지 2개를 1~6으로 고정하고 갯수 합 재기
# Four of a Kind : 2+개의 똑같은 숫자가 보일 경우 그걸로 고정하고 숫자 고르기
# Full House : 2개의 숫자가 똑같은 경우, 나머지 숫자로 고정하고 합, 3개의 숫자가 똑같은 경우 걔를 제외한 최고 숫자로 고정 후 합 구하기
for i in range(1, 6 + 1):
    score_list[i] = hand_list[i] * i * (counter[i] + 2)
    if counter[i] == 2:
        score_list[7] = i * 4 * hand_list[7]
        score_list[8] = (
            max((sum(dice_list) - i * 2, i)) * 3 + min((sum(dice_list) - i * 2, i)) * 2
        ) * hand_list[8]
    elif counter[i] == 3:
        score_list[7] = i * 4 * hand_list[7]
        if i == 6:
            score_list[8] = (5 * 2 + i * 3) * hand_list[8]
        else:
            score_list[8] = (6 * 2 + i * 3) * hand_list[8]
        # Yacht : 3개의 숫자가 동일한 경우 50
        score_list[11] = 50 * hand_list[11]


# Little Straight : 1,2,3,4,5 중에 3개가 있을 경우 30
score_list[9] = (
    (sum([i in little_straight and counter[i] == 1 for i in dice_list]) == 3)
    * 30
    * hand_list[9]
)
# Big Straight : 2,3,4,5,6 중에 3개가 있을 경우 30
score_list[10] = (
    (sum([i in big_straight and counter[i] == 1 for i in dice_list]) == 3)
    * 30
    * hand_list[10]
)

# Choice : 6,6으로 고정 후 합 구하기
score_list[12] = (sum(dice_list) + 6 + 6) * hand_list[12]
print(max(score_list))