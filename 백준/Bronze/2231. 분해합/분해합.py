from math import log10

def digit_generator(N:int):
    digit:int = int(log10(N))+1
    generator:list[int] = []
    for i in range(min(N, digit * 9)+1):
        digit_list:list[int] = [((N-i)//(10**j))%10 for j in range(digit)]
        if sum(digit_list) + N - i == N:
            generator.append(N-i)
    if not generator:
        return 0
    else:
        return min(generator)

N = int(input())
print(digit_generator(N))