rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
left = "qwertasdfgzxcv"
right = "yuiophjklbnm"
position = {}
for i, v in enumerate(rows):
    for j, v2 in enumerate(v):
        if v2 in left:
            position[v2] = [i, j, 0]
        else:
            position[v2] = [i, j, 1]
sl, sr = input().split()
left_pos = position[sl][:2]
right_pos = position[sr][:2]
s = input()
answer = len(s)
for v in s:
    next_pos = position[v]
    if next_pos[-1] == 0:
        answer += sum(abs(i-j) for i, j in zip(next_pos, left_pos))
        left_pos = next_pos[:2]
    else:
        answer += sum(abs(i - j) for i, j in zip(next_pos, right_pos))
        right_pos = next_pos[:2]
print(answer)