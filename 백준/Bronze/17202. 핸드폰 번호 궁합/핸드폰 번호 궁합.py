A = input()
B = input()
phone_concat = ""

for i in range(8):
    phone_concat = phone_concat + A[i] + B[i]

memo = [phone_concat, ""]

for j in range(15, 1, -1):
    memo[j%2] = ""
    for k in range(j):
        memo[j%2] = memo[j%2]+str((int(memo[(j-1)%2][k]) + int(memo[(j-1)%2][k+1]))%10)

print(memo[0])