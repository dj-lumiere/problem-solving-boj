from sys import stderr, stdout


def get_mobius_sieve(limit: int) -> list[int]:
    mu_i_small = [1 for _ in range(limit + 1)]
    mu_i_small[0] = 0
    done_calculating = [0 for _ in range(limit + 1)]
    for i in range(2, limit + 1):
        if not done_calculating[i]:
            for j in range(i, limit + 1, i):
                mu_i_small[j] *= -1
                done_calculating[j] = True
            for j in range(i * i, limit + 1, i * i):
                mu_i_small[j] = 0
    return mu_i_small


def find_phi(x):
    divisors = []
    coefficients = [1]
    for i in range(1, int(x ** .5) + 1):
        if x % i != 0:
            continue
        divisors.append(i)
        if i != x // i:
            divisors.append(x // i)
    divisors.sort(key=lambda y: mu[x // y], reverse=True)
    n = 0
    for divisor in divisors:
        mu_value = mu[x // divisor]
        if mu_value == 0:
            continue
        elif mu_value == 1:
            tmp = [0] * (n + divisor + 1)
            for i, v in enumerate(coefficients):
                tmp[i] -= v
                tmp[i + divisor] += v
            coefficients = tmp
            n += divisor
        else:
            remainder = [0] * (divisor + 1)
            for i, v in enumerate(coefficients):
                remainder[i % divisor] += v
            for i, v in enumerate(remainder):
                coefficients[i] -= v
            tmp = [0] * (n - divisor + 1)
            for i, v in enumerate(reversed(coefficients)):
                degree = n - i
                if degree < divisor:
                    break
                tmp[degree - divisor] += v
                coefficients[degree] -= v
                coefficients[degree - divisor] += v
            coefficients = tmp
            n -= divisor
    return coefficients


def polynomial_to_string(coefficients):
    term_list = []
    n = len(coefficients) - 1
    for i, v in enumerate(reversed(coefficients)):
        degree = n - i
        if v == 0:
            continue
        if degree == 0 and v == 1:
            term_list.append(f"+1")
        elif degree == 0 and v == -1:
            term_list.append(f"-1")
        elif degree == 1 and v == 1:
            term_list.append(f"+x")
        elif degree == 1 and v == -1:
            term_list.append(f"-x")
        elif v == 1:
            term_list.append(f"+x^{degree}")
        elif v == -1:
            term_list.append(f"-x^{degree}")
        elif v > 0:
            term_list.append(f"+{v}x^{degree}")
        else:
            term_list.append(f"{v}x^{degree}")
    term_list[0] = term_list[0][1:]
    return "".join(term_list)


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    mu = get_mobius_sieve(100000)
    answers = []
    for hh in range(t):
        n = int(input())
        divisors = []
        for i in range(1, int(n ** .5) + 1):
            if n % i != 0:
                continue
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        divisors.sort()
        coefficients = [find_phi(x) for x in divisors]
        for i, v in enumerate(coefficients):
            coefficients[i]
        coefficients.sort(key=lambda x: (len(x), x))
        # multiplication of all (x^d-1)*mu(n/d) for d in divisors
        answer = "(" + ")(".join(map(lambda x: polynomial_to_string(x), coefficients)) + ")"
        answers.append(f"{answer}")
    print(*answers, sep="\n")