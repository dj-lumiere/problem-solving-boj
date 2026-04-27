n = int(input())
words = [input() for _ in range(n)]
answer = 0
for x in words:
    if x == x[::-1]: answer +=1
print(answer*(answer-1)) 
