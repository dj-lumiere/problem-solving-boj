T = int(input())
for _ in range(T):
    korea_score = 0
    yonsei_score = 0
    for _ in range(9):
        yonsei_score_sub, korea_score_sub = map(int, input().split(" "))
        yonsei_score += yonsei_score_sub
        korea_score += korea_score_sub
    if korea_score > yonsei_score:
        print("Korea")
    elif korea_score < yonsei_score:
        print("Yonsei")
    else:
        print("Draw")