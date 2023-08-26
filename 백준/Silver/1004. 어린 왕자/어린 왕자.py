# 1004 어린 왕자
from sys import stdin


def input():
    return stdin.readline().strip()


class Point:
    def __init__(self, *coordinates):
        self.value = coordinates

    def __iter__(self):
        return iter(*self.value)

    def distance(self, other: "Point"):
        return sum([(v1 - v2) ** 2 for v1, v2 in zip(self, other)])

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def __iter__(self):
        return iter((*self.center, self.radius))

    def __str__(self):
        return f"{self.center=}, {self.radius=}"

    def __repr__(self):
        return f"{self.center=}, {self.radius=}"

    def is_in_circle(self, some_point: Point):
        return self.center.distance(some_point) < self.radius**2


def minimal_passes(start: Point, end: Point, *circles: Circle):
    result = 0
    for circle in circles:
        if circle.is_in_circle(start) ^ circle.is_in_circle(end):
            result += 1
    return result


T = int(input())
for _ in range(T):
    coordinates = list(map(int, input().split()))
    start = Point(coordinates[:2])
    end = Point(coordinates[2:])
    N = int(input())
    circles = []
    for _ in range(N):
        *center, radius = map(int, input().split(" "))
        circles.append(Circle(Point(center), radius))
    print(minimal_passes(start, end, *circles))