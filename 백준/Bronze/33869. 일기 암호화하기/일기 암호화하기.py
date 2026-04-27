w = input()
s = input()
alphabet_table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
w_deduplicated = []
appeared_letter = set()
for letter in w:
    if letter not in appeared_letter:
        w_deduplicated.append(letter)
        appeared_letter.add(letter)
for letter in reversed(w_deduplicated):
    alphabet_table.pop(alphabet_table.index(letter))
    alphabet_table.insert(0, letter)
answer = ""
for letter in s:
    letter_order = ord(letter) - ord("A")
    answer += alphabet_table[letter_order]
print(answer)