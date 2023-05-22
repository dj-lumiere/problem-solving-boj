# 28708 중력 큐

from collections import deque
from sys import stdin, stdout


input = stdin.readline
print = stdout.write


class GravitationalQueue:
    global FRONT_AT_DOWN, FRONT_AT_LEFT, FRONT_AT_RIGHT, FRONT_AT_UP, BALL, WALL, ROTATE_CLOCKWISE, ROTATE_COUNTER_CLOCKWISE
    FRONT_AT_RIGHT = 0
    FRONT_AT_DOWN = 1
    FRONT_AT_LEFT = 2
    FRONT_AT_UP = 3
    ROTATE_CLOCKWISE = 1
    ROTATE_COUNTER_CLOCKWISE = 3
    BALL = "BALL"
    WALL = "WALL"

    def __init__(self):
        self.orientation = FRONT_AT_RIGHT
        self.value = deque()
        self.ball_count = 0
        self.wall_count = 0

    def __str__(self):
        a = " ".join(self.value)
        if self.orientation == FRONT_AT_DOWN:
            return f"FRONT(DOWN) {a} BACK(UP)"
        if self.orientation == FRONT_AT_LEFT:
            return f"FRONT(LEFT) {a} BACK(RIGHT)"
        if self.orientation == FRONT_AT_UP:
            return f"FRONT(UP) {a} BACK(DOWN)"
        if self.orientation == FRONT_AT_RIGHT:
            return f"FRONT(RIGHT) {a} BACK(LEFT)"

    def __len__(self):
        return self.ball_count + self.wall_count

    def append(self, _object):
        if _object == BALL:
            self.append_ball()
        if _object == WALL:
            self.append_wall()

    def append_ball(self):
        self.value.append(BALL)
        self.ball_count += 1
        self.gravity_ball_drop()

    def append_wall(self):
        self.value.append(WALL)
        self.wall_count += 1

    def pop_front(self):
        if len(self):
            pop_result = self.value.popleft()
            if pop_result == WALL:
                self.wall_count -= 1
                self.gravity_ball_drop()
            if pop_result == BALL:
                self.ball_count -= 1

    def gravity_ball_drop(self):
        if self.orientation == FRONT_AT_DOWN:
            if self.wall_count:
                while self.value[0] == BALL:
                    self.ball_count -= 1
                    self.value.popleft()
            else:
                self.value.clear()
                self.ball_count = 0
        if self.orientation == FRONT_AT_UP:
            if self.wall_count:
                while self.value[-1] == BALL:
                    self.ball_count -= 1
                    self.value.pop()
            else:
                self.value.clear()
                self.ball_count = 0

    def rotate_clockwise(self):
        self.orientation += ROTATE_CLOCKWISE
        self.orientation %= 4
        self.gravity_ball_drop()

    def rotate_counter_clockwise(self):
        self.orientation += ROTATE_COUNTER_CLOCKWISE
        self.orientation %= 4
        self.gravity_ball_drop()

    def count_ball(self):
        return self.ball_count

    def count_wall(self):
        return self.wall_count


Q = int(input().strip())
my_gravitational_queue = GravitationalQueue()
for _ in range(Q):
    operator, *operand = input().strip().split(" ")
    if operator == "push" and operand[0] == "b":
        my_gravitational_queue.append("BALL")
    if operator == "push" and operand[0] == "w":
        my_gravitational_queue.append("WALL")
    if operator == "count" and operand[0] == "b":
        print(f"{my_gravitational_queue.count_ball()}\n")
    if operator == "count" and operand[0] == "w":
        print(f"{my_gravitational_queue.count_wall()}\n")
    if operator == "pop":
        my_gravitational_queue.pop_front()
    if operator == "rotate" and operand[0] == "l":
        my_gravitational_queue.rotate_counter_clockwise()
    if operator == "rotate" and operand[0] == "r":
        my_gravitational_queue.rotate_clockwise()