from decimal import getcontext
from sys import stderr, stdout

getcontext().prec = 1000


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
        A1 = Vector(rectangle_a[0], rectangle_a[1])
        A2 = Vector(rectangle_a[2], rectangle_a[3])
        A3 = Vector(rectangle_a[4], rectangle_a[5])
        A4 = Vector(rectangle_a[6], rectangle_a[7])
        
        B1 = Vector(rectangle_b[0], rectangle_b[1])
        B2 = Vector(rectangle_b[2], rectangle_b[3])
        B3 = Vector(rectangle_b[4], rectangle_b[5])
        B4 = Vector(rectangle_b[6], rectangle_b[7])
        
        rectangle_a_center = (A1 + A2 + A3 + A4) / 4
        rectangle_b_center = (B1 + B2 + B3 + B4) / 4
        vect_a1 = A2 - A1  # Edge from A1 to A2
        vect_a2 = A3 - A2  # Edge from A2 to A3
        
        vect_b1 = B2 - B1  # Edge from B1 to B2
        vect_b2 = B3 - B2  # Edge from B2 to B3

        vect_d = rectangle_b_center - rectangle_a_center
        a1 = vect_a1 * 0.5
        b1 = vect_b1 * 0.5
        a2 = vect_a2 * 0.5
        b2 = vect_b2 * 0.5
        u_a1 = Vector(-a1.y, a1.x)
        u_b1 = Vector(-b1.y, b1.x)
        u_a2 = Vector(-a2.y, a2.x)
        u_b2 = Vector(-b2.y, b2.x)
        u_a1 = u_a1 / u_a1.size() if u_a1.size() != 0 else u_a1
        u_b1 = u_b1 / u_b1.size() if u_b1.size() != 0 else u_b1
        u_a2 = u_a2 / u_a2.size() if u_a2.size() != 0 else u_a2
        u_b2 = u_b2 / u_b2.size() if u_b2.size() != 0 else u_b2
        if any(
                abs(vect_d.dot_product(u)) >= sum(abs(v.dot_product(u)) for v in (a1, a2, b1, b2))
                for u in (u_a1, u_a2, u_b1, u_b2)
        ):
            answer = 0
        else:
            answer = 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")