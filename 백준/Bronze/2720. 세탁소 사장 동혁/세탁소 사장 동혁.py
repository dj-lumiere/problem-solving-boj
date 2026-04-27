# 2720 세탁소 사장 동혁


def minimal_coin_charge(charge_in_cents: int) -> list[int]:
    coin_in_cents = [25, 10, 5, 1]
    result = [0, 0, 0, 0]
    for index, value in enumerate(coin_in_cents):
        while charge_in_cents >= value:
            charge_in_cents -= value
            result[index] += 1
    return result


T = int(input())
for _ in range(T):
    print(*minimal_coin_charge(int(input())))