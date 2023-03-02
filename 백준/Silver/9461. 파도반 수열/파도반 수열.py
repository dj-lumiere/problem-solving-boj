# 9461 파도반 수열

# P(1)=P(2)=P(3)=1, P(4)=P(5)=2
# P(n)=P(n-1)+P(n-5) (n>=6)

padovan_list:list[int] = [0,1,1,1,2,2]
for i in range(6, 100+1):
    padovan_list.append(padovan_list[-1]+padovan_list[-5])
T:int = int(input())
for _ in range(T):
    print(padovan_list[int(input())])