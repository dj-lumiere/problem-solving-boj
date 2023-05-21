# 28123 삶, 우주, 그리고 모든 것에 관한 궁극적인 질문의 해답

n, k, x = (int(i) for i in input().split(" "))
offset_table = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print(n - 3 * (k - 1) - offset_table[x])