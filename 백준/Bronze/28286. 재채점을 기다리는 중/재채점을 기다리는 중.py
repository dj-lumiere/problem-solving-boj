# 28286 재채점을 기다리는 중

N, K = map(int, input().split())
correct_answer = list(map(int, input().split()))
marked_answer = list(map(int, input().split()))


def push_right(answer: list[int], p: int) -> list[int]:
    return answer[:p] + [0] + answer[p : N - 1]


def push_left(answer: list[int], p: int) -> list[int]:
    return answer[:p] + answer[p + 1 : N] + [0]


def score_check(marked_answer: list[int]) -> int:
    return sum([a == b for a, b in zip(correct_answer, marked_answer)])


result = -1


def push(marked_answer: list[int], k: int) -> int:
    if k == 0:
        return score_check(marked_answer)
    global result
    for i in range(N):
        result = max(
            result,
            push(push_right(marked_answer, i), k - 1),
            push(push_left(marked_answer, i), k - 1),
            push(marked_answer, k - 1),
        )
    return result


print(push(marked_answer, K))