N = int(input())
topping = list(input())
strawberry_slice_sub = sum([i=="s" for i in topping[:N//2]])
kiwi_slice_sub = sum([i=="k" for i in topping[:N//2]])
if strawberry_slice_sub == kiwi_slice_sub == N//4:
    print(f"1\n{N//2}")
else:
    answer = 0
    for i, v in enumerate(topping):
        if i >= N // 2:
            break
        if v == "s":
            strawberry_slice_sub -= 1
        elif v == "k":
            kiwi_slice_sub -= 1
        if topping[i + N // 2] == "s":
            strawberry_slice_sub += 1
        elif topping[i + N // 2] == "k":
            kiwi_slice_sub += 1
        if strawberry_slice_sub == kiwi_slice_sub == N // 4:
            answer = i + 1
            break
    print(f"2\n{answer} {answer + N // 2}")