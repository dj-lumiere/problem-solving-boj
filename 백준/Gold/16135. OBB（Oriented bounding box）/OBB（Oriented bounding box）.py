from collections import deque
from decimal import getcontext
from itertools import combinations, product
from math import floor, log10
from sys import stdout, stderr

getcontext().prec = 1000


class MapIndex:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.function(self.iterable[key])


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def size(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, other):
        self.x *= other
        self.y *= other

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def angle_cos(self, other):
        return self.dot_product(other) / self.size() / other.size()

    def __str__(self):
        return f"[x: {self.x}, y: {self.y}]"

    def __repr__(self):
        return f"[x: {self.x}, y: {self.y}]"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        rectangle_a = [int(input()) for _ in range(8)]
        rectangle_b = [int(input()) for _ in range(8)]
        point_a1_x = rectangle_a[0]
        point_a1_y = rectangle_a[1]
        point_a2_x = rectangle_a[2]
        point_a2_y = rectangle_a[3]
        point_a3_x = rectangle_a[4]
        point_a3_y = rectangle_a[5]
        point_a4_x = rectangle_a[6]
        point_a4_y = rectangle_a[7]
        point_b1_x = rectangle_b[0]
        point_b1_y = rectangle_b[1]
        point_b2_x = rectangle_b[2]
        point_b2_y = rectangle_b[3]
        point_b3_x = rectangle_b[4]
        point_b3_y = rectangle_b[5]
        point_b4_x = rectangle_b[6]
        point_b4_y = rectangle_b[7]
        rectangle_a_center = Vector(sum(rectangle_a[::2]), sum(rectangle_a[1::2])) / 4
        rectangle_b_center = Vector(sum(rectangle_b[::2]), sum(rectangle_b[1::2])) / 4
        vect_a1 = Vector(point_a2_x - point_a1_x, point_a2_y - point_a1_y)
        vect_b1 = Vector(point_b2_x - point_b1_x, point_b2_y - point_b1_y)
        vect_a2 = Vector(point_a3_x - point_a1_x, point_a3_y - point_a1_y)
        vect_b2 = Vector(point_b3_x - point_b1_x, point_b3_y - point_b1_y)
        vect_a3 = Vector(point_a4_x - point_a1_x, point_a4_y - point_a1_y)
        vect_b3 = Vector(point_b4_x - point_b1_x, point_b4_y - point_b1_y)
        vect_a_center = vect_a2 * 0.5
        vect_b_center = vect_b2 * 0.5
        vect_d = rectangle_b_center - rectangle_a_center
        a1 = vect_a1 * 0.5
        b1 = vect_b1 * 0.5
        a2 = (vect_a2 if a1.dot_product(vect_a2) == 0 else vect_a3) * 0.5
        b2 = (vect_b2 if b1.dot_product(vect_b2) == 0 else vect_b3) * 0.5
        u_a1 = Vector(a1.y, -a1.x)
        u_a2 = Vector(a2.y, -a2.x)
        if u_a1.size() == 0 and u_a2.size() == 0:
            u_a1 = Vector(1, 0)
            u_a2 = Vector(0, 1)
        elif u_a1.size() == 0:
            u_a1 = Vector(u_a2.y, -u_a2.x)
        elif u_a2.size() == 0:
            u_a2 = Vector(u_a1.y, -u_a1.x)
        u_b1 = Vector(b1.y, -b1.x)
        u_b2 = Vector(b2.y, -b2.x)
        if u_b1.size() == 0 and u_b2.size() == 0:
            u_b1 = Vector(1, 0)
            u_b2 = Vector(0, 1)
        elif u_b1.size() == 0:
            u_b1 = Vector(u_b2.y, -u_b2.x)
        elif u_b2.size() == 0:
            u_b2 = Vector(u_b1.y, -u_b1.x)
        u_a1 = u_a1 / u_a1.size()
        u_b1 = u_b1 / u_b1.size()
        u_a2 = u_a2 / u_a2.size()
        u_b2 = u_b2 / u_b2.size()
        if any(
                abs(vect_d.dot_product(u)) >= abs(a1.dot_product(u)) + abs(a2.dot_product(u)) + abs(b1.dot_product(u)) + abs(b2.dot_product(u))
                for u in (u_a1, u_a2, u_b1, u_b2)):
            answer = 0
        else:
            answer = 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")