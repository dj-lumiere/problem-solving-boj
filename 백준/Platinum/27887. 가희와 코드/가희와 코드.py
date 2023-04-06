# 27887 가희와 코드

from re import split
from collections import deque
from sys import stdin

# >>> 런타임 전 전처리 파트 <<<

# 조심해야할 거, B#, C$, E#, F$은 안 나옴
# 12음계 리스트 정리
tone_list: list[str] = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
tone_dict: dict[str, int] = {j: i for (i, j) in enumerate(tone_list)}

# 내림음은 올림음으로 교체 (사전상 올림음이 앞에 나올 수밖에 없기 때문에 일단 미리 배제함)
tone_replace_list: dict[str, str] = {
    "D$": "C#",
    "E$": "D#",
    "G$": "F#",
    "A$": "G#",
    "B$": "A#",
}

# 코드들을 사전순으로 정리
chord_list: list[str] = (
    [i + "M" for i in tone_list]
    + [i + "m" for i in tone_list]
    + [i + "aug" for i in tone_list]
    + [i + "dim" for i in tone_list]
)
chord_list.sort()

# Major는 4subtone씩 올린거 (X, X+4, X+7)
# minor는 2번 음을 하나 내린거 (X, X+3, X+7)
# aug는 5음을 하나 올린거 (X, X+4, X+8)
# dim은 3음, 5음을 하나 내린거 (X, X+3, X+6)
major_chord = lambda x: ((x + 0) % 12, (x + 4) % 12, (x + 7) % 12)
minor_chord = lambda x: ((x + 0) % 12, (x + 3) % 12, (x + 7) % 12)
augmented_chord = lambda x: ((x + 0) % 12, (x + 4) % 12, (x + 8) % 12)
diminshed_chord = lambda x: ((x + 0) % 12, (x + 3) % 12, (x + 6) % 12)

# 코드에 따라 나오는 음들을 미리 다 정리해두기
chord_tone_dict: dict[str, tuple] = dict()
tone_chord_dict: dict[int, list[str]] = dict()
for i in range(12):
    tone_chord_dict[i] = []
for i in chord_list:
    if i[-3:] == "aug":
        chord_tone_dict[i] = augmented_chord(tone_dict[i[:-3]])
    elif i[-3:] == "dim":
        chord_tone_dict[i] = diminshed_chord(tone_dict[i[:-3]])
    elif i[-1] == "M":
        chord_tone_dict[i] = major_chord(tone_dict[i[:-1]])
    elif i[-1] == "m":
        chord_tone_dict[i] = minor_chord(tone_dict[i[:-1]])

# 음에 따른 코드들 미리 다 정리해두기
for (i, (j, k, l)) in chord_tone_dict.items():
    tone_chord_dict[j].append(i)
    tone_chord_dict[k].append(i)
    tone_chord_dict[l].append(i)
for i in range(12):
    tone_chord_dict[i].sort()


# >>> 실제 로직 진행 파트 <<<

# k마디까지 코드가 몇 번 등장하는지 정리
chord_frequency_list: dict[str, int] = dict()
for i in chord_list:
    chord_frequency_list[i] = 0

# k마디까지의 코드 정리
chord_memo: deque[str] = deque()
chord_memo_len: int = 0

m, p, k = list(map(int, stdin.readline().strip().split()))
for _ in range(m):

    # 음들을 parsing
    tones_sub: list[str] = split(r"(C|D|E|F|G|A|B)", stdin.readline().strip())
    tones: list[str] = []
    for i in tones_sub:
        if not i:
            continue
        elif i in ["C", "D", "E", "F", "G", "A", "B"]:
            tones.append(i)
        elif i[-1] in ["$", "#"]:
            tones[-1] += i[-1]
    for (i, j) in enumerate(tones):
        if j in tone_replace_list:
            tones[i] = tone_replace_list[j]

    # 코드를 조사
    # k번 이상 나온 코드는 아예 선택에서 배제될 수밖에 없게 함
    chord_count: dict[str, int] = {
        j: -5000000 if chord_frequency_list[j] >= k else 0 for j in chord_list
    }

    # 각각의 음에 따라 해당되는 후보군이 어떤지 조사
    for i in tones:
        for j in tone_chord_dict[tone_dict[i]]:
            if chord_frequency_list[j] < k:
                chord_count[j] += 1

    # 선택에서 배제된 코드 제외하고 가장 음이 자주 겹치는 코드를 조사
    maximum_count_for_measure: int = max([j for (i, j) in chord_count.items()])
    # 만약 모든 코드가 배제되었다면 마지막으로 사용한 코드를 활용
    if maximum_count_for_measure == -5000000:
        print(chord_memo[0])
        chord_memo.append(chord_memo[0])
        chord_memo_len += 1
        chord_frequency_list[chord_memo[0]] += 1

    # 그렇지 않다면 코드들을 순회하면서 최대로 많이 겹치는 코드가 어떤건지 확인
    else:
        for i in chord_count:
            if (
                chord_count[i] == maximum_count_for_measure
                and chord_frequency_list[i] < k
            ):
                print(i)
                chord_memo.append(i)
                chord_memo_len += 1
                chord_frequency_list[i] += 1
                break

    # queue가 꽉차면 하나씩 밀면서 지우기
    if chord_memo_len > p:
        chord_to_remove = chord_memo.popleft()
        chord_frequency_list[chord_to_remove] -= 1
        chord_memo_len -= 1
