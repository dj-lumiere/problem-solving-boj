# 4779 칸토어 집합

def find_cantor_set(order: int) -> str:
    cantor_set_length = 3**order
    result = ["-"]*cantor_set_length
    if order == 0:
        return "".join(result)
    stack = [(0, cantor_set_length)]
    while stack:
        current_position, window_length = stack.pop()
        if window_length == 1:
            continue
        crop_start = current_position + window_length//3
        crop_end = crop_start + window_length//3
        result[crop_start:crop_end] = [" "] * (crop_end-crop_start)
        stack.append((current_position, window_length//3))
        stack.append((current_position + 2*window_length//3, window_length//3))
    return "".join(result)

while True:
    try:
        N = int(input())
        print(find_cantor_set(N))
    except:
        break