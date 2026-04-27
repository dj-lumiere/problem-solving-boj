from itertools import product

number = set(map(int, input().split()))
for i, j in product(range(-100,101), range(-100, 101)):
    target = set([i, i+j, i+2*j, i+3*j])
    if number.intersection(target) == number:
        print(*target.difference(number))
        break