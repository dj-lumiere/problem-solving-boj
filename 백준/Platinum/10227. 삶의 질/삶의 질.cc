#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <climits>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    vector<string> answers;
    for (int hh = 1; hh <= t; ++hh) {
        int r, c, h, w;
        cin >> r >> c >> h >> w;
        vector<vector<int>> grid(r, vector<int>(c));
        for (int y = 0; y < r; ++y) {
            for (int x = 0; x < c; ++x) {
                cin >> grid[y][x];
            }
        }
        int answer = 0;
        int start = 0;
        int end = r * c;
        vector<vector<int>> accumulated_sum(r + 1, vector<int>(c + 1, 0));
        while (start + 1 < end) {
            int mid = (start + end) / 2;
            for (int y = 0; y < r; ++y) {
                for (int x = 0; x < c; ++x) {
                    if (grid[y][x] == mid) {
                        accumulated_sum[y + 1][x + 1] = 0;
                    } else {
                        accumulated_sum[y + 1][x + 1] = (grid[y][x] - mid) / abs(grid[y][x] - mid);
                    }
                }
            }
            for (int y = 1; y <= r; ++y) {
                for (int x = 1; x <= c; ++x) {
                    accumulated_sum[y][x] += accumulated_sum[y][x - 1];
                }
            }
            for (int y = 1; y <= r; ++y) {
                for (int x = 1; x <= c; ++x) {
                    accumulated_sum[y][x] += accumulated_sum[y - 1][x];
                }
            }
            bool found = false;
            for (int y = 0; y <= r - h; ++y) {
                for (int x = 0; x <= c - w; ++x) {
                    int bigger_than_mid_count = accumulated_sum[y + h][x + w]
                                                - accumulated_sum[y + h][x]
                                                - accumulated_sum[y][x + w]
                                                + accumulated_sum[y][x];
                    
                    if (bigger_than_mid_count <= 0) {
                        end = mid;
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
            if (not found) start = mid;
        }
        answer = end;
        answers.push_back(to_string(answer));
    }
    for (const auto& ans : answers) {
        cout << ans << '\n';
    }
}