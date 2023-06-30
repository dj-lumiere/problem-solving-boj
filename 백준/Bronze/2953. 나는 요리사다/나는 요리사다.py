# 2953 나는 요리사다

max_score = 0
max_score_person = 0
for i in range(5):
    current_score = sum(list(map(int, input().split(" "))))
    if current_score > max_score:
        max_score = current_score
        max_score_person = i + 1
print(max_score_person, max_score)