# 17362 수학은 체육과목 입니다 2

n = int(input())
n -= 1
pattern_count, remainder = divmod(n, 4)
pattern = [[1, 2, 3, 4], [5, 4, 3, 2]]
print(pattern[pattern_count & 1][remainder])