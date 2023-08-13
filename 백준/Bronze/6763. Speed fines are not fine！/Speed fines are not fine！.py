# 6763 Speed fines are not fine!


def find_fine(speed: int, speed_limit: int) -> int:
    over_speed = speed - speed_limit
    if over_speed > 30:
        return 500
    if over_speed > 20:
        return 270
    if over_speed > 0:
        return 100
    return 0


speed_limit = int(input())
speed = int(input())
fine = find_fine(speed, speed_limit)
if fine == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print(f"You are speeding and your fine is ${fine}.")