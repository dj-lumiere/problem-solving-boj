from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    answers = []
    for hh in range(t):
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        count = 0
        nums = [a, b, c, d]
        while not (nums[0] == nums[1] == nums[2] == nums[3]):
            nums = [abs(nums[0]-nums[1]), abs(nums[1]-nums[2]), abs(nums[2]-nums[3]), abs(nums[3]-nums[0])]
            count +=1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")