# 1394 암호

mod = 900528
available_letters_dict = {value: index for index, value in enumerate(input())}
available_letters_count = len(available_letters_dict)
target_string = input()
target_string_length = len(target_string)
answer = 0
# 일단 target_string_length-1자리까지의 모든 문자열을 거침
answer_sub1 = (
    (
        available_letters_count
        * pow(
            base=available_letters_count,
            exp=target_string_length - 1,
            mod=mod * (available_letters_count - 1),
        )
        - 1
    )
    // (available_letters_count - 1)
) % mod
# 그 다음 target_string이 target_string_length 자리 문자열 중 몇번째인지 구함
answer_sub2 = 0
for index, value in enumerate(target_string):
    answer_sub2 *= available_letters_count
    answer_sub2 += available_letters_dict[value]
    answer_sub2 %= mod
print((answer_sub1 + answer_sub2) % mod)
