x, y, w, h = list(map(int, input().split(" ")))

def square_dist(pos_x: int, pos_y: int, sq_width: int, sq_height: int) -> int:
    dist = [pos_x, pos_y, abs(sq_height-y), abs(sq_width-x)]
    return min(dist)

print(square_dist(x,y,w,h))
