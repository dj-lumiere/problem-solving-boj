# 30801 가희와 클럽 오디션 2

import re

key_mapper = {
    "LU!": 3,
    "LD!": 9,
    "RU!": 1,
    "RD!": 7,
    "W!": 2,
    "A!": 6,
    "S!": 8,
    "D!": 4,
    "LU": 7,
    "LD": 1,
    "RU": 9,
    "RD": 3,
    "W": 8,
    "A": 4,
    "S": 2,
    "D": 6,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

pattern = "(LU!|LD!|RU!|RD!|W!|A!|S!|D!|LU|LD|RU|RD|W|A|S|D|1|2|3|4|6|7|8|9)"

notes = [key_mapper[i] for i in re.split(pattern, input()) if i in key_mapper]
pressed_keys = [key_mapper[i] for i in re.split(pattern, input()) if i in key_mapper]
correct_streak = 0
for i, key in enumerate(pressed_keys):
    if correct_streak >= len(notes) or key != notes[correct_streak]:
        correct_streak = 0
    elif key == notes[correct_streak]:
        correct_streak += 1
print("Yes" if correct_streak == len(notes) else "No")