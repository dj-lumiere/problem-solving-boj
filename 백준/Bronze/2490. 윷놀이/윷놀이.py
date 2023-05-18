while True:
    try:
        yut = sum(list(map(int, input().split(" "))))
        print(chr(3-yut+ord("A")) if yut-4 else "E")
    except:
        break