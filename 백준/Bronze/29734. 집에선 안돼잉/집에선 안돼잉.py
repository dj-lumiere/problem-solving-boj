# 29734 집에선 안돼잉

n, m = map(int, input().split(" "))
t, s = map(int, input().split(" "))

zip_hour = (8 + s) * ((n + 7) // 8 - 1) + (n % 8 if n % 8 else 8)
dok_hour = (t + 8 + t + s) * ((m + 7) // 8 - 1) + (t + m % 8 if m % 8 else t + 8)

if zip_hour > dok_hour:
    print(f"Dok\n{dok_hour}")
elif zip_hour < dok_hour:
    print(f"Zip\n{zip_hour}")
