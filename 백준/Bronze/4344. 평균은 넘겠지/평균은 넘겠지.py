# 4344 평균은 넘겠지
N = int(input())

for _ in range(N):
    student_count, *score = list(map(int, input().split(" ")))
    total_score = sum(score)
    score_over_avg_count = (
        sum([student_count * i > total_score for i in score]) * 100 / student_count
    )
    print(f"{score_over_avg_count:.3f}%")