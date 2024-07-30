has_appeared = set()
n, s = input().split()
discarded = 0
answer = ""
for v in s:
    if v in has_appeared: discarded += 1
    else: answer += v;has_appeared.add(v)
answer = str(1906+int(n))+answer+str(discarded+4)
answer = "smupc_" + answer[::-1]
print(answer)