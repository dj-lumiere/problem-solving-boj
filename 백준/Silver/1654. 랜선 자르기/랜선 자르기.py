# 1654 랜선 자르기

K, N = list(map(int, input().split(" ")))
wire_length: list[int] = [int(input()) for _ in range(K)]

start: int = 0
end: int = 2**31
result: int = 0
cut_length: int = 0
while start + 1 != end:
    mid: int = (start + end) // 2
    wire_count: int = sum([i // mid for i in wire_length])
    if wire_count < N:
        end = mid
    else:
        result = mid
        start = mid
print(result)