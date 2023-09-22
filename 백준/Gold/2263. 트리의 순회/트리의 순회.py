# 2263 트리의 순회
# 포스트오더의 마지막 자리가 루트임
# 인오더에서 루트 왼쪽은 왼쪽 트리 오른쪽은 오른쪽 트리
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
result = []
inorder = list(map(int, input().split(" ")))
postorder = list(map(int, input().split(" ")))
inorder_dict = {v: i for i, v in enumerate(inorder)}
dfs_stack = [(0, N - 1, 0, N - 1)]
while dfs_stack:
    in_start, in_end, post_start, post_end = dfs_stack.pop()
    if in_start > in_end and post_start > post_end:
        continue
    root = postorder[post_end]
    result.append(root)
    root_pos_inorder = inorder_dict[root]
    left_tree_length = root_pos_inorder - in_start
    right_tree_length = in_end - root_pos_inorder
    left_in_start = in_start
    left_in_end = in_start + left_tree_length - 1
    left_post_start = post_start
    left_post_end = post_start + left_tree_length - 1
    right_in_start = root_pos_inorder + 1
    right_in_end = in_end
    right_post_end = post_end - 1
    right_post_start = left_post_end + 1
    dfs_stack.append((right_in_start, right_in_end, right_post_start, right_post_end))
    dfs_stack.append((left_in_start, left_in_end, left_post_start, left_post_end))
print(*result)