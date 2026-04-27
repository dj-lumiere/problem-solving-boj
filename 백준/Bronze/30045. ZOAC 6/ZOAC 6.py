# 30045 ZOAC 6

N = int(input())
result = 0
words = [input() for _ in range(N)]
for word in words:
    for index, _ in enumerate(word):
        if index + 1 == len(word):
            break
        if word[index:index+2] in ("01", "OI"):
            result += 1
            break
print(result)