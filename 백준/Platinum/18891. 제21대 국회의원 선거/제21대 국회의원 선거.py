# 18891 제21대 국회의원 선거
from fractions import Fraction

P, V = list(map(int, input().split(" ")))
party_list: list[str] = []
r_i_list: list[int] = []
vote_number_list: list[int] = []
for _ in range(P):
    party_name, r_i, vote_number = list(map(str, input().split(" ")))
    party_list.append(party_name)
    r_i_list.append(int(r_i))
    vote_number_list.append(int(vote_number))
party_list.append("")
r_i_list.append(253 - sum(r_i_list))
vote_number_list.append(V - sum(vote_number_list))


# (1단계) 30석에 대해 전국단위 준연동(연동비율 50%) 방식으로 각 정당별 연동배분의석수 산정
# 국회의원 정수
N: int = 300
# 의석할당정당이 아닌 정당의 지역구 당선인 수 총합 + 무소속 지역구 당선인 수
R: int = 253 - sum(
    [
        r_i
        for (party_name, r_i, vote_count) in zip(party_list, r_i_list, vote_number_list)
        if party_name
        and (
            r_i >= 5
            or Fraction(vote_count, V - vote_number_list[-1]) >= Fraction(3, 100)
        )
    ]
)

# 해당 정당의 비례대표국회의원선거 득표비율
# 전체 유효표에 대한 득표비율이 아니고, 의석할당정당의 득표수를 모든 의석할당정당의 득표수의 합계로 나누어 다시 산출됨에 주의
new_V: int = sum(
    [
        vote_count
        for (party_name, r_i, vote_count) in zip(party_list, r_i_list, vote_number_list)
        if party_name
        and (
            r_i >= 5
            or Fraction(vote_count, V - vote_number_list[-1]) >= Fraction(3, 100)
        )
    ]
)

p_i_list: list[Fraction] = [
    Fraction(vote_count) / Fraction(new_V)
    if party_name
    and (r_i >= 5 or Fraction(vote_count, V - vote_number_list[-1]) >= Fraction(3, 100))
    else Fraction(0)
    for (party_name, r_i, vote_count) in zip(party_list, r_i_list, vote_number_list)
]

s_i_prime_list_before: list[Fraction] = [
    Fraction((N - R) * p_i - r_i) / Fraction(2)
    for (p_i, r_i) in zip(p_i_list, r_i_list)
]

s_i_prime_list: list[int] = [
    int(s_i_prime) + 1
    if s_i_prime >= 1 and s_i_prime - int(s_i_prime) >= Fraction(1, 2)
    else int(s_i_prime)
    if s_i_prime >= 1
    else 0
    for s_i_prime in s_i_prime_list_before
]

# (2-1단계) 각 정당별 연동배분의석수의 합계 < 30석일 경우 ☞ 잔여의석에 대해 기존 의석배분방식(병립형) 적용 배분
sum_s_i_prime: int = sum(s_i_prime_list)
s_i_list: list[int] = []
s_i_frac_list: list[Fraction] = []
if sum_s_i_prime < 30:
    left_s_i: int = 30 - sum_s_i_prime
    s_i_list: list[int] = [
        s_i_prime + int(left_s_i * p_i)
        for s_i_prime, p_i in zip(s_i_prime_list, p_i_list)
    ]
    s_i_frac_list = [Fraction(left_s_i * p_i) - int(left_s_i * p_i) for p_i in p_i_list]

# (2-2단계) 각 정당별 연동배분의석수의 합계 > 30석 ☞ 각 정당별 연동배분의석수비율대로 배분
elif sum_s_i_prime > 30:
    s_i_list = [int(30 * s_i_prime / sum_s_i_prime) for s_i_prime in s_i_prime_list]
    s_i_frac_list = [
        Fraction(30 * s_i_prime) / Fraction(sum_s_i_prime) - p_i
        for s_i_prime, p_i in zip(s_i_prime_list, s_i_list)
    ]

else:
    s_i_list = s_i_prime_list

if sum(s_i_list) < 30:
    left_seat: int = 30 - sum(s_i_list)
    s_i_cutline: Fraction = sorted(s_i_frac_list, reverse=True)[left_seat - 1]
    for i, s_i_frac in enumerate(s_i_frac_list):
        if i < P and s_i_cutline <= s_i_frac and left_seat >= 1:
            s_i_list[i] += 1
            left_seat -= 1

# (3단계) 17석에 대해 기존 의석배분방식(병립형) 적용 배분

# 정수부만 먼저 배급
t_i_list: list[int] = [int(17 * p_i) for p_i in p_i_list]
t_i_frac_list: list[Fraction] = [
    17 * p_i - t_i for (p_i, t_i) in zip(p_i_list, t_i_list)
]

# 자리가 남으면 소수부가 큰 순서대로
if sum(t_i_list) < 17:
    left_seat: int = 17 - sum(t_i_list)
    t_i_cutline: Fraction = sorted(t_i_frac_list, reverse=True)[left_seat - 1]
    for i, t_i_frac in enumerate(t_i_frac_list):
        if i < P and t_i_frac >= t_i_cutline and left_seat >= 1:
            t_i_list[i] += 1
            left_seat -= 1

answer_list: list[tuple] = sorted(
    [
        (party_name, r_i + s_i + t_i)
        for (party_name, r_i, s_i, t_i) in zip(party_list, r_i_list, s_i_list, t_i_list)
        if party_name
    ],
    key=lambda x: (-x[1], x[0]),
)

print(
    *[f"{party_name} {total_seat}" for (party_name, total_seat) in answer_list],
    sep="\n",
)