# E번 - 가지 사진 찾기

# 시작지점과 끝지점을 이분탐색이긴 한데 대체 뭘 어떻게 해야하냐가 포인트
# 딱 두 번의 이분탐색만에 끝내야함
# 가지가 과반수를 넘긴다 -> 정확히 반에 해당하는 위치에 가지가 무조건 위치
# -> 그녀석이 가지이므로, 가지가 아닌 놈이 나오면 값을 올리고, 가지인 놈이 나오면 값을 내린다
N = int(input())
# output이 query, input이 answer
# 1st query
print(f"? {(N+1)//2}", flush=True)
gaji_name = input()
first_bs_start = 0
first_bs_end = (N + 1) // 2
second_bs_start = (N + 1) // 2
second_bs_end = N + 1
# 왼쪽 쿼리와 오른쪽 쿼리 진행
while first_bs_start + 1 != first_bs_end:
    first_bs_mid = (first_bs_start + first_bs_end) // 2
    print(f"? {first_bs_mid}", flush=True)
    if input() != gaji_name:
        first_bs_start = first_bs_mid
    else:
        first_bs_end = first_bs_mid
while second_bs_start + 1 != second_bs_end:
    second_bs_mid = (second_bs_start + second_bs_end) // 2
    print(f"? {second_bs_mid}", flush=True)
    if input() != gaji_name:
        second_bs_end = second_bs_mid
    else:
        second_bs_start = second_bs_mid
print(f"! {first_bs_end} {second_bs_start}")