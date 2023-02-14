from collections import deque
import sys

def sol():
    N = int(sys.stdin.readline())
    user_deque : deque = deque()
    user_deque_size = 0
    for i in range(N):
        opcode = sys.stdin.readline().rstrip()
        try:
            opcode, operand = opcode.split(" ")
            if opcode == "push_front":
                user_deque_size += 1
                user_deque.appendleft(int(operand))
            elif opcode == "push_back":
                user_deque_size += 1
                user_deque.append(int(operand))
        except:
            if opcode == "pop_front":
                if user_deque:
                    sys.stdout.writelines(f"{user_deque.popleft()}\n")
                    user_deque_size -= 1
                else:
                    sys.stdout.writelines("-1\n")
            if opcode == "pop_back":
                if user_deque:
                    sys.stdout.writelines(f"{user_deque.pop()}\n")
                    user_deque_size -= 1
                else:
                    sys.stdout.writelines("-1\n")
            elif opcode == "size":
                sys.stdout.writelines(f"{user_deque_size}\n")
            elif opcode == "empty":
                if not user_deque:
                    sys.stdout.writelines("1\n")
                else:
                    sys.stdout.writelines("0\n")
            elif opcode == "front":
                if user_deque:
                    pop_cache = user_deque.popleft()
                    sys.stdout.writelines(f"{pop_cache}\n")
                    user_deque.appendleft(pop_cache)
                else:
                    sys.stdout.writelines("-1\n")
            elif opcode == "back":
                if user_deque:
                    pop_cache = user_deque.pop()
                    sys.stdout.writelines(f"{pop_cache}\n")
                    user_deque.append(pop_cache)
                else:
                    sys.stdout.writelines("-1\n")
sol()