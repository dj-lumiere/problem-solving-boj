def stick(length:int) -> int:
    split_stick = 64
    stick_count = 0
    while split_stick >= 1:
        if length < split_stick:
            split_stick = split_stick // 2
        elif length >= split_stick:
            length = length - split_stick
            stick_count += 1
    return stick_count

print(stick(int(input())))