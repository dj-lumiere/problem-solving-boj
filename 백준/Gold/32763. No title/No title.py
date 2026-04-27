n = int(input())
signs = [0 for _ in range(n+1)]
multiple_signs = [0 for _ in range(n)]
for i in range(1, n):
    print(f"? {i} * {i+1}")
    multiple_signs[i] = 1 if input() == "+" else -1
#인접한 두 수를 잡고 만약 양수인 게 하나라도 보이면 걔네 둘을 더하기로 잡아서 초기 부호 결정
if any(i==1 for i in multiple_signs):
    idx = multiple_signs.index(1)
    print(f"? {idx} + {idx+1}")
    result = 1 if input() == "+" else -1
    if result == 1:
        signs[idx] = signs[idx+1] = 1
    else: 
        signs[idx] = signs[idx+1] = -1
    for i in reversed(range(1, idx)):
        signs[i] = multiple_signs[i] // signs[i+1]
    for i in range(idx+1, n+1):
        signs[i] = multiple_signs[i-1] // signs[i-1]
#아니면 마지막꺼랑 첫번째껄로 부호 정하기
else:
    print(f"? {1} + {n}")
    result = 1 if input() == "+" else -1
    if result == 1:
        signs[1] = signs[n] = 1
    else: 
        signs[1] = signs[n] = -1
    for i in range(2, n+1):
        signs[i] = multiple_signs[i-1] // signs[i-1]
print(" ".join(["!"]+["+" if v == 1 else "-" for v in signs[1:]]))