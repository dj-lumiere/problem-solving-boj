while True:
    try:
        n, x = list(map(int, input().split(" ")))
        seq_a = list(map(int, input().split(" ")))
        seq_b = ""
        for i in seq_a:
            if i < x:
                seq_b += f"{i} "
        print(seq_b[:-1])
    except:
        break