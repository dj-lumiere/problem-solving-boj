n = int(input())
s = list(input())
numbers = [int(j) for j in s[::2]]
ops = [j for j in s[1::2]]
max_answer = -(2**32)

for mask in range(1<<(n//2)):
    prior_ops = [mask&(1<<i)!=0 for i in range(n//2)]
    numbers2 = numbers[:]
    ops2 = ops[:]
    if any(i and j for i, j in zip(prior_ops, prior_ops[1:])):
        continue
    precalculated = 0
    for i, v in enumerate(prior_ops):
        if v:
            a = numbers2.pop(i - precalculated)
            b = numbers2.pop(i - precalculated)
            op = ops2.pop(i - precalculated)
            if op=="+":
                numbers2.insert(i - precalculated,a+b)
            elif op=="-":
                numbers2.insert(i - precalculated,a-b)
            elif op=="*":
                numbers2.insert(i - precalculated,a*b)
            precalculated += 1
    answer = numbers2[0]
    for a, op in zip(numbers2[1:], ops2):
        if op == "+":
            answer += a
        if op == "-":
            answer -= a
        if op == "*":
            answer *= a
    max_answer = max(max_answer, answer)
print(max_answer)