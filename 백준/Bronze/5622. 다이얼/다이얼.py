# 5622 다이얼

dialpad = "22233344455566677778889999"


def alphabet_order(x: str) -> int:
    if x.isupper():
        return ord(x) - ord("A")
    if x.islower():
        return ord(x) - ord("a")


print(sum([1 + int(dialpad[alphabet_order(i)]) for i in input()]))