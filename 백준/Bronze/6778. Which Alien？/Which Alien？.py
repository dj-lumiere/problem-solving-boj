# 6778 Which Alien?


def find_alien_type(antenna_count: int, eye_count: int) -> list[str]:
    possible_type = []
    if antenna_count >= 3 and eye_count <= 4:
        possible_type.append("TroyMartian")
    if antenna_count <= 6 and eye_count >= 2:
        possible_type.append("VladSaturnian")
    if antenna_count <= 2 and eye_count <= 3:
        possible_type.append("GraemeMercurian")
    return possible_type


antenna_count = int(input())
eye_count = int(input())
alien = find_alien_type(antenna_count=antenna_count, eye_count=eye_count)
print(*alien, sep="\n")