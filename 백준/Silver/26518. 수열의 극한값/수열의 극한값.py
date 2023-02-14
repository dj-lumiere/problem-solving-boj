a, b, c, d = list(map(int, input().split(" ")))

def seq_limit(b:int, c:int, a_1:int, a_2:int) -> float:
    return ((b**2+4*c)**0.5+b)/2

print(seq_limit(a,b,c,d))