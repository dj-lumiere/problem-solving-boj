from sys import stdin, stdout

def pokemon_finder():
    N, M = list(map(int, input().split(" ")))
    pokedex_by_name = dict()
    pokedex_by_num = dict()
    for i in range(1, N+1):
        pokemon_name = stdin.readline().rstrip()
        pokedex_by_name[pokemon_name] = i
        pokedex_by_num[i] = pokemon_name
    for j in range(M):
        pokemon_find = stdin.readline().rstrip()
        if is_int(pokemon_find):
            stdout.writelines(f"{pokedex_by_num[is_int(pokemon_find)]}\n")
        else:
            stdout.writelines(f"{pokedex_by_name[pokemon_find]}\n")

def is_int(n):
    try:
        return int(n)
    except ValueError:
        return False

pokemon_finder()