a, b, c = (int(input()) for _ in range(3))
s = ((a&15)<<8)+((b&15)<<4)+((c&15)<<0)
print(f"{s:0>4}")