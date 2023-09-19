# 11285 초성 중성 종성 2

first_consonant_list = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]
middle_vowel_list = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]
last_consonant_list = [
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]
first_consonant_count = len(first_consonant_list)
middle_vowel_count = len(middle_vowel_list)
last_consonant_count = len(last_consonant_list)

first_korean_letter_index = ord("가")
first_target_consonant = input()
middle_target_vowel = input()
last_target_consonant = input()
first_consonant_index = first_consonant_list.index(first_target_consonant)
middle_vowel_index = middle_vowel_list.index(middle_target_vowel)
last_consonant_index = last_consonant_list.index(last_target_consonant)
target_letter_index_in_korean = (
    first_consonant_index * middle_vowel_count + middle_vowel_index
) * last_consonant_count + last_consonant_index
print(chr(first_korean_letter_index + target_letter_index_in_korean))