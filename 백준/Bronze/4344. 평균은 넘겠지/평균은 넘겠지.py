# 4344 평균은 넘겠지
N = int(input())

for _ in range(N):
    student_count, *score = list(map(int, input().split(" ")))
    total_score = sum(score)
    score_over_avg_count = sum([student_count * i > total_score for i in score])
    score_over_avg_percentage = (score_over_avg_count * 1000000) // student_count
    score_over_avg_percentage_int_part, score_over_avg_percentage_frac_part = divmod(
        score_over_avg_percentage, 10000
    )
    if score_over_avg_percentage_frac_part % 10 >= 5:
        score_over_avg_percentage_frac_part = (
            score_over_avg_percentage_frac_part // 10 + 1
        )
    else:
        score_over_avg_percentage_frac_part = score_over_avg_percentage_frac_part // 10
    print(
        f"{score_over_avg_percentage_int_part}.{score_over_avg_percentage_frac_part:0>3}%"
    )
