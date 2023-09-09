# B번 - 에르다 노바와 오리진 스킬


def skill_hit_count(cooltime, button_press):
    result = 0
    recent_skill_time = -1
    for v in button_press:
        if recent_skill_time == -1:
            recent_skill_time = v
            result += 1
            continue
        if v >= recent_skill_time + cooltime:
            recent_skill_time = v
            result += 1
            continue
    return result


N, M = map(int, input().split())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
A.sort()
B.sort()
print(skill_hit_count(100, A), skill_hit_count(360, B))