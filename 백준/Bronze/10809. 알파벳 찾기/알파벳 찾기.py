word_s = input()
letter_pos = [-1 for i in range(26)]
for i, letter in enumerate(word_s):
    if letter_pos[ord(letter)-ord("a")] == -1:
        letter_pos[ord(letter)-ord("a")] = i
print(" ".join(map(str, letter_pos)))
