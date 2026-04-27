import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        word = list(input().decode())
        start = 0
        end = n - 1
        while start <= end:
            front = word[start]
            back = word[end]
            if front == back == "?":
                word[start] = word[end] = "a"
            elif front == "?":
                word[start] = back
            elif back == "?":
                word[end] = front
            start += 1
            end -= 1
        answers[i] = "".join(word)
    print(answers)