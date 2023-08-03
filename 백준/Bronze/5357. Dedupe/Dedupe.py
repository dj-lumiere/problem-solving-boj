# 5357 Dedupe


def dedupize_string(target: str) -> str:
    result = ""
    for letter in target:
        if not result:
            result += letter
        elif letter == result[-1]:
            continue
        else:
            result += letter
    return result


N = int(input())
for _ in range(N):
    target = input()
    print(dedupize_string(target))