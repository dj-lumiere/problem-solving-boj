# 4299 AFC 윔블던

score_sum, score_dif = map(int, input().split(" "))
if (score_sum + score_dif) % 2:
    print(-1)
else:
    score1, score2 = (score_sum + score_dif) // 2, (score_sum - score_dif) // 2
    if score2 < 0:
        print(-1)
    else:
        print(f"{score1} {score2}")