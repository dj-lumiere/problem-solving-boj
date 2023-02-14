# 4378 트ㅏㅊ;
from sys import stdin

wrong_keys = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "-",
    "=",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "[",
    "]",
    "\\",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    ";",
    "'",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
    ",",
    ".",
    "/",
    " ",
    "\n",
]
right_keys = [
    "`",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "-",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "[",
    "]",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    ";",
    "Z",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
    ",",
    ".",
    " ",
    "\n",
]
keyboard_dict = dict()

for i, j in zip(wrong_keys, right_keys):
    keyboard_dict[i] = j

keyboard_list = []
while True:
    keyboard_list_sub = stdin.readline().rstrip("\n")
    if not keyboard_list_sub:
        break
    else:
        keyboard_list += list(keyboard_list_sub) + ["\n"]
keyboard_list.pop()
for i in keyboard_list:
    print(keyboard_dict[i], end="")
