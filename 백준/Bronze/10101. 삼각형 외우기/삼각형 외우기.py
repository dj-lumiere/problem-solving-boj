# 10101 삼각형 외우기

angle1, angle2, angle3 = int(input()), int(input()), int(input())
if angle1 + angle2 + angle3 != 180:
    print("Error")
elif angle1 == angle2 == angle3 == 60:
    print("Equilateral")
elif angle1 != angle2 != angle3 != angle1:
    print("Scalene")
else:
    print("Isosceles")