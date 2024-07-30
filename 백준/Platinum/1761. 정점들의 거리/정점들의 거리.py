from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

MAX_STEP = 20


def find_lca(a, b, depth, ancestor_power_of_2):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(MAX_STEP - 1, -1, -1):
        if depth[b] - depth[a] >= 2 ** i:
            b = ancestor_power_of_2[b][i]
    if a == b:
        return a
    for i in range(MAX_STEP - 1, -1, -1):
        if ancestor_power_of_2[a][i] != ancestor_power_of_2[b][i]:
            a = ancestor_power_of_2[a][i]
            b = ancestor_power_of_2[b][i]
    return ancestor_power_of_2[a][0]


def find_distance(a, b, depth, ancestor_power_of_2, distance_power_of_2):
    distance = 0
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(MAX_STEP - 1, -1, -1):
        if depth[b] - depth[a] >= 2 ** i:
            distance += distance_power_of_2[b][i]
            b = ancestor_power_of_2[b][i]
    if a == b:
        return distance
    for i in range(MAX_STEP - 1, -1, -1):
        if ancestor_power_of_2[a][i] != ancestor_power_of_2[b][i]:
            distance += distance_power_of_2[a][i] + distance_power_of_2[b][i]
            a = ancestor_power_of_2[a][i]
            b = ancestor_power_of_2[b][i]
    distance += distance_power_of_2[a][0] + distance_power_of_2[b][0]
    return distance


def find_cost(a, b, depth, ancestor_power_of_2, cost_power_of_2):
    cost = 0
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(MAX_STEP - 1, -1, -1):
        if depth[b] - depth[a] >= 2 ** i:
            cost += cost_power_of_2[b][i]
            b = ancestor_power_of_2[b][i]
    if a == b:
        return cost
    for i in range(MAX_STEP - 1, -1, -1):
        if ancestor_power_of_2[a][i] != ancestor_power_of_2[b][i]:
            cost += cost_power_of_2[a][i] + cost_power_of_2[b][i]
            a = ancestor_power_of_2[a][i]
            b = ancestor_power_of_2[b][i]
    cost += cost_power_of_2[a][0] + cost_power_of_2[b][0]
    return cost


def find_kth(a, b, k, depth, ancestor_power_of_2, distance_power_of_2):
    lca = find_lca(a, b, depth, ancestor_power_of_2)
    lca_distance_a = find_distance(a, lca, depth, ancestor_power_of_2, distance_power_of_2)
    lca_distance_b = find_distance(b, lca, depth, ancestor_power_of_2, distance_power_of_2)
    if k > lca_distance_a + lca_distance_b:
        return -1
    if k > lca_distance_a:
        a = lca
        k = lca_distance_a + lca_distance_b - k
        for i in range(MAX_STEP - 1, -1, -1):
            if depth[b] - depth[a] >= 2 ** i and k >= 2 ** i:
                k -= distance_power_of_2[b][i]
                b = ancestor_power_of_2[b][i]
        return b
    else:
        b = lca
        for i in range(MAX_STEP - 1, -1, -1):
            if depth[a] - depth[b] >= 2 ** i and k >= 2 ** i:
                k -= distance_power_of_2[a][i]
                a = ancestor_power_of_2[a][i]
        return a


def dfs(adjacent_node, node_distance, N, root):
    NOT_FOUND = -1
    dfs_stack = [(root, NOT_FOUND)]
    depth = [0] * (N + 1)
    ancestor_power_of_2 = [[NOT_FOUND] * MAX_STEP for _ in range(N + 1)]
    cost_power_of_2 = [[NOT_FOUND] * MAX_STEP for _ in range(N + 1)]
    distance_power_of_2 = [[NOT_FOUND] * MAX_STEP for _ in range(N + 1)]
    while dfs_stack:
        current_node, current_parent = dfs_stack.pop()
        ancestor_power_of_2[current_node][0] = current_parent
        cost_power_of_2[current_node][0] = node_distance[(current_node, current_parent)]
        distance_power_of_2[current_node][0] = 1
        for power in range(1, MAX_STEP):
            if ancestor_power_of_2[current_node][power - 1] != NOT_FOUND:
                ancestor_power_of_2[current_node][power] = ancestor_power_of_2[ancestor_power_of_2[current_node][power - 1]][power - 1]
                if ancestor_power_of_2[current_node][power] == NOT_FOUND:
                    continue
                cost_power_of_2[current_node][power] = cost_power_of_2[current_node][power - 1] + cost_power_of_2[ancestor_power_of_2[current_node][power - 1]][power - 1]
                distance_power_of_2[current_node][power] = distance_power_of_2[current_node][power - 1] + distance_power_of_2[ancestor_power_of_2[current_node][power - 1]][power - 1]
        for next_node in adjacent_node[current_node]:
            if next_node == current_parent:
                continue
            depth[next_node] = depth[current_node] + 1
            dfs_stack.append((next_node, current_node))
    return depth, ancestor_power_of_2, distance_power_of_2, cost_power_of_2


# with open(0, 'rb') as f:
with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        N = int(input())
        adjacent_node = [[] for _ in range(N + 1)]
        parent = [-1 for _ in range(N + 1)]
        node_distance = {}
        parent[0] = 0
        for _ in range(N - 1):
            a, b, c = int(input()), int(input()), int(input())
            adjacent_node[a].append(b)
            adjacent_node[b].append(a)
            parent[b] = a
            node_distance[(a,b)] = c
            node_distance[(b,a)] = c
        root = parent.index(-1)
        node_distance[(root, -1)]=0
        depth, ancestor_power_of_2, distance_power_of_2, cost_power_of_2 = dfs(adjacent_node, node_distance, N, root)
        M = int(input())
        for _ in range(M):
            q = 1
            answer = 0
            if q == 1:
                u, v = int(input()), int(input())
                answer = find_cost(u, v, depth, ancestor_power_of_2, cost_power_of_2)
            if q == 2:
                u, v, k = int(input()), int(input()), int(input()) - 1
                answer = find_kth(u, v, k, depth, ancestor_power_of_2, distance_power_of_2)
            answers.append(f"{answer}")
    print(answers)