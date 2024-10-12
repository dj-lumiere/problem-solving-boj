from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = int(input())
    answers = []
    for hh in range(1, x + 1):
        cards = []
        for i in range(4):
            card = input()
            cards.append(card)
        m_cards = []
        p_cards = []
        s_cards = []
        for card in cards:
            number = int(card[:-1])
            letter = card[-1]
            if letter == 'm':
                m_cards.append(number)
            elif letter == 'p':
                p_cards.append(number)
            elif letter == 's':
                s_cards.append(number)


        def has_consecutive_three(card_set):
            unique_cards = sorted(set(card_set))
            for i in range(len(unique_cards) - 2):
                if unique_cards[i] + 1 == unique_cards[i + 1] and unique_cards[i + 1] + 1 == unique_cards[i + 2]:
                    return True
            return False


        rest_day = False
        if has_consecutive_three(m_cards) or has_consecutive_three(p_cards) or has_consecutive_three(s_cards):
            rest_day = True
        card_count = {}
        for card in cards:
            if card not in card_count:
                card_count[card] = 0
            card_count[card] += 1
        for key in card_count:
            if card_count[key] >= 3:
                rest_day = True
        pairs = 0
        for key in card_count:
            if card_count[key] >= 2:
                pairs += 1
        if pairs >= 2:
            rest_day = True
        if rest_day:
            answers.append(":)")
        else:
            answers.append(":(")
    print(*answers, sep="\n")