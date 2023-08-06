# 10384 팬그램


def alphabet_counter(target: str) -> list[int]:
    result = [0] * 26
    for letter in target:
        for i in range(26):
            if letter == chr(ord("a") + i) or letter == chr(ord("A") + i):
                result[i] += 1
    return result


N = int(input())
for i in range(1, N + 1):
    target = input()
    result = alphabet_counter(target)
    if all(i >= 3 for i in result):
        print(f"Case {i}: Triple pangram!!!")
    elif all(i >= 2 for i in result):
        print(f"Case {i}: Double pangram!!")
    elif all(i >= 1 for i in result):
        print(f"Case {i}: Pangram!")
    else:
        print(f"Case {i}: Not a pangram")