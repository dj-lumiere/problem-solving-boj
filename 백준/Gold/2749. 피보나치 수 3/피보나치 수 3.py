answer = [0, 1]
for _ in range(1500000):
    answer.append(sum(answer[-2:]) % 1000000)
n = int(input())
print(answer[n % 1500000])