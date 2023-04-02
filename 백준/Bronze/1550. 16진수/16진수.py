# 1550 16진수

hex_str: str = input()
answer: int = 0

for (i, j) in enumerate(hex_str):
    if ord("A") <= ord(j) <= ord("F"):
        answer = answer * 16 + 10 + ord(j) - ord("A")
    else:
        answer = answer * 16 + int(j)
print(answer)