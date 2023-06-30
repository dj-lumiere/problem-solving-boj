# 10886 0 = not cute / 1 = cute

N = int(input())
vote_difference = 0
for _ in range(N):
    vote = int(input())
    if vote == 1:
        vote_difference += 1
    elif vote == 0:
        vote_difference -= 1
print("Junhee is " + ("not " if vote_difference < 0 else "") + "cute!")