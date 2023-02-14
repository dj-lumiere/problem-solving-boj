def solution():
    string_list = []
    while True:
        try:
            string_element = input()
            if string_element == "":
                raise EOFError
            else:
                string_list.append(string_element)
        except EOFError:
            break
    angle_count = int(string_list[0])
    angle_init = int(string_list[1])
    angle_correction = list(map(int, string_list[2:]))[::-1]
    angle_compare_1 = angle_init
    angle_compare_2 = 0
    spin_left = 0
    spin_right = 0
    spinning_angle = 0
    for i in range(angle_count):
        angle_compare_2 = int(angle_correction[-1])
        spin_left = abs(angle_compare_1 - angle_compare_2)
        spin_right = -1 * abs(angle_compare_1 - angle_compare_2) + 360
        if spin_left >= spin_right:
            spinning_angle += spin_right
        else:
            spinning_angle += spin_left
        angle_compare_1 = angle_compare_2
        angle_compare_2 = 0
        angle_correction.pop()
    print(spinning_angle)
solution()