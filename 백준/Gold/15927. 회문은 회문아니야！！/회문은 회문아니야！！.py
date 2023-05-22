# 15927 회문은 회문아니야!!

from sys import stdin, stdout


def check_palindrome(target: str) -> bool:
    start = 0
    end = len(target) - 1
    while start < end:
        if target[start] != target[end]:
            return False
        start += 1
        end -= 1
    return True


target_string = stdin.readline().strip()
if target_string == target_string[0] * len(target_string):
    stdout.writelines(f"-1\n")
elif check_palindrome(target_string):
    stdout.writelines(f"{len(target_string)-1}\n")
else:
    stdout.writelines(f"{len(target_string)}\n")