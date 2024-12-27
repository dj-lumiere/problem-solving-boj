from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        mother = input()
        father = input()
        mother_alleles = [mother[i:i+2] for i in range(0,10,2)]
        father_alleles = [father[i:i+2] for i in range(0,10,2)]
        X = int(input())
        for _ in range(X):
            baby_pheno = input()
            possible = True
            for gene_idx in range(5):
                m_a1, m_a2 = mother_alleles[gene_idx]
                f_a1, f_a2 = father_alleles[gene_idx]
                child_alleles = [(m_a1, f_a1), (m_a1, f_a2), (m_a2, f_a1), (m_a2, f_a2)]
                possible_pheno = set()
                for a, b in child_alleles:
                    if a.isupper() or b.isupper():
                        possible_pheno.add(chr(ord('A')+gene_idx))
                    else:
                        possible_pheno.add(chr(ord('a')+gene_idx))
                if baby_pheno[gene_idx] not in possible_pheno:
                    possible = False
                    break
            answer = "Possible baby." if possible else "Not their baby!"
            answers.append(f"{answer}")
    print(*answers, sep="\n")