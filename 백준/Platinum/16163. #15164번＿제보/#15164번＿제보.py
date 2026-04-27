from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        s = input()
        # Process the array to make this problem always the odd length palindrome finder problem
        s_processed = "#" + "#".join(list(s)) + "#"
        # Radius of the largest palindrome at position `i`
        radius = [0] * len(s_processed)
        n = len(s_processed)
        # Center of the rightmost palindrome
        center = 0
        # Right boundary of the rightmost palindrome
        right = 0

        for i in range(n):
            # Mirror of `i` with respect to center
            mirror = 2 * center - i

            # If `i` is within the right boundary, we can use previously computed values because of symmetry
            if i < right:
                radius[i] = min(right - i, radius[mirror])
                # eprint("1st stage", i, center, right, radius)

            # Expand palindrome centered at `i`
            while (0 <= i - radius[i] - 1 < i + radius[i] + 1 < n  # out-of-bounds check
                   and s_processed[i - radius[i] - 1] == s_processed[i + radius[i] + 1]): # same character at left and right
                radius[i] += 1
            # eprint("2nd stage", i, center, right, radius)

            # If palindrome centered at `i` extends past right, update center and right
            if i + radius[i] > right:
                center = i
                right = i + radius[i]
                # eprint("3rd stage", i, center, right, radius)
            # eprint()
        # eprint(list(map(lambda x: (x + 1) // 2, radius)))
        answer = sum(map(lambda x: (x + 1) // 2, radius))
        answers.append(answer)
    print(*answers, sep="\n")