# 15087 DRM Messages

A_IN_ASCII = ord("A")


def find_alphabet_position(target: str) -> int:
    return ord(target) - A_IN_ASCII


def divide_message(target: list[int]) -> list[list[int]]:
    partition = len(target) // 2
    return [target[:partition], target[partition:]]


def rotate_message(target1: list[int]) -> list[int]:
    offset = sum(target1) % 26
    return [(i + offset) % 26 for i in target1]


def merge_message(target1: list[int], target2: list[int]) -> list[int]:
    return [(i + j) % 26 for i, j in zip(target1, target2)]


def find_positionth_alphabet(pos: int) -> str:
    return chr(A_IN_ASCII + pos)


def decrypt_message(target: str) -> str:
    positions = list(map(find_alphabet_position, target))
    division = divide_message(positions)
    message_after_division = [rotate_message(i) for i in division]
    message_after_merge = merge_message(*message_after_division)
    return "".join(map(find_positionth_alphabet, message_after_merge))


encrypted_message = input()
print(decrypt_message(encrypted_message))