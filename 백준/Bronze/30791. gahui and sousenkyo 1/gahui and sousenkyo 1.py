# A번 - gahui and sousenkyo 1

senbatsu, *others = map(int, input().split(" "))
print(sum(senbatsu - i <= 1000 for i in others))