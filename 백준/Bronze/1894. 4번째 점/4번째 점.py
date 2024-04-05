import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    while True:
        try:
            a = [(float(input()), float(input())) for _ in range(4)]
            intersect_point = None
            for i, v1 in enumerate(a):
                for j, v2 in enumerate(a):
                    if i == j:
                        continue
                    if v1 == v2:
                        intersect_point = v1
            other_point_middle = [0.0, 0.0]
            for i, v1 in enumerate(a):
                if v1 != intersect_point:
                    other_point_middle[0] += v1[0]
                    other_point_middle[1] += v1[1]
            other_point_middle = [i/2 for i in other_point_middle]
            fourth_point = [i+(j-i)*2 for i, j in zip(intersect_point, other_point_middle)]
            answers.append(f"{fourth_point[0]:.3f} {fourth_point[1]:.3f}")
        except:
            print(answers)
            break
