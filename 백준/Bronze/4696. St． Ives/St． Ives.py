# 4696 St. Ives

while True:
    ratio = float(input())
    result = 0.0
    if ratio == 0.0:
        break
    for i in range(5):
        result += ratio**i
    print(f"{result:.2f}")