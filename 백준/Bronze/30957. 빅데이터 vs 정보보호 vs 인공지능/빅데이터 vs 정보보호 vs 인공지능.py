N = int(input())
interest_list = input()
interest_student = {"B":0, "S":0, "A":0}
for interest in interest_list:
    interest_student[interest] += 1
max_interest = max(interest_student.values())
result = "".join(i for i in "BSA" if interest_student[i] == max_interest)
if result == "BSA":
    result = "SCU"
print(result)