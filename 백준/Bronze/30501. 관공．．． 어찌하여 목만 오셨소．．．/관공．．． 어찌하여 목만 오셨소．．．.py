# 30501 관공... 어찌하여 목만 오셨소...

N = int(input())
suspects = [input() for _ in range(N)]
for suspect in suspects:
    if "S" in suspect:
        print(suspect)
        break