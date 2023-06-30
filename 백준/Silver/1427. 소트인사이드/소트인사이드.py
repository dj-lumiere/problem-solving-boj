# 1427 소트인사이드

number = list(map(int, list(input())))
number.sort()
number.reverse()
print(*number, sep="")