
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = list(map(int, input().split()))
offset = [abs(b-a) for a, b in zip(A, B)]
mod= [o%x for o,x in zip(offset, X)]
press_count = [o//x for o,x in zip(offset, X)]
if all(i==0 for i in mod) and (all(i%2==press_count[0]%2 for i in press_count)):
    print(max(press_count))
else:
    print(-1)