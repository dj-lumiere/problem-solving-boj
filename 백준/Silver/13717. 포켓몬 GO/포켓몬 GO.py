import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        pokemons = [(input().decode(), int(input()), int(input())) for _ in range(n)]
        pokemon_name = ""
        current_count = 0
        max_evolution_count = -1
        for name, k, m in pokemons:
            evolution_count = 0
            while m >= k:
                m -= k
                evolution_count += 1
                m += 2
            current_count += evolution_count
            if evolution_count > max_evolution_count:
                pokemon_name = name
                max_evolution_count = evolution_count
        answers[i] = f"{current_count}\n{pokemon_name}"
    print(answers)
