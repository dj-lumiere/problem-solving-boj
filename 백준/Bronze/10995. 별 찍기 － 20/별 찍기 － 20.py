N = int(input())
for i in range(N):
    if i % 2:
        print(" *"*N)
    else:
        print((" *"*N)[1:])