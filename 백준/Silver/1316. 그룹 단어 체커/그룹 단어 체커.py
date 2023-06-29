# 1316 그룹 단어 체커


def group_word_checker(target: str) -> bool:
    letter_checked = set()
    for i, v in enumerate(target):
        if v not in letter_checked:
            letter_checked.add(v)
            continue
        if v in target and target[i - 1] != v:
            return False
    return True


N = int(input())
result = 0
for _ in range(N):
    result += int(group_word_checker(input()))
print(result)