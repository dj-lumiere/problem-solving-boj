N, r, c = list(map(int, input().split(" ")))

def z(grid_size: int, row: int, col: int) -> int:
    if not grid_size:
        return 0
    else:
        row_offset = (4**(grid_size-1)) * 2 * (row//(2**(grid_size-1)))
        col_offset = (4**(grid_size-1)) * (col//(2**(grid_size-1)))
        return row_offset + col_offset + z(grid_size-1, row%(2**(grid_size-1)), col%(2**(grid_size-1)))

print(z(N, r, c))