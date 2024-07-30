#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <tuple>
#include <functional>

// Constants
const int64_t INF = 1e18;
const int MOD = 1'000'000'007;
const std::vector<std::pair<int, int>> DELTA = {
    {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}
};

// Utility function to check if coordinates are within bounds
bool is_inbound(int pos_x, int pos_y, int size_x, int size_y) {
    return pos_x >= 0 && pos_x < size_x && pos_y >= 0 && pos_y < size_y;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t = 1; // You can adjust this as needed

    while (t--) {
        int n, m, k;
        std::cin >> n >> m >> k;

        std::vector<std::vector<int>> food(n, std::vector<int>(n, 5));
        std::vector<std::vector<int>> delta_food(n, std::vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                std::cin >> delta_food[i][j];
            }
        }

        std::vector<std::vector<std::unordered_map<int, int>>> trees(n, std::vector<std::unordered_map<int, int>>(n));
        for (int i = 0; i < m; ++i) {
            int y, x, z;
            std::cin >> y >> x >> z;
            --y; --x;
            trees[y][x][z]++;
        }

        for (int a = 1; a <= k; ++a) {
            // Spring & Summer
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (trees[r][c].empty()) continue;

                    std::unordered_map<int, int> new_trees;
                    int dead_tree_age_sum = 0;
                    int current_food = food[r][c];

                    std::vector<int> ages;
                    for (const auto& [age, count] : trees[r][c]) {
                        ages.push_back(age);
                    }
                    std::sort(ages.begin(), ages.end());

                    for (int age : ages) {
                        int count = trees[r][c][age];
                        int can_be_fed = current_food / age;
                        int fed_count = std::min(can_be_fed, count);

                        if (fed_count < count) {
                            dead_tree_age_sum += (age / 2) * (count - fed_count);
                        }
                        if (fed_count > 0) {
                            new_trees[age + 1] += fed_count;
                            current_food -= age * fed_count;
                        }
                    }
                    trees[r][c] = new_trees;
                    food[r][c] = current_food;
                    food[r][c] += dead_tree_age_sum;
                }
            }

            // Fall
            std::vector<std::vector<int>> trees_to_be_grown(n, std::vector<int>(n, 0));
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    for (const auto& [age, count] : trees[r][c]) {
                        if (age % 5 == 0) {
                            for (const auto& [dr, dc] : DELTA) {
                                int nr = r + dr;
                                int nc = c + dc;
                                if (is_inbound(nr, nc, n, n)) {
                                    trees_to_be_grown[nr][nc] += count;
                                }
                            }
                        }
                    }
                }
            }

            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    int sapling_count = trees[r][c][1] + trees_to_be_grown[r][c];
                    if (sapling_count > 0) {
                        trees[r][c][1] = sapling_count;
                    }
                }
            }

            // Winter
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    food[r][c] += delta_food[r][c];
                }
            }
        }

        int answer = 0;
        for (const auto& row : trees) {
            for (const auto& cell : row) {
                for (const auto& [age, count] : cell) {
                    answer += count;
                }
            }
        }

        std::cout << answer << "\n";
    }

    return 0;
}
