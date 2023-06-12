def sol2():
    while True:
        N = int(input())
        if N == -1:
            break
        elif N == 6:
            print("6 = 1 + 2 + 3")
        elif N == 28:
            print("28 = 1 + 2 + 4 + 7 + 14")
        elif N == 496:
            print("496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248")
        elif N == 8128:
            print(
                "8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"
            )
        else:
            print(f"{N} is NOT perfect.")
            
sol2()