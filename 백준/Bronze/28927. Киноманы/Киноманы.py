# 28927 Киноманы

A1, B1, C1 = map(int, input().split(" "))
A2, B2, C2 = map(int, input().split(" "))
max_score = A1 * 3 + B1 * 20 + C1 * 120
mel_score = A2 * 3 + B2 * 20 + C2 * 120
if max_score == mel_score:
    print("Draw")
elif max_score > mel_score:
    print("Max")
else:
    print("Mel")