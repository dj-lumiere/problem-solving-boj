from itertools import permutations

t = int(input())
answers = []
for hh in range(1, t + 1):
    n = int(input())
    company_x, company_y, home_x, home_y, *customers = map(int, input().split())
    answer = min(sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in
                     zip([(company_x, company_y)] + list(visiting_order),
                         list(visiting_order) + [(home_x, home_y)])) for visiting_order in
                 permutations(zip(customers[::2], customers[1::2])))
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")