# 1406 에디터

from sys import stdin

initial_string = list(stdin.readline().strip())
string_before_cursor = initial_string[:]
string_after_cursor = []
N = int(stdin.readline().strip())
string_before_cursor_length = len(initial_string)
string_after_cursor_length = 0
for _ in range(N):
    opcode, *operand = list(stdin.readline().strip().split(" "))
    if opcode == "L" and string_before_cursor_length > 0:
        string_after_cursor.append(string_before_cursor.pop())
        string_before_cursor_length -= 1
        string_after_cursor_length += 1
    elif opcode == "D" and string_after_cursor_length > 0:
        string_before_cursor.append(string_after_cursor.pop())
        string_before_cursor_length += 1
        string_after_cursor_length -= 1
    elif opcode == "B" and string_before_cursor_length:
        string_before_cursor.pop()
        string_before_cursor_length -= 1
    elif opcode == "P":
        string_before_cursor.append(operand[-1])
        string_before_cursor_length += 1
print(*(string_before_cursor + string_after_cursor[::-1]), sep="")