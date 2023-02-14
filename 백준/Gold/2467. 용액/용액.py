N = int(input())
acidity_list = list(map(int, input().split(" ")))

def most_neutral_pair(acidity_list:list[int]) -> list[int]:
    lower_ptr = 0
    upper_ptr = N-1
    ptr_pair = [lower_ptr, upper_ptr]
    neutrality = 10000000000
    def binary_search(finding_list, target, init, term) -> int:
        midpoint = init + (term-init+1)//2
        if init == term:
            return init
        elif term-init == 1:
            if abs(finding_list[term]-target) >= abs(finding_list[init]-target):
                return init
            else:
                return term
        else:
            if finding_list[midpoint] < target:
                return binary_search(finding_list, target, midpoint, term)
            else:
                return binary_search(finding_list, target, init, midpoint)
    for i in range(len(acidity_list)-1):
        new_ptr = binary_search(acidity_list, -1*acidity_list[i], i+1, upper_ptr)
        if abs(acidity_list[new_ptr] + acidity_list[i]) < neutrality:
            neutrality = abs(acidity_list[new_ptr] + acidity_list[i])
            ptr_pair = [i, new_ptr]
    return [acidity_list[i] for i in ptr_pair]
print(" ".join(map(str, most_neutral_pair(acidity_list))))