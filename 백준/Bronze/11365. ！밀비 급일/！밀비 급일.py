while True:
    sentence = input()
    if sentence == "END":
        break
    else:
        print(sentence[::-1])