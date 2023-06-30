# 10162 전자레인지

minimal_button_presses = [0, 0, 0]
button_time = [300, 60, 10]
t = int(input())
if t % 10:
    print(-1)
else:
    for i, v in enumerate(button_time):
        while t >= v:
            t -= v
            minimal_button_presses[i] += 1
    print(*minimal_button_presses)