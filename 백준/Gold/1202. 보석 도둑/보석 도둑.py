# 1202 보석 도둑

from heapq import heappush, heappop
from sys import stdin


class sort_by_mass:
    def __init__(self, A, B):
        self.value = (A, B)
        self.mass = A
        self.price = B

    def __lt__(self, other):
        return self.value < other.value

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        mass, price = self.value
        return f"({mass=}, {price=})"

    def __repr__(self):
        return str(self)


class sort_by_price:
    def __init__(self, A, B):
        self.value = (B, A)
        self.price = B
        self.mass = A

    def __lt__(self, other):
        return (-self.price, self.mass) < (-other.price, other.mass)

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        price, mass = self.value
        return f"({price=}, {mass=})"

    def __repr__(self):
        return str(self)


def input():
    return stdin.readline().strip()


N, K = map(int, input().split(" "))

jewelries = []
for _ in range(N):
    mass, price = map(int, input().split(" "))
    jewelries.append(sort_by_mass(mass, price))
jewelries.sort(reverse=True)

bags = []
for _ in range(K):
    max_mass_per_bag = int(input())
    bags.append(max_mass_per_bag)
bags.sort(reverse=True)


total_value = 0
stealable_jewelries = []
while bags:
    bag_capacity = bags.pop()
    while jewelries:
        current_jewelry = jewelries.pop()
        if current_jewelry.mass > bag_capacity:
            jewelries.append(current_jewelry)
            break
        current_mass, current_price = current_jewelry
        heappush(stealable_jewelries, sort_by_price(current_mass, current_price))
    if stealable_jewelries:
        current_value, _ = heappop(stealable_jewelries)
        total_value += current_value
print(total_value)