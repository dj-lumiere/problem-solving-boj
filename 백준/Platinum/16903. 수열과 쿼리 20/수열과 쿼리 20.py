from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000


class BitArray:
    def __init__(self, bits):
        self.size = bits
        self.array = bytearray((bits + 7) // 8)

    def __len__(self):
        return self.size

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')

    def set(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        self.array[byte_index] |= (1 << bit_index)

    def clear(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        self.array[byte_index] &= ~(1 << bit_index)

    def get(self, index):
        self._check_index(index)
        byte_index = index // 8
        bit_index = index % 8
        return (self.array[byte_index] >> bit_index) & 1

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self._check_index(index)
        if value:
            self.set(index)
        else:
            self.clear(index)

    def __iter__(self):
        for i in range(self.size):
            yield self[i]

    def __eq__(self, other):
        if isinstance(other, BitArray):
            return self.array == other.array
        raise TypeError(f'Cannot compare BitArray objects to {type(other)}')

    def __hash__(self):
        return hash(sum([v << i for i, v in enumerate(reversed(self))]))

    def __str__(self):
        return str(sum([v << i for i, v in enumerate(reversed(self))]))

    def __repr__(self):
        return str(sum([v << i for i, v in enumerate(reversed(self))])) + " (" + "".join(map(str, map(int, self))) + ")"


class Trie:
    """https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py"""

    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in reversed(word):
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_"]
        for i, (v, node) in enumerate(zip(reversed(word), reversed(nodes[:-1]))):
            if not node[v]:
                del node[v]

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


def int_to_bitarray(number, size=0):
    bitarray = BitArray(max(size, number.bit_length()))
    for i in range(max(size, number.bit_length()), -1, -1):
        if number & (1 << i) != 0:
            bitarray.set(max(size, number.bit_length()) - 1 - i)
    return bitarray


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    MAX_SIZE = 30
    trie = Trie()
    trie.add(int_to_bitarray(0, MAX_SIZE))
    number_counter = {int_to_bitarray(0, MAX_SIZE): 1}
    for hh in range(t):
        q = int(input())
        if q == 1:
            x = int_to_bitarray(int(input()), size=MAX_SIZE)
            trie.add(x)
            if x not in number_counter:
                number_counter[x] = 0
            number_counter[x] += 1
        if q == 2:
            x = int_to_bitarray(int(input()), size=MAX_SIZE)
            number_counter[x] -= 1
            if number_counter[x] == 0:
                trie.__delitem__(x)
        if q == 3:
            x = int(input())
            try_to_find = int_to_bitarray(x, size=MAX_SIZE)
            for i, v in enumerate(try_to_find):
                try_to_find[i] = (False if v else True)
            result = BitArray(bits=MAX_SIZE)
            current_root = trie.root
            for i, v in enumerate(try_to_find):
                result_sub = 0
                if v not in current_root or not current_root[v]:
                    result_sub = (0 if v else 1)
                else:
                    result_sub = v
                result[i] = result_sub
                current_root = current_root[result_sub]
            answer = x ^ int(str(result))
            answers.append(f"{answer}")
    print(answers)