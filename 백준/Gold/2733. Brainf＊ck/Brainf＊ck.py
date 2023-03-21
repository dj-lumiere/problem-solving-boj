# 2733 Brainf*ck


N = int(input())
memory_size = 32768
letter_max = 256
for i in range(1, N + 1):
    answer = ""
    string_to_compile = ""
    pos = -1
    jump_address = dict()
    bracket_stack = []
    while True:
        string_to_compile_sub = input()
        if string_to_compile_sub == "end":
            break
        else:
            for a in string_to_compile_sub:
                if a == "%":
                    break
                elif (
                    a == "+"
                    or a == "-"
                    or a == "["
                    or a == "]"
                    or a == "<"
                    or a == ">"
                    or a == "."
                ):
                    string_to_compile += a
                    pos += 1
                if a == "[":
                    bracket_stack.append((1, pos))
                elif a == "]" and (
                    not bracket_stack or (bracket_stack and bracket_stack[-1][0] != 1)
                ):
                    bracket_stack.append((-1, pos))
                elif a == "]" and bracket_stack[-1][0] == 1:
                    pair_address = bracket_stack.pop()[1]
                    jump_address[pair_address] = pos
                    jump_address[pos] = pair_address
    print(f"PROGRAM #{i}:")
    if bracket_stack:
        print("COMPILE ERROR")
    else:
        j = 0
        subroutine_stack = []
        memory_list = [0 for _ in range(memory_size)]
        address = 0
        while j < len(string_to_compile):
            if string_to_compile[j] == "+":
                memory_list[address] += 1
                if memory_list[address] > letter_max - 1:
                    memory_list[address] %= letter_max
            elif string_to_compile[j] == "-":
                memory_list[address] -= 1
                if memory_list[address] < 0:
                    memory_list[address] %= letter_max
            elif string_to_compile[j] == "[":
                if memory_list[address] == 0:
                    j = jump_address[j]
            elif string_to_compile[j] == "]":
                if memory_list[address] != 0:
                    j = jump_address[j]
            elif string_to_compile[j] == "<":
                address -= 1
                if address < 0:
                    address %= memory_size
            elif string_to_compile[j] == ">":
                address += 1
                if address > memory_size - 1:
                    address %= memory_size
            elif string_to_compile[j] == ".":
                answer += chr(memory_list[address])
            j += 1
        if answer:
            print(answer)
