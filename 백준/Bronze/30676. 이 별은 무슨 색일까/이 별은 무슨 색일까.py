# Red번 - 이 별은 무슨 색일까

color = [""] * 781
color[380:425] = ["Violet"] * (425 - 380)
color[425:450] = ["Indigo"] * (450 - 425)
color[450:495] = ["Blue"] * (495 - 450)
color[495:570] = ["Green"] * (570 - 495)
color[570:590] = ["Yellow"] * (590 - 570)
color[590:620] = ["Orange"] * (620 - 590)
color[620:781] = ["Red"] * (781 - 620)

l = int(input())
print(color[l])