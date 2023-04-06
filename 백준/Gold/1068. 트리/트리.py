# 1068 트리

node_count: int = int(input())
parent_list: list[int] = list(map(int, input().split(" ")))
tree_dict: dict[int, list[int]] = {i: [] for i in range(-1, node_count)}
for (i, j) in enumerate(parent_list):
    tree_dict[j].append(i)
node_to_erase: int = int(input())
answer: int = 0


def erase_all_leaf_node(start: int):
    if not tree_dict[start]:
        tree_dict.pop(start)
    else:
        while tree_dict[start]:
            node_to_erase_next = tree_dict[start].pop()
            erase_all_leaf_node(node_to_erase_next)
        tree_dict.pop(start)


for i in tree_dict:
    if node_to_erase in tree_dict[i]:
        tree_dict[i].remove(node_to_erase)
        erase_all_leaf_node(node_to_erase)
        break

for (i, j) in tree_dict.items():
    if not j and i != -1:
        answer += 1
print(answer)