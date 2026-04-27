n = int(input())
while True:
    x = int(input())
    if not x:
        break
    print(f'{x} is {"NOT " if x%n else ""}a multiple of {n}.')