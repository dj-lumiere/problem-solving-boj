s = input()
quote_count = 0
quotes = []
for i, v in enumerate(s):
    if quote_count == 0 and v == r'"':
        quote_count += 1
        quotes.append(i)
    elif quote_count == 1 and v == r'"':
        quote_count += 1
        quotes.append(i)

if s == '"' or s == '""':
    print("CE")
elif quote_count != 2:
    print("CE")
elif quotes != [0, len(s) - 1]:
    print("CE")
elif s[1:-1].strip() == "":
    print("CE")
else:
    print(s[1:-1])