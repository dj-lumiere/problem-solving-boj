n=int(input())
w=int(input())
score=10*n
if n>=3:
    score += 20
if n == 5:
    score += 50
if w > 1000:
    score -= 15
if score < 0:
    score = 0
print(score)