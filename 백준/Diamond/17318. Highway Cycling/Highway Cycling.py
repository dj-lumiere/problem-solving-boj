# 17318 Highway Cycling
from sys import stdin


def input():
    return stdin.readline().strip()


def a(l, ki, vi, vip):
    return 2 * l * ki * vi * vi * (vi - vip) + 1


# 2lkv^2(v-vi)+1=0 (v>vi)의 해를 이분탐색으로 구함
def find_root(l, ki, vip):
    # 속도가 당연히 vip보단 커야할 것임.
    vi_start = vip
    # 아무튼 뭔가 엄청 큰 수를 집어넣어봄
    vi_end = 99999999.0
    # 이분탐색에서 무한루프를 막기 위해 이렇게 설정함
    iteration = 0
    while iteration < 100:
        vi_mid = (vi_start + vi_end) / 2
        if a(l, ki, vi_mid, vip) <= 0:
            vi_end = vi_mid
        else:
            vi_start = vi_mid
        iteration += 1
    return vi_start


def find_total_energy(s_list, vi_list, vip_list, ki_list):
    return sum(
        [
            ki * (vi - vip) ** 2 * si
            for si, vi, vip, ki in zip(s_list, vi_list, vip_list, ki_list)
        ]
    )


# 등속 운동임을 가정
def find_vi(s_list, vip_list, ki_list, E_U):
    # l을 이분탐색해봄. 라그랑주 방정식 형태가 2lkv^2(v-vi)+1=0 (v>vi)이어서 l은 음수일 것임. (제약조건이 등식이므로 l은 0만 아니면 됨.)
    # 아무튼 뭔가 엄청 작은 수를 집어넣어봄
    l_start = -999999999.0
    # l은 음수일 수 없음
    l_end = 0.0
    vi_list = [0.0] * len(vip_list)
    # 이분탐색에서 무한루프를 막기 위해 이렇게 설정함
    iteration = 0
    while iteration < 100:
        l_mid = (l_start + l_end) / 2
        vi_list = [find_root(l_mid, ki, vip) for ki, vip in zip(ki_list, vip_list)]
        total_energy = find_total_energy(s_list, vi_list, vip_list, ki_list)
        # 에너지 총합이 E보다 크다면 속도를 작게나오는 방향으로 조절해야함. 이때 l의 최소를 줄이게 되면 (절댓값을 늘리게 되면) 해가 조금 더 빨리 떨어짐
        if total_energy > E_U:
            l_end = l_mid
        else:
            l_start = l_mid
        iteration += 1
    return vi_list


# 등속 운동임을 가정
def find_time(s_list, vi_list):
    # s/v의 합 구하기
    return sum(si / vi for si, vi in zip(s_list, vi_list))


N, E_U = map(float, input().split(" "))
N = int(N)
s_list = []
vip_list = []
ki_list = []
for _ in range(N):
    si, ki, vip = map(float, input().split(" "))
    s_list.append(si)
    ki_list.append(ki)
    vip_list.append(vip)
vi_list = find_vi(s_list, vip_list, ki_list, E_U)
print(f"{find_time(s_list, vi_list):.13f}")