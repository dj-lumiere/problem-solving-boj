#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000000000000
#define MOD 1000000000

// Helper lambda functions
auto is_inbound = [](int pos_x, int size_x, int pos_y, int size_y) {
    return 0 <= pos_x && pos_x < size_x && 0 <= pos_y && pos_y < size_y;
};

// Delta for directions
const vector<pair<int, int>> DELTA = {{0, 0}, {0, -1}, {1, 0}, {0, 1}, {-1, 0}};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // Input tokens
    int t = 1;
    vector<string> answers;

    for (int hh = 1; hh <= t; hh++) {
        int n, m;
        cin >> n >> m;

        // Triangle grid (padded with two extra rows/columns)
        vector<vector<int>> grid_triangle(n + 2, vector<int>(n + 2, 0));

        // Imos method for triangle: record on 6 cells and then accumulate
        for (int i = 0; i < m; i++) {
            int a, b, x;
            cin >> b >> a >> x;
            b -= 1; // Offset by 1 (as in the Python version)
            a -= 1; // Offset by 1
            x += 1;

            grid_triangle[b][a] += 1;
            grid_triangle[b][a + 1] -= 1;
            grid_triangle[b + x][a + x + 1] += 1;
            grid_triangle[b + x + 1][a + x + 1] -= 1;
            grid_triangle[b + x][a] -= 1;
            grid_triangle[b + x + 1][a + 1] += 1;

            // Debugging print for triangle grid (optional)
            // for (const auto& row : grid_triangle) {
            //     for (const auto& val : row) {
            //         cerr << val << " ";
            //     }
            //     cerr << "\n";
            // }
            // cerr << "\n";
        }

        // Left-right accumulation
        for (int y = 0; y < n + 2; y++) {
            int x = 1;
            while (is_inbound(x, n + 2, y, n + 2)) {
                grid_triangle[y][x] += grid_triangle[y][x - 1];
                x++;
            }
        }

        // Top-bottom accumulation
        for (int x = 0; x < n + 2; x++) {
            int y = 1;
            while (is_inbound(x, n + 2, y, n + 2)) {
                grid_triangle[y][x] += grid_triangle[y - 1][x];
                y++;
            }
        }

        // Diagonal accumulation
        for (int r = 0, dy_minus_dx = -n - 3; dy_minus_dx < n + 4; r++, dy_minus_dx++) {
            int x, y;
            if (dy_minus_dx < 0) {
                x = -dy_minus_dx;
                y = 0;
            } else {
                x = 0;
                y = dy_minus_dx;
            }
            x++;
            y++;
            while (is_inbound(x, n + 2, y, n + 2)) {
                grid_triangle[y][x] += grid_triangle[y - 1][x - 1];
                x++;
                y++;
            }
        }

        // Counting the final answer
        int answer = 0;
        for (const auto& row : grid_triangle) {
            for (const auto& val : row) {
                if (val) answer++;
            }
        }
        answers.push_back(to_string(answer));
    }

    // Output the answers
    for (const auto& ans : answers) {
        cout << ans << "\n";
    }

    return 0;
}
