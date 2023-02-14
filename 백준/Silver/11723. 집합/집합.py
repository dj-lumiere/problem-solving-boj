import sys

def set_implementation():
    N = int(sys.stdin.readline())
    user_set = [False for i in range(20+1)]
    set_size = 0
    for i in range(N):
        opcode = sys.stdin.readline().rstrip()
        try:
            opcode, operand = opcode.split(" ")
            operand = int(operand)
            if opcode == "add":
                if not user_set[operand]:
                    user_set[operand] = True
                    set_size += 1
            elif opcode == "remove":
                if user_set[operand]:
                    user_set[operand] = False
                    set_size -= 1
            elif opcode == "check":
                if user_set[operand]:
                    sys.stdout.writelines("1\n")
                else:
                    sys.stdout.writelines("0\n")
            elif opcode == "toggle":
                if user_set[operand]:
                    user_set[operand] = False
                    set_size -= 1
                else:
                    user_set[operand] = True
                    set_size += 1
        except:
            if opcode == "all":
                user_set = [True for i in range(0,20+1)]
                set_size = 20
            elif opcode == "empty":
                user_set = [False for i in range(0,20+1)]
                set_size = 0

set_implementation()