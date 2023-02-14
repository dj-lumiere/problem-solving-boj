def word_count(sentence: str) -> int:
    word_list = []
    word_list = list(sentence.split(" "))
    if not word_list[0]:
        word_list.pop(0)
    if not word_list[-1]:
        word_list.pop()
    return len(word_list)

print(word_count(input()))
