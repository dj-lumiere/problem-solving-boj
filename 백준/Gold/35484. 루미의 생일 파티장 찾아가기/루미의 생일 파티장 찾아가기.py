start = 0
n = int(input())
end = (n + 1) // 2 + 1
while start + 1 < end:
    mid = (start + end) // 2
    print(f"? 0 {n} {mid}")
    query_ans = int(input())
    if query_ans == 0:
        start = mid
    else:
        end = mid
print(f"? 1 {n} {end - 1}")
query_ans = int(input())
if query_ans == 0:
    answer = 2 * end
else:
    answer = 2 * end - 1
print(f"! {answer}")