# 14347 Radioactive Islands (Large)

from math import inf
from sys import stdin, stdout
from typing import List, Tuple
input = stdin.readline
print = stdout.write

STEP: float = 0.01
Y_TOP: float = 20.0
Y_BOTTOM: float = -Y_TOP
X_END: float = 10.0
X_START: float = -X_END
ISLAND_X_POS: float = 0.0
ERROR_LIMIT: float = 10**-4


def distance_squared(
    island_i_y_pos: float, boat_x_pos: float, boat_y_pos: float
) -> float:
    return boat_x_pos**2 + (boat_y_pos - island_i_y_pos) ** 2


def dose_rate(island_y_pos: List[float], boat_x_pos: float, boat_y_pos: float) -> float:
    result = 1.0
    for island_i_y_pos in island_y_pos:
        if distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos) < ERROR_LIMIT:
            return inf
        result += 1.0 / distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos)
    return result


def curve_length_part(boat_y_pos_prime: float) -> float:
    return 1.0 + boat_y_pos_prime**2


def df_dy_corrected(
    island_y_pos: List[float],
    boat_x_pos: float,
    boat_y_pos: float,
    boat_y_pos_prime: float,
) -> float:
    result = 0.0
    for island_i_y_pos in island_y_pos:
        if distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos) < ERROR_LIMIT:
            return inf
        result -= (
            2.0
            * (boat_y_pos - island_i_y_pos)
            * distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos) ** -2
        )
    return result * curve_length_part(boat_y_pos_prime) ** 2


def d_dx_df_dyp_no_double_prime_part_corrected(
    island_y_pos: List[float],
    boat_x_pos: float,
    boat_y_pos: float,
    boat_y_pos_prime: float,
) -> float:
    result = 0.0
    for island_i_y_pos in island_y_pos:
        if distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos) < ERROR_LIMIT:
            return inf
        result -= (
            2.0
            * ((boat_y_pos - island_i_y_pos) * boat_y_pos_prime + boat_x_pos)
            * distance_squared(island_i_y_pos, boat_x_pos, boat_y_pos) ** -2
        )
    result *= boat_y_pos_prime * curve_length_part(boat_y_pos_prime)
    return result


def d_dx_df_dyp_double_prime_part_corrected(
    island_y_pos: List[float],
    boat_x_pos: float,
    boat_y_pos: float,
    boat_y_pos_prime: float,
) -> float:
    result = dose_rate(island_y_pos, boat_x_pos, boat_y_pos)
    return result


def find_y_double_prime(
    island_y_pos: List[float],
    boat_x_pos: float,
    boat_y_pos: float,
    boat_y_pos_prime: float,
) -> float:
    no_double_prime_part = df_dy_corrected(
        island_y_pos, boat_x_pos, boat_y_pos, boat_y_pos_prime
    ) - d_dx_df_dyp_no_double_prime_part_corrected(
        island_y_pos, boat_x_pos, boat_y_pos, boat_y_pos_prime
    )
    double_prime_part = -d_dx_df_dyp_double_prime_part_corrected(
        island_y_pos, boat_x_pos, boat_y_pos, boat_y_pos_prime
    )
    # print(f"{double_prime_part} {no_double_prime_part}\n")
    return -no_double_prime_part / double_prime_part


def is_inbound(current_pos: float, lower_limit: float, upper_limit: float):
    return lower_limit <= current_pos <= upper_limit


