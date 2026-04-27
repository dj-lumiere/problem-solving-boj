n = int(input())
divisors = [1]
for i in range(2, int((n+1)**.5)+1):
    if (n+1)%i==0:
        divisors.append(i)
        if i != (n+1)//i: divisors.append((n+1)//i)
divisors.sort()
print(*divisors)