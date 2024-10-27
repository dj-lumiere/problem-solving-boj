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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    morse_code = {
        'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.",
        'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
        'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.",
        'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
        'Y': "-.--", 'Z': "--..", '_': "..--", '.': "---.", ',': ".-.-", '?': "----"
    }
    reverse_morse = {v: k for k, v in morse_code.items()}
    t = int(input())
    answers = []
    for hh in range(t):
        encoded_message = input()
        morse_str = ''.join(morse_code[char] for char in encoded_message)
        length_str = ''.join(str(len(morse_code[char])) for char in encoded_message)
        reversed_length_str = length_str[::-1]
        decoded_message, idx = "", 0
        for length in map(int, reversed_length_str):
            decoded_message += reverse_morse[morse_str[idx:idx + length]]
            idx += length
        answer = f"{hh + 1}: {decoded_message}"
        answers.append(answer)
    print(*answers, sep="\n")