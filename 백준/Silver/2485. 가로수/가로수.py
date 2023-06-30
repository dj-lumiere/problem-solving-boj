# 2485 가로수
from math import gcd
from sys import stdin

input = stdin.readline
tree_pos = []
N = int(input())
for _ in range(N):
    tree_pos_sub = int(input())
    tree_pos.append(tree_pos_sub)
starting_pos = tree_pos[0]
for i in range(N):
    tree_pos[i] -= starting_pos
maximal_tree_spacing = gcd(*tree_pos[1:])
print((tree_pos[-1] - tree_pos[0]) // maximal_tree_spacing + 1 - N)