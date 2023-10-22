# 6841 I Speak TXTMSG

substitute = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later",
}

while True:
    try:
        word = input()
        if word not in substitute:
            print(word)
        else:
            print(substitute[word])
    except:
        break