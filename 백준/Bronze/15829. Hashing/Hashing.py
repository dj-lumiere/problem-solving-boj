length = int(input())
string = input()

def hasher(string_to_hash: str, r: int, M: int) -> int:
    hash_value = 0
    r_to_i = 1
    for i, letter in enumerate(string_to_hash):
        if not i:
            r_to_i = 1
        else:
            r_to_i = (r_to_i * r) % M
        hash_value += ((ord(letter) - ord("a") + 1) * r_to_i) % M
        hash_value = hash_value % M
    return hash_value

print(hasher(string, 31, 1234567891))