# 7579 앱

# 0-1 배낭 문제

N, M = list(map(int, input().split(" ")))
memory_list = [0] + list(map(int, input().split(" ")))
cost_list = [0] + list(map(int, input().split(" ")))

# 최소 비용을 기준으로 표를 짠 다음 어느 하나라도 메모리 한도 넘으면 바로 중단 후 답 리턴

memory_dp_table = [[] for _ in range(N + 1)]

# 앱을 r번째까지 지울 때, cost를 c까지 지불할 수 있다면 확보 가능한 memory의 양을 dp_table에 정리
# 만약 c cost에서 M바이트가 확보되면 답 리턴.
answer = sum(cost_list) + 1
answer_found_check = False

for c in range(sum(cost_list) + 1):
    if not answer_found_check:
        for r in range(N + 1):
            if r == 0:
                memory_dp_table[r].append(0)
                continue
            elif cost_list[r] <= c:
                # r-1번째 앱을 추가로 삭제할 수 있다면 기존에 삭제한 앱에 추가로 r-1번째 앱을 삭제할지, 아니면 r-1번째 앱만 삭제하는게 좋을지 선택 가능
                memory_dp_table[r].append(
                    max(
                        memory_list[r] + memory_dp_table[r - 1][c - cost_list[r]],
                        memory_dp_table[r - 1][c],
                    )
                )
            else:
                # 앱이 삭제가 불가능하면 그냥 기존에 넣었던 플랜이 그대로 되므로, memory_dp_table을 전행의 동열 값으로 채운다.
                memory_dp_table[r].append(memory_dp_table[r - 1][c])
            if memory_dp_table[r][c] >= M and answer > c:
                answer = c
                answer_found_check = True
    else:
        break
print(answer)