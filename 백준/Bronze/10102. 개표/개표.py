V = int(input())
votes = list(input())
a_score = sum(i=="A" for i in votes)
b_score = V - a_score
if a_score > b_score:
    print("A")
elif a_score < b_score:
    print("B")
else:
    print("Tie")