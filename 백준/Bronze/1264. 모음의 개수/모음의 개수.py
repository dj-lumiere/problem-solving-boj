# 1264 모음의 개수

vowels = ["a","e","i","o","u","A","E","I","O","U"]

while True:
    sentence = list(input())
    if sentence == ["#"]:
        break
    else:
        print(sum([l in vowels for l in sentence]))