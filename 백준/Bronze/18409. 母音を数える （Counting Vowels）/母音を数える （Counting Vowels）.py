# 18409 母音を数える (Counting Vowels)

N = int(input())
S = input()
print(sum([i in ["a", "e", "i", "o", "u"] for i in S]))