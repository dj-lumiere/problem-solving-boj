import os
from collections import Counter

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        votes = [int(input()) for _ in range(n)]
        vote_count = Counter([i for i in votes if i != 0])
        freq_count = [0 for _ in range(n + 1)]
        for k, v in vote_count.items():
            if k == 0:
                continue
            freq_count[v] += 1
        most_voted = vote_count.most_common(1)[0][0]
        has_multiple_votes = False
        if freq_count[vote_count[most_voted]] > 1:
            has_multiple_votes = True
        answers[h] = f"{most_voted}" if not has_multiple_votes and any(i != 0 for i in votes) else "skipped"
    print(answers)