def runge_kutta(
    island_y_pos: List[float],
    boat_x_pos: float,
    boat_y_pos: float,
    boat_y_pos_prime: float,
) -> Tuple[float, float, float]:
    dose = 0.0
    try:
        for _ in range(int(X_START / STEP), int(X_END / STEP) + 1):
            if not is_inbound(boat_y_pos, Y_BOTTOM, Y_TOP):
                dose = inf
                break
            if not is_inbound(boat_x_pos, X_START, X_END):
                break
            dose += (STEP* dose_rate(island_y_pos, boat_x_pos, boat_y_pos) * curve_length_part(boat_y_pos_prime)**.5)
            runge_kutta_1st_const_k = STEP * boat_y_pos_prime
            runge_kutta_1st_const_l = STEP * find_y_double_prime(island_y_pos, boat_x_pos, boat_y_pos, boat_y_pos_prime)
            runge_kutta_2st_const_k = STEP * (boat_y_pos_prime + runge_kutta_1st_const_l / 2.0)
            runge_kutta_2st_const_l = STEP * find_y_double_prime(island_y_pos,boat_x_pos + STEP / 2.0,boat_y_pos + runge_kutta_1st_const_k / 2.0,boat_y_pos_prime + runge_kutta_1st_const_l / 2.0)
            runge_kutta_3st_const_k = STEP * (boat_y_pos_prime + runge_kutta_2st_const_l/2)
            runge_kutta_3st_const_l = STEP * find_y_double_prime(island_y_pos, boat_x_pos+STEP/2, boat_y_pos+runge_kutta_2st_const_k/2, boat_y_pos_prime+runge_kutta_2st_const_l/2)
            runge_kutta_4st_const_k = STEP * (boat_y_pos_prime + runge_kutta_3st_const_l)
            runge_kutta_4st_const_l = STEP * find_y_double_prime(island_y_pos, boat_x_pos+STEP, boat_y_pos+runge_kutta_3st_const_k, boat_y_pos_prime+runge_kutta_3st_const_l)
            boat_x_pos += STEP
            boat_y_pos += (runge_kutta_1st_const_k+2*runge_kutta_2st_const_k+2*runge_kutta_3st_const_k+runge_kutta_4st_const_k)/6
            boat_y_pos_prime += (runge_kutta_1st_const_l+2*runge_kutta_2st_const_l+2*runge_kutta_3st_const_l+runge_kutta_4st_const_l)/6
            # boat_y_pos += runge_kutta_1st_const_k
            # boat_y_pos_prime += runge_kutta_1st_const_l
            '''print(
                f"{dose=}\n{runge_kutta_1st_const_k=}\n{runge_kutta_1st_const_l=}\n{runge_kutta_2st_const_k=}\n{runge_kutta_2st_const_l=}\n{boat_x_pos=}\n{boat_y_pos=}\n{boat_y_pos_prime=}\n\n"
            )'''
            # print(f"{boat_x_pos=}\n")
    finally:
        return (dose, boat_y_pos, boat_x_pos)


def binary_search(
    A: float,
    B: float,
    island_y_pos: List[float],
    lower_bound_for_y_prime: float,
    upper_bound_for_y_prime: float,
) -> Tuple[float, float, float]:
    result: float = inf
    left_y_prime, right_y_prime = lower_bound_for_y_prime, upper_bound_for_y_prime
    while abs(right_y_prime-left_y_prime) > ERROR_LIMIT:
        mid_y_prime = (left_y_prime + right_y_prime) / 2.0
        result, boat_y_pos, boat_x_pos = runge_kutta(island_y_pos, X_START, A, mid_y_prime)
        # print(f"{left_y_prime=} {right_y_prime=} {mid_y_prime=} {result=} {boat_y_pos=} {boat_x_pos=}\n")
        if boat_y_pos >= B:
            right_y_prime = mid_y_prime
        else:
            left_y_prime = mid_y_prime
    return (result, boat_y_pos, boat_x_pos)


def find_slope_range_for_binary_search(A: float, island_y_pos: List[float]):
    MINIMAL_SLOPE: float = (A-Y_BOTTOM) / -10
    MAXIMAL_SLOPE: float = (A-Y_TOP) / -10
    slope_list = [MINIMAL_SLOPE, MAXIMAL_SLOPE]
    for island_i_y_pos in island_y_pos:
        slope_list.append((A-island_i_y_pos) / -10)
    slope_list.sort()
    # print(f"{slope_list}\n")
    return slope_list


def find_minimal_dose(A: float, B: float, island_y_pos: List[float]):
    result: float = inf
    slope_list = find_slope_range_for_binary_search(A, island_y_pos)
    for index, slope in enumerate(slope_list):
        if index == 0:
            continue
        result_sub, boat_y_pos, boat_x_pos = binary_search(A, B, island_y_pos, slope_list[index - 1], slope)
        if abs(boat_y_pos-B) <= 0.02 and abs(boat_x_pos-10) <= 0.02:
            result = min(result, result_sub)
    return result

T = int(input())
for i in range(1, T + 1):
    N, A, B = map(float, input().split(" "))
    island_y_pos = list(map(float, input().split(" ")))
    print(f"Case #{i}: {find_minimal_dose(A, B, island_y_pos)}\n")