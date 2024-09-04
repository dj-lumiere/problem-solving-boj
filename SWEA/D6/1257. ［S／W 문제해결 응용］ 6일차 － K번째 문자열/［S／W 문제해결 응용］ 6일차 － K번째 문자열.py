from itertools import combinations
from string import ascii_lowercase


class Trie:
    def __init__(self):
        self.root = {"_": 0}

    def add(self, *letters):
        current = self.root
        if letters in self:
            return
        self.root["_"] += 1
        for i in letters:
            if i not in current:
                current[i] = {"_": 0}
            current[i]["_"] += 1
            current = current[i]

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_" in current_dict

    def __str__(self, current_dict=None, level=0):
        if current_dict is None:
            current_dict = self.root

        indent = " " * (level + 1) * 2
        child_repr = ""
        if current_dict:
            for i, (key, child) in enumerate(sorted(current_dict.items())):
                if key == "_":
                    continue
                child_repr += (f"{indent}child{level + 1}={key}{self.__str__(child, level + 1) if child else chr(10)}")
        else:
            child_repr = f""

        if level == 0:
            return f"root\n{child_repr}"
        else:
            return f"\n{child_repr}"


t = int(input())
answers = []
for hh in range(1, t + 1):
    n = int(input())
    s = input()
    my_trie = Trie()
    for i, j in combinations(range(len(s) + 1), r=2):
        my_trie.add(*s[i:j])
    if my_trie.root["_"] < n:
        answer = "none"
    else:
        answer = ""
        current = my_trie.root
        n -= 1
        for step in range(len(s)):
            letters = [0 for _ in range(27)]
            if step != 0:
                letters[0] = 1
            for i, j in enumerate(ascii_lowercase, start=1):
                if j not in current:
                    letters[i] = letters[i - 1]
                    continue
                letters[i] = letters[i - 1] + current[j]["_"]
            index = 0
            for i, (v1, v2) in enumerate(zip(letters, letters[1:]), start=1):
                if v1 <= n < v2:
                    n -= v1
                    index = i
                    break
            if index == 0:
                break
            answer += ascii_lowercase[index - 1]
            current = current[ascii_lowercase[index - 1]]
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
