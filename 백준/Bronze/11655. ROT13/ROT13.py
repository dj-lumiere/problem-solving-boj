# 11655 ROT13

target_string = input()
answer = ""
for i in target_string:
    if ord("A") <= ord(i) <= ord("Z"):
        answer += chr((ord(i) + 13 - ord("A")) % 26 + ord("A"))
    elif ord("a") <= ord(i) <= ord("z"):
        answer += chr((ord(i) + 13 - ord("a")) % 26 + ord("a"))
    else:
        answer += i
print(answer)