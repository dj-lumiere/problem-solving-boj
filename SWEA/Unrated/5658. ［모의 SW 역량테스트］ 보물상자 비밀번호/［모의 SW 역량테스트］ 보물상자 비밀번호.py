t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    code = input()
    code += code[:n//4]
    numbers = set()
    for v in zip(*[code[i:] for i in range(n//4)]):
        numbers.add(int("".join(v), base=16))
    print(f"#{i} {sorted(numbers, reverse=True)[k-1]}")