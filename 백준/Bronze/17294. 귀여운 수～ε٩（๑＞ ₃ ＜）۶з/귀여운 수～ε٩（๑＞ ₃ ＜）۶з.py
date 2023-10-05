# 17294 귀여운 수~ε٩(๑> ₃ <)۶з

IS_CUTE = r"◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
IS_NOT_CUTE = r"흥칫뿡!! <(￣ ﹌ ￣)>"


def is_cute_number(target: list[int]):
    for i, v in enumerate(target):
        if i - 1 < 0:
            continue
        if i + 1 >= len(target):
            break
        if v * 2 != target[i - 1] + target[i + 1]:
            return False
    return True


number = list(map(int, list(input())))
print(IS_CUTE if is_cute_number(number) else IS_NOT_CUTE)