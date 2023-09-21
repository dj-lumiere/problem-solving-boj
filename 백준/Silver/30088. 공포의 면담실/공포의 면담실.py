# 30088 공포의 면담실

N = int(input())
work_end_time = [0 for _ in range(N)]

for i in range(N):
    _, *interview_time = map(int, input().split(" "))
    work_end_time[i] = sum(interview_time)

work_end_time.sort(reverse=True)
print(sum((i + 1) * v for i, v in enumerate(work_end_time)))