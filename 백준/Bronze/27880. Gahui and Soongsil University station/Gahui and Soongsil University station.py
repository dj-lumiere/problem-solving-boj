# A번 - Gahui and Soongsil University station

elevator_step:int = 21
stair_step:int = 17
answer:int = 0

for _ in range(4):
    step_category, step_count = input().split(" ")
    if step_category == "Es":
        answer += int(step_count)*elevator_step
    else:
        answer += int(step_count)*stair_step
print(answer)