def atm(draw_time: list[int], waiting_person: int) -> int:
    draw_time.sort()
    time_sum = 0
    for i, time in enumerate(draw_time):
        time_sum += (waiting_person-i)*time
    return time_sum

N = int(input())
p_i = list(map(int, input().split(" ")))

print(atm(p_i, N))