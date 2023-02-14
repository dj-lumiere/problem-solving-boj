# 17114 하이퍼 토마토
import io, os
from collections import deque
from itertools import product

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
delta_list = [
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]
(
    m_size,
    n_size,
    o_size,
    p_size,
    q_size,
    r_size,
    s_size,
    t_size,
    u_size,
    v_size,
    w_size,
) = list(map(int, input().split()))
queue = deque()
graph = dict()

global zero_count
zero_count = 0

graph = [
    [
        [
            [
                [
                    [
                        [
                            [
                                [
                                    [
                                        list(map(int, input().split()))
                                        for _ in range(n_size)
                                    ]
                                    for _ in range(o_size)
                                ]
                                for _ in range(p_size)
                            ]
                            for _ in range(q_size)
                        ]
                        for _ in range(r_size)
                    ]
                    for _ in range(s_size)
                ]
                for _ in range(t_size)
            ]
            for _ in range(u_size)
        ]
        for _ in range(v_size)
    ]
    for _ in range(w_size)
]

for m, n, o, p, q, r, s, t, u, v, w in product(range(m_size), range(n_size), range(o_size), range(p_size), range(q_size), range(r_size), range(s_size), range(t_size), range(u_size), range(v_size), range(w_size)):
    if graph[w][v][u][t][s][r][q][p][o][n][m] == 1:
        queue.append((m, n, o, p, q, r, s, t, u, v, w))
    if graph[w][v][u][t][s][r][q][p][o][n][m] == 0:
        zero_count += 1

global max_time
max_time = 0

while queue:
    m, n, o, p, q, r, s, t, u, v, w = queue.popleft()
    for i in range(22):
        nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw = (
            m + delta_list[i][0],
            n + delta_list[i][1],
            o + delta_list[i][2],
            p + delta_list[i][3],
            q + delta_list[i][4],
            r + delta_list[i][5],
            s + delta_list[i][6],
            t + delta_list[i][7],
            u + delta_list[i][8],
            v + delta_list[i][9],
            w + delta_list[i][10],
        )
        if (
            0 <= nm < m_size
            and 0 <= nn < n_size
            and 0 <= no < o_size
            and 0 <= np < p_size
            and 0 <= nq < q_size
            and 0 <= nr < r_size
            and 0 <= ns < s_size
            and 0 <= nt < t_size
            and 0 <= nu < u_size
            and 0 <= nv < v_size
            and 0 <= nw < w_size
        ):
            if not graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]:
                graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = (
                    graph[w][v][u][t][s][r][q][p][o][n][m] + 1
                )
                zero_count -= 1
                queue.append((nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw))
                if max_time < graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]:
                    max_time = graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]

if zero_count != 0:
    print(-1)
else:
    print(max(max_time - 1, 0))
