# 3107 IPv6

ip = input()
ip_split = ip.split(":")
has_omitted_element = False
not_omitted_element_count = sum([not not v for v in ip_split])
result = ["" for _ in range(8)]
current_index = 0
for i, v in enumerate(ip_split):
    if not has_omitted_element and not v:
        has_omitted_element = True
        for j in range(current_index, current_index + 8 - not_omitted_element_count):
            result[j] = "0000"
        current_index += 8 - not_omitted_element_count
        continue
    elif has_omitted_element and not v:
        continue
    result[current_index] = f"{v:0>4}"
    current_index += 1
print(*result, sep=":")