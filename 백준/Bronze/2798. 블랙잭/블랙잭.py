N, M = list(map(int, input().split(" ")))
card = list(map(int, input().split(" ")))

def sol(card_count: int, target_number: int, card_list: list[int]) -> int:
    card_sum = 0
    for i in range(0, card_count):
        for j in range(i+1, card_count):
            for k in range(j+1, card_count):
                card_sum_temp = card_list[i]+card_list[j]+card_list[k]
                if card_sum_temp <= target_number and card_sum_temp > card_sum:
                    card_sum = card_sum_temp
    return card_sum

print(sol(N, M, card))