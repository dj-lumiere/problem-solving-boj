not_pinary_list = [0 for i in range(90+1)]
not_pinary_list[2] = 1
def not_pinary_count(digits : int) -> int:
    if digits == 1:
        return 1
    else:

        case_11 = 2 ** (digits - 2)
        case_10_element = 0
        case_0 = 2 ** (digits - 1)

        for i in range(2, digits - 2 + 1):
            if i == 2:
                case_10_element += 1
            else:
                if not not_pinary_list[i]:
                    case_10_element += not_pinary_count(i) - 2 ** (i-1)
                else:
                    case_10_element += not_pinary_list[i] - 2 ** (i-1)
        if not not_pinary_list[digits]:
            not_pinary_list[digits] = case_11 + case_10_element + case_0
        return case_11 + case_10_element + case_0

n = int(input())

print(2**n - not_pinary_count(n))