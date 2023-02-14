import sys

t = int(sys.stdin.readline().rstrip("\n"))

def sol(_h_ : int, _w_ : int, _n_ : int) -> str:
    _y_ = (_n_ - 1) % _h_ + 1
    _x_ = (_n_ - 1) // _h_ + 1
    _room_number_ = int(f"{_y_}{_x_:0>2}")
    return _room_number_

for i in range(t):
    h, w, n = list(map(int, sys.stdin.readline().split(" ")))
    print(sol(h, w, n))