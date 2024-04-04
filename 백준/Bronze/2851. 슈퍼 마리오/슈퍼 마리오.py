import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        numbers = [int(next(tokens)) for _ in range(10)]
        minimal_distance = 100
        current_value = 0
        answer = 0
        for j in numbers:
            current_value += j
            if minimal_distance > abs(current_value - 100) or (
                    minimal_distance == abs(current_value - 100) and current_value > answer):
                answer = current_value
                minimal_distance = abs(current_value - 100)
        answers[i] = str(answer)
    os.write(1, "\n".join(answers).encode())