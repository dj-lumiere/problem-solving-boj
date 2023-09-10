# 29738 Goodbye, Code Jam


def last_candidate_round(rank):
    if rank <= 25:
        return "World Finals"
    if rank <= 1000:
        return "Round 3"
    if rank <= 4500:
        return "Round 2"
    return "Round 1"


T = int(input())
for i in range(1, T + 1):
    rank = int(input())
    print(f"Case #{i}: {last_candidate_round(rank)}")