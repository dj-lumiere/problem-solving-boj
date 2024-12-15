n = int(input())
low = 0
high = n + 1
answer = 0
while low + 1 < high:
    mid = (low + high) // 2
    print(f"? {mid}")
    response = int(input())
    if response == 0:
        answer = mid
        break
    elif response == -1:
        low = mid
    else:
        high = mid
print(f"= {answer}")