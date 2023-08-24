# 27315 틀리는 건 싫으니까 쉬운 문제에 올인하려고 합니다

from heapq import heappush, heappop, heapify
from sys import stdin


class sort_by_idea:
    def __init__(self, A, B):
        self.value = (A, B)

    def __lt__(self, other):
        return self.value < other.value

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return f"(idea difficulty = {self.value[0]}, implementation difficulty = {self.value[1]})"

    def __repr__(self):
        return f"(idea difficulty = {self.value[0]}, implementation difficulty = {self.value[1]})"


class sort_by_implementation:
    def __init__(self, A, B):
        self.value = (B, A)

    def __lt__(self, other):
        return self.value < other.value

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return f"(implementation difficulty = {self.value[0]}, idea difficulty = {self.value[1]})"

    def __repr__(self):
        return f"(implementation difficulty = {self.value[0]}, idea difficulty = {self.value[1]})"


def input():
    return stdin.readline().strip()


def is_solvable(current_idea_ability, idea_difficulty):
    return current_idea_ability >= idea_difficulty


def parse_problems(N):
    problems = []
    for _ in range(N):
        idea_difficulty, implementation_difficulty, has_data, has_editorial = map(
            int, input().split(" ")
        )
        if has_data:
            implementation_difficulty = 0
        if has_editorial:
            idea_difficulty = (idea_difficulty + 1) // 2
            implementation_difficulty = implementation_difficulty // 2
        problems.append(sort_by_idea(idea_difficulty, implementation_difficulty))
    return problems


def find_solvable_problem(problems, current_idea_ability, solvable_problems):
    while problems:
        problem = heappop(problems)
        idea_difficulty, _ = problem
        if not is_solvable(current_idea_ability, idea_difficulty):
            heappush(problems, problem)
            break
        heappush(solvable_problems, sort_by_implementation(*problem))
    return solvable_problems


def minimize_wrong_answer_count(solvable_problems, current_implementation_ability):
    problem = heappop(solvable_problems)
    implementation_difficulty, _ = problem
    result = max(implementation_difficulty - current_implementation_ability, 0)
    return result


N, M = map(int, input().split(" "))
problems = parse_problems(N)
problems.sort()
current_idea_ability, current_implementation_ability = map(int, input().split(" "))
solvable_problems = []
wrong_answer_count = 0
paused_prematurely = False
for _ in range(M):
    wrong_answer_count_sub = 0
    solvable_problems = find_solvable_problem(
        problems, current_idea_ability, solvable_problems
    )
    if not solvable_problems:
        paused_prematurely = True
        break
    wrong_answer_count_sub = minimize_wrong_answer_count(
        solvable_problems, current_implementation_ability
    )
    wrong_answer_count += wrong_answer_count_sub
    current_idea_ability += 1
    current_implementation_ability += 1

if paused_prematurely:
    print(-1)
else:
    print(wrong_answer_count)