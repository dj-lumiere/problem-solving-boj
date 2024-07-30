#include <vector>
#include <iostream>
#include <deque>
#include <cstdint>
#include <utility>
#include <tuple>

using namespace std;


bool is_inbound(int32_t pos_x, int32_t size_x, int32_t pos_y, int32_t size_y) {
    return 0 <= pos_x and pos_x < size_x and 0 <= pos_y and pos_y < size_y;
}

vector<pair<int32_t, int32_t>> delta = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

int main() {
    int32_t t;
    cin >> t;
    for (int32_t i = 1; i <= t; i++) {
        int32_t n, start_x, start_y, end_x, end_y;
        cin >> n;
        vector<vector<int32_t>> grid(n, vector<int32_t>(n, 0));
        vector<vector<int32_t>> time(n, vector<int32_t>(n, 0));
        for (int32_t y = 0; y < n; y++) {
            for (int32_t x = 0; x < n; x++) {
                cin >> grid[y][x];
            }
        }
        cin >> start_y >> start_x >> end_y >> end_x;
        time[start_y][start_x] = 1;
        deque<tuple<int32_t, int32_t, int32_t>> queue;
        queue.push_back({ start_x, start_y, 1 });
        while (not queue.empty()) {
            //cout << queue << "\n";
            int32_t cur_x, cur_y, cur_time;
            tie(cur_x, cur_y, cur_time) = queue.front();
            queue.pop_front();
            if (cur_x == end_x and cur_y == end_y) {
                break;
            }
            for (int32_t j = 0; j < 4; j++) {
                int32_t dx, dy;
                tie(dy, dx) = delta[j];
                int32_t next_x = cur_x + dx;
                int32_t next_y = cur_y + dy;
                if (not is_inbound(next_x, n, next_y, n)) {
                    continue;
                }
                if (grid[next_y][next_x] == 1) {
                    continue;
                }
                if (grid[next_y][next_x] == 2 and cur_time % 3 != 0) {
                    queue.push_back({ cur_x, cur_y, cur_time + 1 });
                    continue;
                }
                else if (time[next_y][next_x] != 0) {
                    continue;
                }
                time[next_y][next_x] = cur_time + 1;
                queue.push_back({ next_x, next_y, cur_time + 1 });
            }
        }
        cout << "#" << i << " " << (time[end_y][end_x] - 1) << "\n";
    }
}