N, M = map(int, input().split())
answer = [""] + ["OLDBIE!"]*N + ["TLE!"]*1000
answer[1:3]= ["NEWBIE!"]*2
print(answer[M])