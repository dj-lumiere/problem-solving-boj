# 28418 회장님께 바치는 합성함수

INF = 10**9


def get_square(g: tuple[int, int]) -> tuple[int, int, int]:
    first, constant = g
    return tuple([first**2, 2 * first * constant, constant**2])


def get_p_x(f: tuple[int, int, int], g: tuple[int, int]) -> tuple[int, int, int]:
    f_second, f_first, f_constant = f
    g_square = get_square(g)
    g_square_second, g_square_first, g_square_constant = g_square
    g_first, g_constant = g
    result = (
        f_second * g_square_second,
        f_second * g_square_first + f_first * g_first,
        f_second * g_square_constant + f_first * g_constant + f_constant,
    )
    return result


def get_q_x(f: tuple[int, int, int], g: tuple[int, int]) -> tuple[int, int, int]:
    f_second, f_first, f_constant = f
    g_first, g_constant = g
    result = (
        g_first * f_second,
        g_first * f_first,
        g_first * f_constant + g_constant,
    )
    return result


def get_p_minus_q_x(
    p: tuple[int, int, int], q: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple([i - j for i, j in zip(p, q)])


def root_count(polynomial: tuple[int, int, int]) -> int:
    second, first, constant = polynomial
    if second == first == constant == 0:
        return INF
    if second == first == 0 and constant != 0:
        return 0
    if second == 0:
        return 1
    determinant = first * first - 4 * second * constant
    if determinant > 0:
        return 2
    elif determinant == 0:
        return 1
    else:
        return 0


f, g = tuple(map(int, input().split(" "))), tuple(map(int, input().split(" ")))
p = get_p_x(f, g)
q = get_q_x(f, g)
p_minus_q = get_p_minus_q_x(p, q)
result = root_count(p_minus_q)
if result == INF:
    print("Nice")
elif result == 2:
    print("Go ahead")
elif result == 1:
    print("Remember my character")
else:
    print("Head on")