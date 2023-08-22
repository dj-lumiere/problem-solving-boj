# 27967 고추장 괄호 문자열


def is_valid_bracket_pair(target: str) -> bool:
    bracket_stack = 0
    is_valid = True
    for letter in target:
        if letter == "(":
            bracket_stack += 1
        elif letter == ")" and bracket_stack > 0:
            bracket_stack -= 1
        else:
            is_valid = False
    return bracket_stack == 0 and is_valid


def fill_g_letter(status: int, g_position: list[int], g_count: int, target: str) -> str:
    result = list(target)
    for i in range(g_count):
        bracket = "(" if status >> i & 1 else ")"
        result[g_position[i]] = bracket
    return "".join(result)


def find_valid_bracket(target: str) -> str:
    g_count = sum(i == "G" for i in string_to_complete)
    g_position = [i for i, v in enumerate(string_to_complete) if v == "G"]
    answer = ""
    for status in range(1 << g_count):
        bracket = fill_g_letter(status, g_position, g_count, string_to_complete)
        if is_valid_bracket_pair(bracket):
            answer = bracket
            break
    return answer


N = int(input())
string_to_complete = input()
answer = find_valid_bracket(string_to_complete)
print(answer)