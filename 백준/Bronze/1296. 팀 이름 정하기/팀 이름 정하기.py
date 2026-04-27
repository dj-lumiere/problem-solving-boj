def score(names: str):
    L, O, V, E = names.count("L"), names.count("O"), names.count("V"), names.count("E")
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100


yeondu_name = input()
N = int(input())
team_names = sorted([input() for _ in range(N)])
winning_possibility = [score(yeondu_name + i) for i in team_names]
answer = team_names[winning_possibility.index(max(winning_possibility))]
print(answer)
