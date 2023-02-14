test_case_count = int(input())
test_case = list(map(int, input().split(" ")))
prime_count = 0

def sol(prime_check: int) -> int:
    if prime_check == 1:
        return 0
    else:
        for i in range(1, int(prime_check ** 0.5) + 1):
            if i == 1:
                continue
            if not prime_check % i and i != 1:
                return 0
        return 1

for i in test_case:
    prime_count += sol(i)

print(prime_count)

