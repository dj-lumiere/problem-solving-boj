# 29163 Счастье Мистера Бина

N = int(input())
numbers = list(map(int, input().split(" ")))
odd_numbers = [i % 2 for i in numbers]
even_numbers = [1 - i for i in odd_numbers]
if sum(odd_numbers) < sum(even_numbers):
    print("Happy")
else:
    print("Sad")