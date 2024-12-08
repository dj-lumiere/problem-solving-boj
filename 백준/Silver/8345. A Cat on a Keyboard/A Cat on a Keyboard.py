from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        s = input()
        s = s.lower()
        mapping = {
            '`':'1','1':'1','2':'1','3':'1','4':'1','5':'1','6':'1','7':'1','8':'1','9':'1','0':'1','-':'1','=':'1',
        'q':'2','w':'2','e':'2','r':'2','t':'2','y':'2','u':'2','i':'2','o':'2','p':'2','[':'2',']':'2','\\':'2',
        'a':'3','s':'3','d':'3','f':'3','g':'3','h':'3','j':'3','k':'3','l':'3',';':'3',"'":'3',
        'z':'4','x':'4','c':'4','v':'4','b':'4','n':'4','m':'4',',':'4','.':'4','/':'4',
        ' ':'5'
        }
        answer = ''.join(mapping.get(c, '') for c in s)
        answers.append(f"{answer}")
    print(*answers, sep="\n")