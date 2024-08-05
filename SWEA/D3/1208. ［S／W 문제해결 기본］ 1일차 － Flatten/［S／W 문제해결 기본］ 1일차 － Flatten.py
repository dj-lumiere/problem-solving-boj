t = 10
answers = []
for hh in range(t):
    k = int(input())
    x = list(map(int, input().split()))
    freq = [0 for _ in range(101)]
    for v in x:
        freq[v] += 1
    min_height = 0
    max_height = 0
    for _ in range(k):
        for i, v in enumerate(freq):
            if v != 0:
                min_height = i
                break
        for i, v in enumerate(reversed(freq), start=1):
            if v != 0:
                max_height = 101 - i
                break
        if max_height - min_height == 1:
            break
        freq[max_height] -= 1
        freq[max_height-1] += 1
        freq[min_height] -= 1
        freq[min_height+1] += 1
    for i, v in enumerate(freq):
        if v != 0:
            min_height = i
            break
    for i, v in enumerate(reversed(freq), start=1):
        if v != 0:
            max_height = 101 - i
            break
    answer = max_height - min_height
    answers.append(f"#{hh+1} {answer}")
print(*answers, sep="\n")
