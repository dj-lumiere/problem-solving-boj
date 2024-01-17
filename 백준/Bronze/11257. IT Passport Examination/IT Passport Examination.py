# 11257 IT Passport Examination

n = int(input())
for _ in range(n):
    id_number, strategy, it_management, technology = map(int, input().split(" "))
    is_pass = all(
        [
            (strategy + it_management + technology) >= 55,
            strategy * 10 >= 35 * 3,
            it_management * 10 >= 25 * 3,
            technology * 10 >= 40 * 3,
        ]
    )
    print(
        f"{id_number} {(strategy+it_management+technology)} "
        + ("PASS" if is_pass else "FAIL")
    )