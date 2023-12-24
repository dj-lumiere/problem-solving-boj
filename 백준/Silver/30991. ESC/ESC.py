# CB번 - ESC

def esc_n(n):
    if n == 1:
        return (-1, 1, 1)
    ss, cc, sc = esc_n(n - 1)
    return (ss - sc, cc + sc, sc + 2 * ss - 2 * cc)


n = int(input())
print(sum(esc_n(n)))