# 10808 알파벳 개수

alphabet_list = [0 for _ in range(26)]

for i in list(input()):
    alphabet_list[ord(i)-ord("a")] += 1

print(" ".join(map(str, alphabet_list)))