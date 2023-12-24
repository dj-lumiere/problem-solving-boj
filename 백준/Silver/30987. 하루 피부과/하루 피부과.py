# CA번 - 하루 피부과

# ax^2+(b-d)x+(c-e) -> ax^3/3+(b-d)x^2/2+(c-e)x -> (2ax^3+3(b-d)x^2+6(c-e)x)//6

x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())
print(
    (
        2 * a * (x2**3 - x1**3)
        + 3 * (b - d) * (x2**2 - x1**2)
        + 6 * (c - e) * (x2 - x1)
    )
    // 6
)