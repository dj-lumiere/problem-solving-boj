from sys import stdin, stdout
N = int(input())
for _ in range(N):
    x = int(stdin.readline())
    difference = 2**(x.bit_length() + 1)
    index = [x.bit_length() - 1, x.bit_length() - 1]
    for i in range(x.bit_length() - 1, -1, -1):
        for j in range(x.bit_length() - 1, i - 1, -1):
            difference_sub = abs(2**j + 2**i - x)
            if difference_sub <= difference:
                difference = difference_sub
                index = [i, j]
    stdout.write(f"{index[0]} {index[1]}\n")