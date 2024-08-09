from bisect import bisect_right, bisect_left
from sys import stdout, stderr


def find_prime(a):
    finder_limit = a
    prime_list = [True for i in range(0, finder_limit + 1)]
    prime_list[0] = False
    prime_list[1] = False
    for x in range(1, int(finder_limit ** 0.5) + 1):
        if not prime_list[x]:
            continue
        prime_list[x: finder_limit + 1: x] = [False] * (finder_limit // x)
        prime_list[x] = True
    return [i for i, v in enumerate(prime_list) if v]


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    primes = find_prime(1000001)
    for hh in range(t):
        n = int(input())
        start_primes_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                            191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                            283, 293, 307, 311, 313, 317, 331, 337, 349, 353, 359, 367, 373, 383, 389, 397, 409, 439,
                            523]
        if n < 8:
            result_list = [-1]
        elif n % 2 == 1:
            result_list = [2, 3, 0, 0]
            n -= 5
            for j in start_primes_set:
                count = bisect_right(primes, n - j) - bisect_left(primes, n - j)
                if count != 0:
                    result_list[2] = j
                    result_list[3] = n - j
                    break
        else:
            result_list = [2, 2, 0, 0]
            n -= 4
            for j in start_primes_set:
                count = bisect_right(primes, n - j) - bisect_left(primes, n - j)
                if count != 0:
                    result_list[2] = j
                    result_list[3] = n - j
                    break
        result = " ".join(map(str, result_list))
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
