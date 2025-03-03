from sys import stderr, stdout

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
    pokemon_types = ["bug", "dark", "dragon", "electric", "fairy", "fighting", "fire", "flying", "ghost", "grass",
                     "ground", "ice", "normal", "poison", "psychic", "rock", "steel", "water"]
    for hh in range(t):
        n = int(input())
        enabled_types = {v: True for v in pokemon_types}
        enabled_types["none"] = False
        sort_order = {"idx": 0, "hp": 0, "atk": 0, "def": 0, "special_atk": 0, "special_def": 0, "speed": 0}
        sorting_order = {"idx": 0, "hp": 0, "atk": 0, "def": 0, "special_atk": 0, "special_def": 0, "speed": 0}
        filter_order = {"idx"        : [1, 200000], "hp": [1, 200000], "atk": [1, 200000], "def": [1,
            200000], "special_atk"   : [1, 200000], "special_def": [1, 200000], "speed": [1, 200000]}
        prefix = ""
        w, h = 5, 5
        offsets = []
        pokemons = [{}]
        for i in range(1, n + 1):
            words = iter(input().split())
            name = next(words)
            type1 = next(words)
            type2 = next(words)
            hp = int(next(words))
            atk = int(next(words))
            _def = int(next(words))
            special_atk = int(next(words))
            special_def = int(next(words))
            speed = int(next(words))
            pokemons.append({"idx": i, "name": name, "type1": type1, "type2": type2, "hp": hp, "atk": atk, "def": _def, "special_atk": special_atk, "special_def": special_def, "speed": speed})
        for i, x in enumerate(pokemons[1:], start=1):
            type1 = x["type1"]
            type2 = x["type2"]
            pokemons[i].pop("type1")
            pokemons[i].pop("type2")
            pokemons[i]["types"] = [type1, type2] if type2 != "none" else [type1]
        # eprint(pokemons)
        m = int(input())
        for i in range(1, m + 1):
            raw_query = input().replace("filter name", "filtername").replace("filter type", "filtertype").split()
            q = iter(raw_query)
            query = next(q)
            # eprint(raw_query)
            if query == "sort":
                subtoken1 = next(q)
                subtoken2 = next(q)
                sort_order[subtoken1] = -1 if subtoken2 == "desc" else 1
                sorting_order[subtoken1] = -i
                offsets.clear()
            elif query == "filter":
                subtoken1 = next(q)
                subtoken2 = next(q)
                subtoken3 = int(next(q))
                if subtoken2 == "min":
                    filter_order[subtoken1][0] = subtoken3
                elif subtoken2 == "max":
                    filter_order[subtoken1][1] = subtoken3
                offsets.clear()
            elif query == "filtername":
                subtoken = next(q)
                if subtoken == "BLANK":
                    prefix = ""
                else:
                    prefix = subtoken
                offsets.clear()
            elif query == "filtertype":
                subtoken = next(q)
                enabled_types[subtoken] ^= True
                offsets.clear()
            elif query == "resize":
                subtoken = next(q)
                if subtoken == "W":
                    w = int(next(q))
                elif subtoken == "H":
                    h = int(next(q))
            elif query == "cursor":
                subtoken = next(q)
                if subtoken == "l":
                    offsets.append(-1)
                if subtoken == "r":
                    offsets.append(1)
                if subtoken == "u":
                    offsets.append(-w)
                if subtoken == "d":
                    offsets.append(w)
            elif query == "flush":
                available_pokemons = []
                for v in pokemons[1:]:
                    if not v["name"].startswith(prefix):
                        continue
                    if not any(enabled_types[v2] for v2 in v["types"]):
                        continue
                    for cond, (l, r) in filter_order.items():
                        if not l <= v[cond] <= r:
                            break
                    else:
                        available_pokemons.append(v["idx"])
                final_sort_order = []
                for k, v in sorted(sorting_order.items(), key=lambda item: item[1]):
                    if v != 0:
                        final_sort_order.append((k, sort_order[k]))
                # eprint(final_sort_order)
                available_pokemons.sort(key=lambda x: [pokemons[x][v1] * v2 for v1, v2 in
                                                       final_sort_order] if sort_order else x)
                # eprint(*[pokemons[i] for i in available_pokemons], sep="\n")
                cursor_offset = 0
                # eprint(cursor_offset)
                for offset in offsets:
                    cursor_offset += offset
                    if cursor_offset < 0:
                        cursor_offset = 0
                    if cursor_offset >= len(available_pokemons):
                        cursor_offset = len(available_pokemons) - 1
                cursor_offset = cursor_offset // w * w
                answer_format = [[0 for _ in range(w)] for _ in range(h)]
                for j, v in enumerate(available_pokemons, start=-cursor_offset):
                    if j < 0:
                        continue
                    y, x = divmod(j, w)
                    if y >= h:
                        break
                    answer_format[y][x] = v
                answers.append("\n".join(" ".join(map(str, v)) for v in answer_format))
    print(*answers, sep="\n\n")