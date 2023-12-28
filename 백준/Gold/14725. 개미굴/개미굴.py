# 14725 개미굴


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, items):
        node = self
        for item in items:
            if item not in node.children:
                node.children[item] = TrieNode()
            node = node.children[item]
        node.is_end = True

    def __str__(self, depth=0):
        result = ""
        for item in sorted(self.children.keys()):
            result += (
                "--" * depth
                + item
                + "\n"
                + self.children[item].__str__(depth=depth + 1)
            )
        return result


N = int(input())
root = TrieNode()

for _ in range(N):
    items = input().split()[1:]  # Skip the first count element
    root.insert(items)

print(root)