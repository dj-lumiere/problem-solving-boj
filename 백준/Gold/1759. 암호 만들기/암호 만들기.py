# 1759 암호 만들기

l, c = list(map(int, input().split(" ")))
letters = list(map(str, input().split(" ")))
letters.sort()

vowels = ["a","e","i","o","u"]

def permut(N:int, M:int) -> list[list[str]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            password = []
            for i in stack:
                password.append(letters[i-1])
            list_permut.append(password[:])
            return
        else:
            for i in range(init, N+1):
                stack.append(i)
                dfs(i+1, M-1, stack)
                stack.pop()
    dfs(1, M, stack)
    return list_permut

password_list = permut(c, l)
allowed_password_list = []

for i in password_list:
    vowel_count = 0
    for k in i:
        if k in vowels:
            vowel_count += 1
    consonant_count = l-vowel_count
    if vowel_count >= 1 and consonant_count >= 2:
        allowed_password_list.append("".join(i))

for i in allowed_password_list:
    print(i)