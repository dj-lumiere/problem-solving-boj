def calculate_digit(end):
    digit_count = 0
    jjam_or_ppong_count = 0
    jjamppong_count = 0
    for i in range(len(str(end))):
        if i == 0:
            for k in range(1, 10):
                if end >= k and k not in (3, 6, 9):
                    digit_count += 1
                elif end >= k and k in (3, 6, 9):
                    jjam_or_ppong_count += 1
            continue
        for j in range(1, 10):
            if j in (3, 6, 9):
                if end >= (j + 1) * 10 ** i:
                    jjam_or_ppong_count += 10 ** (i - 1) * 7
                    jjamppong_count += 10 ** (i - 1) * 3
                elif j * 10 ** i <= end < (j + 1) * 10 ** i:
                    threshold = j * 10 ** i - 1
                    groups = (end - threshold) // 10
                    threshold2 = (end + 1) // 10 * 10
                    jjam_or_ppong_count_sub = groups * 7
                    jjamppong_count_sub = groups * 3
                    for k in range(10):
                        if end - threshold2 >= k and k not in (3, 6, 9):
                            jjam_or_ppong_count_sub += 1
                        elif end - threshold2 >= k and k in (3, 6, 9):
                            jjamppong_count_sub += 1
                    jjam_or_ppong_count += jjam_or_ppong_count_sub
                    jjamppong_count += jjamppong_count_sub
            else:
                if end >= (j + 1) * 10 ** i:
                    groups = 10 ** (i - 1)
                    jjam_or_ppong_count += groups * 3
                    digit_count += groups * (i + 1) * 7
                elif j * 10 ** i <= end < (j + 1) * 10 ** i:
                    threshold = j * 10 ** i - 1
                    groups = (end - threshold) // 10
                    threshold2 = (end + 1) // 10 * 10
                    jjam_or_ppong_count_sub = groups * 3
                    number_count = groups * 7
                    for k in range(10):
                        if end - threshold2 >= k and k not in (3, 6, 9):
                            number_count += 1
                        if end - threshold2 >= k and k in (3, 6, 9):
                            jjam_or_ppong_count_sub += 1
                    jjam_or_ppong_count += jjam_or_ppong_count_sub
                    digit_count += number_count * (i + 1)
    jjam_count = (jjam_or_ppong_count + 1) // 2
    ppong_count = jjam_or_ppong_count - jjam_count
    digit_count += jjam_count * 4 + ppong_count * 5 + jjamppong_count * 9
    return digit_count, jjam_count, ppong_count, jjamppong_count


t = int(input())
answers = []
for hh in range(t):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    start = 0
    end = l + 1
    digit_count = 0
    jjam_count = 0
    ppong_count = 0
    jjamppong_count = 0
    while start + 1 < end:
        mid = (start + end) // 2
        digits, jjam_count_sub, ppong_count_sub, jjamppong_count_sub = calculate_digit(mid)
        if digits > l:
            end = mid
        else:
            start = mid
            digit_count, jjam_count, ppong_count, jjamppong_count = digits, jjam_count_sub, ppong_count_sub, jjamppong_count_sub
    concatenate_string = ""
    for i in range(start + 1, start + 1001):
        if i == 0:
            continue
        starting = False
        ending = False
        for j in (3, 6, 9):
            if str(i).startswith(str(j)):
                starting = True
            if str(i).endswith(str(j)):
                ending = True
        substring = ""
        if len(str(i)) != 1 and starting and ending:
            substring = "JJAMPPONG"
        elif (starting or ending) and jjam_count == ppong_count:
            substring = "JJAM"
            jjam_count += 1
        elif (starting or ending) and jjam_count > ppong_count:
            substring = "PPONG"
            ppong_count += 1
        else:
            substring = str(i)
        if i == start + 1:
            cut_length = l - digit_count
            substring = substring[cut_length:]
        concatenate_string += substring
        if len(concatenate_string) > (r - l + 1):
            concatenate_string = concatenate_string[:(r - l + 1)]
            break
    answers.append(concatenate_string)
print(*answers, sep="\n")