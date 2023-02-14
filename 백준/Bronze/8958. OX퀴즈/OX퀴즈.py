while True:
    try:
        question_count = int(input())
        successive_answers = 0
        for i in range(question_count):
            score = 0
            answers = input() + "X"
            for j in range(len(answers)):
                if answers[j] == "O":
                    successive_answers += 1
                    score += successive_answers
                    if answers[j+1] == "X":
                        successive_answers = 0
                else:
                    successive_answers = 0
            print(score)
    except:
        break