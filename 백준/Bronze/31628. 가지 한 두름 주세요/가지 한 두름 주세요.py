import os

tokens = list(os.read(0, os.fstat(0).st_size).split())
yes = False
for i in range(10):
    #print(tokens[i::10], tokens[i*10:i*10+10]) 
    if all(tokens[i]==j for j in tokens[i::10]):
        yes=True
        break
    if all(tokens[i*10]==j for j in tokens[i*10:i*10+10]):
        yes=True
        break
print(int(yes))