from itertools import product
sound_match = {i:[] for i in product("ABCDEFG", repeat=3)}
n,m= map(int, input().split())
for _ in range(n):
    song_info = input().split()
    _, song_name, a1, a2, a3, *left = song_info
    sound_match[(a1,a2,a3)].append(song_name)
for _ in range(m):
    pattern = tuple(input().split())
    if not sound_match[pattern]:
        print("!")
    elif len(sound_match[pattern])>1:
        print("?")
    else:
        print(sound_match[pattern][0])