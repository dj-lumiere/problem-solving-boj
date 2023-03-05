# 17478 재귀함수가 뭔가요?

n = int(input())
a = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
b = '"재귀함수가 뭔가요?"'
c = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
d = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
e = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
f = '"재귀함수는 자기 자신을 호출하는 함수라네"'
g = "라고 답변하였지."


def recursive_text(i: int):
    if i != n:
        print("_" * 4 * i + b)
        print("_" * 4 * i + c)
        print("_" * 4 * i + d)
        print("_" * 4 * i + e)
        recursive_text(i+1)
        print("_" * 4 * i + g)
    if i == n:
        print("_" * 4 * i + b)
        print("_" * 4 * i + f)
        print("_" * 4 * i + g)
print(a)
recursive_text(0)