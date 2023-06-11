# 1213 팰린드롬 만들기

from collections import Counter, deque

letter_counter: Counter[str] = Counter(list(input()))
letter_counter_sorted: list[tuple] = sorted(
    letter_counter.items(), key=lambda item: item[0]
)
palindrome_deque: deque[str] = deque()

odd_number_char: str = ""
if sum([j % 2 == 1 for (i, j) in letter_counter_sorted]) > 1:
    print("I'm Sorry Hansoo")
else:
    for i, j in letter_counter_sorted:
        if j % 2 == 0:
            palindrome_deque.append(i * (j // 2))
        else:
            odd_number_char = i
            palindrome_deque.append(i * ((j - 1) // 2))
    print(*palindrome_deque, odd_number_char, *palindrome_deque.__reversed__(), sep="")