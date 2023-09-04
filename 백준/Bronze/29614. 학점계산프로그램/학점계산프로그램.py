# A번 - 학점계산프로그램

from re import split
from sys import stdin


def input():
    return stdin.readline().strip()


def grade_to_score(grade):
    conversion_factor = {
        "A+": 4.5,
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D+": 1.5,
        "D": 1.0,
        "F": 0.0,
    }
    return conversion_factor[grade]


grades = split(r"(A\+|B\+|C\+|D\+|[A-F])", input())
grades = [i for i in grades if i]
print(sum(map(grade_to_score, grades)) / len(grades))