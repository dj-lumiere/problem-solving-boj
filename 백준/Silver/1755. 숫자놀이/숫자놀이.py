from itertools import zip_longest

m, n = map(int, input().split())
n+=1
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_convert = [" ".join([numbers[int(x)] for x in str(y)]) for y in range(m, n)]
words_convert = {v:i for i, v in enumerate(number_convert, start=m)}
number_convert.sort()
result = [str(words_convert[v]) for v in number_convert]
answer = []
for j in zip_longest(*[result[i::10] for i in range(10)], fillvalue=""):
    answer.append(" ".join(j).strip())
print("\n".join(answer))