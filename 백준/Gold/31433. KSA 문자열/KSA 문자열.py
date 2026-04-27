x = list(input())

answers = []
for a in range(3):
    letter_found = 0
    current_index = a
    answer = 2 * a
    indices = []
    for i, v in enumerate(x):
        if "KSA"[current_index] == v:
            letter_found += 1
            current_index += 1
            current_index %= 3
            indices.append(i)
            continue
    answers.append(answer + max(0, len(x) - letter_found - a) * 2)
print(min(answers))