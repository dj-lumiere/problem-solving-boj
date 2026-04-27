n = int(input())
a_base = list(input())
a = list(input())
b_base = list(input())
b = list(input())
if any(i==j and k!=l for i,j,k,l in zip(a_base,b_base,a,b)):
    print("htg!")
else:
    print(*(k for i,j,k in zip(a_base,b_base,a) if i==j), sep="")