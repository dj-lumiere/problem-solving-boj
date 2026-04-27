import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    change_table = {i:int(j) for  i, j in zip("A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z".split(), "3	2	1	2	3	3	3	3	1	1	3	1	3	3	1	2	2	2	1	2	1	1	2	2	2	1".split())}
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = input().decode()
        answer = 0
        for v in n:
            answer = answer + change_table[v] % 10
        if answer % 2 == 1:
            answers[i] = "I'm a winner!"
        else:
            answers[i] = "You're the winner?"
    print(answers)