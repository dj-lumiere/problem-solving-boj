# B번 - 무지개 만들기
from collections import Counter

N = int(input())
word = list(input())
letter_count = Counter(word)
small_letter_rainbow = "roygbiv"
big_letter_rainbow = "ROYGBIV"
small_letter_rainbow_completable = all(i in letter_count for i in small_letter_rainbow)
big_letter_rainbow_completable = all(i in letter_count for i in big_letter_rainbow)
if small_letter_rainbow_completable and big_letter_rainbow_completable:
    print("YeS")
elif small_letter_rainbow_completable:
    print("yes")
elif big_letter_rainbow_completable:
    print("YES")
else:
    print("NO!")