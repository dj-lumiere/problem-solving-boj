# 5073 삼각형과 세 변

while True:
    side1, side2, side3 = map(int, input().split(" "))
    if side1 == side2 == side3 == 0:
        break
    side1, side2, side3 = sorted([side1, side2, side3])
    if side1 + side2 <= side3:
        print("Invalid")
    elif side1 == side2 == side3:
        print("Equilateral")
    elif side1 != side2 != side3 != side1:
        print("Scalene")
    else:
        print("Isosceles")