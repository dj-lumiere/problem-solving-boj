# 2805 나무 자르기

N, M = list(map(int, input().split(" ")))
wood_height = list(map(int, input().split(" ")))

start = 0
end = max(wood_height)
result = 0
cut_height = 0
while start <= end:
    mid = (start+end) // 2
    cut_height = 0
    for i in wood_height:
        if i >= mid:
            cut_height += i - mid
    if cut_height < M:
        end = mid - 1
        
    else:
        result = mid
        start = mid + 1
print(result)