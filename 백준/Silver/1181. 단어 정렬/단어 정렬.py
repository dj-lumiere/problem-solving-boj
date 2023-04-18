# 1181 단어 정렬

N: int = int(input())
word_list: list[tuple[int, str]] = []
for i in range(N):
    word: str = input()
    word_list.append((len(word), word))
word_list = list(set(word_list))
word_list = sorted(word_list, key=lambda x: (x[0], x[1]))
print(*[j for (_, j) in word_list], sep="\n")