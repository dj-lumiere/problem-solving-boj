import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    place_table = "botswana, ethiopia, kenya, namibia, south-africa, tanzania, zambia, zimbabwe".split(", ")
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        places = [input().decode() for _ in range(n)]
        answer = 0
        if "ethiopia" in places:
            answer += 50
        if "tanzania" in places:
            answer += 50
        if "zimbabwe" in places and "zambia" in places and abs(places.index("zimbabwe") - places.index("zambia")) == 1:
            answer += 50
        elif "zimbabwe" in places and "zambia" in places:
            answer += 80
        elif "zimbabwe" in places:
            answer += 30
        elif "zambia" in places:
            answer += 50
        if "kenya" in places:
            answer += 50
        if "south-africa" in places and "namibia" in places and places.index("south-africa") < places.index("namibia"):
            answer += 40
        elif "namibia" in places:
            answer += 140
        answers[i] = f"{answer}"
    print(answers)