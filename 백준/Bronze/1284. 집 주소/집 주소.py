def string_length(target):
    letter_length=[4,2,3,3,3,3,3,3,3,3]
    result = 0
    for letter in target:
        result += letter_length[int(letter)]
    result += len(target)+1
    return result

while True:
    target = input()
    if target == "0":
        break
    print(string_length(target))