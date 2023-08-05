# 5358 Football Team

def replace_i_to_e(target:str)->str:
    result = ""
    for letter in target:
        if letter == "e":
            result += "i"
        elif letter == "i":
            result += "e"
        elif letter == "E":
            result += "I"
        elif letter == "I":
            result += "E"
        else:
            result += letter
    return result

while True:
    try:
        target = input()
        print(replace_i_to_e(target))
    except:
        break