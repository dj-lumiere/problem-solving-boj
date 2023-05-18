N :int = int(input())
print(*[" "*(N-1-i)+"*"*(2*i+1) for i in range(N)], sep="\n")