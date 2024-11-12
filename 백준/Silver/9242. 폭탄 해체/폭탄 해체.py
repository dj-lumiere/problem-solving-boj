from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        lines = [input() for _ in range(5)]
        num_digits = (len(lines[0]) + 1) // 4
        digits = []
        for d in range(num_digits):
            pattern = tuple(line[d*4:d*4+3] for line in lines)
            digits.append(pattern)
        digit_map = {
            ('***', '* *', '* *', '* *', '***'): '0',
            ('  *', '  *', '  *', '  *', '  *'): '1',
            ('***', '  *', '***', '*  ', '***'): '2',
            ('***', '  *', '***', '  *', '***'): '3',
            ('* *', '* *', '***', '  *', '  *'): '4',
            ('***', '*  ', '***', '  *', '***'): '5',
            ('***', '*  ', '***', '* *', '***'): '6',
            ('***', '  *', '  *', '  *', '  *'): '7',
            ('***', '* *', '***', '* *', '***'): '8',
            ('***', '* *', '***', '  *', '***'): '9'
        }
        number = ''
        invalid = False
        for pattern in digits:
            if pattern in digit_map:
                number += digit_map[pattern]
            else:
                invalid = True
                break
        if invalid:
            answer = "BOOM!!"
        else:
            num = int(number)
            if num % 6 == 0:
                answer = "BEER!!"
            else:
                answer = "BOOM!!"
        answers.append(f"{answer}")
    print(*answers, sep="\n")