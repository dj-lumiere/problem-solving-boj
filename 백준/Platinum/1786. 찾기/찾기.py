# 1786 찾기


def pattern_match(pattern, text):
    result = []
    M = len(pattern)
    N = len(text)

    longest_prefix_suffix_length = [0] * M
    j = 0
    calculate_lps_length(pattern, M, longest_prefix_suffix_length)

    i = 0
    while (N - i) >= (M - j):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i - j + 1)
            j = longest_prefix_suffix_length[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = longest_prefix_suffix_length[j - 1]
            else:
                i += 1
    return result


def calculate_lps_length(pattern, M, lps):
    longest_prefix_suffix_length = 0

    lps[0] = 0
    i = 1

    while i < M:
        if pattern[i] == pattern[longest_prefix_suffix_length]:
            longest_prefix_suffix_length += 1
            lps[i] = longest_prefix_suffix_length
            i += 1
        else:
            if longest_prefix_suffix_length != 0:
                longest_prefix_suffix_length = lps[longest_prefix_suffix_length - 1]
            else:
                lps[i] = 0
                i += 1


text = input()
pattern = input()
result = pattern_match(pattern, text)
print(len(result))
print(*result)