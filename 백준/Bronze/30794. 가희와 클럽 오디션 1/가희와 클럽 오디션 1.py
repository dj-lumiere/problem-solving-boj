lv,judgement = input().split()
score={"miss":0, "bad":200, "cool": 400, "great": 600, "perfect":1000}
print(int(lv)*score[judgement])