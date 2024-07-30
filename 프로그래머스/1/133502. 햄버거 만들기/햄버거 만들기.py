def solution(ingredient):
    answer = 0
    stack = []
    for value in ingredient:
        stack.append(value)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return answer