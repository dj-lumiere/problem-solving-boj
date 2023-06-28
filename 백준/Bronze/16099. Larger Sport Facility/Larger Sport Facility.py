# 16099 Larger Sport Facility

T = int(input())
for _ in range(T):
    w_y, h_y, w_k, h_k = map(int, input().split(" "))
    print(
        "Eurecom"
        if w_y * h_y < w_k * h_k
        else "TelecomParisTech"
        if w_y * h_y > w_k * h_k
        else "Tie"
    )