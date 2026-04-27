def parse(s):
    s_split = s.split(".")
    return int(s_split[0][1:])*100+int(s_split[1])

n=int(input())
s=input()
initial_budget = parse(s)
answer = 0
for _ in range(n):
    s=input()
    initial_budget+=parse(s)
    if initial_budget % 100 != 0:
        answer+=1
print(answer)