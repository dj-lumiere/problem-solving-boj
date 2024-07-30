#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& member) {
    os << "[";
    for (auto it = member.begin(); it != member.end(); ++it) {
        os << *it;
        if (it != member.end() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

class SegmentForest {
private:
    int size_x, size_y;
    int default_val, identity_val;
    int log_size_x, tree_capacity_x;
    int log_size_y, tree_capacity_y;
    int index_start_x, index_start_y;
    vector<vector<int>> tree;
    vector<vector<int>> lazy;
    vector<vector<int>> lazy_multiplier;
    int index_offset_x, index_offset_y;

public:
    SegmentForest(vector<vector<int>>& member, int default_val, int identity_val, int index_start_x, int index_start_y) {
        size_y = member.size();
        size_x = member[0].size();
        this->default_val = default_val;
        this->identity_val = identity_val;
        log_size_x = ceil(log2(size_x));
        tree_capacity_x = 1 << log_size_x;
        log_size_y = ceil(log2(size_y));
        tree_capacity_y = 1 << log_size_y;
        this->index_start_x = index_start_x;
        this->index_start_y = index_start_y;
        tree.resize(2 * tree_capacity_y, vector<int>(2 * tree_capacity_x, default_val));
        lazy.resize(2 * tree_capacity_y, vector<int>(2 * tree_capacity_x, identity_val));
        lazy_multiplier.resize(2 * tree_capacity_y, vector<int>(2 * tree_capacity_x, 0));
        index_offset_x = tree_capacity_x - index_start_x;
        index_offset_y = tree_capacity_y - index_start_y;
        build_tree(member);
    }

    void build_tree(vector<vector<int>>& member) {
        for (int y = tree_capacity_y; y < 2 * tree_capacity_y; ++y) {
            for (int x = tree_capacity_x; x < 2 * tree_capacity_x; ++x) {
                tree[y][x] = member[y - tree_capacity_y][x - tree_capacity_x];
                lazy_multiplier[y][x] = 1;
            }
        }
        for (int y = 2 * tree_capacity_y - 1; y > 0; --y) {
            for (int x = tree_capacity_x - 1; x > 0; --x) {
                pull_x(x, y);
            }
        }
        for (int y = tree_capacity_y - 1; y > 0; --y) {
            for (int x = 2 * tree_capacity_x - 1; x > 0; --x) {
                pull_y(x, y);
            }
        }
    }

    void point_update(int index_x, int index_y, int value) {
        index_x += index_offset_x;
        index_y += index_offset_y;
        for (int level1 = log_size_x; level1 > 0; --level1) {
            for (int level2 = log_size_y; level2 > 0; --level2) {
                push_x(index_x >> level1, index_y >> level2);
                push_y(index_x >> level1, index_y >> level2);
            }
        }
        apply_update_y(index_x, index_y, value);
        for (int level1 = 0; level1 <= log_size_x; ++level1) {
            for (int level2 = 0; level2 <= log_size_y; ++level2) {
                if (level1 != 0) pull_x(index_x >> level1, index_y >> level2);
                if (level2 != 0) pull_y(index_x >> level1, index_y >> level2);
            }
        }
    }

    int point_query(int index_x, int index_y) {
        return range_query(index_x, index_x, index_y, index_y);
    }

    int range_query(int left, int right, int up, int down) {
        int left_result = default_val;
        int right_result = default_val;
        left += index_offset_x;
        right += index_offset_x;
        up += index_offset_y;
        down += index_offset_y;
        for (int level1 = log_size_x; level1 > 0; --level1) {
            for (int level2 = log_size_y; level2 > 0; --level2) {
                if (((left >> level1) << level1) != left) {
                    push_x(left >> level1, up >> level2);
                    push_x(left >> level1, down >> level2);
                }
                if ((((right + 1) >> level1) << level1) != right + 1) {
                    push_x(right >> level1, up >> level2);
                    push_x(right >> level1, down >> level2);
                }
                if (((up >> level2) << level2) != up) {
                    push_y(left >> level1, up >> level2);
                    push_y(right >> level1, up >> level2);
                }
                if ((((down + 1) >> level2) << level2) != down + 1) {
                    push_y(left >> level1, down >> level2);
                    push_y(right >> level1, down >> level2);
                }
            }
        }
        while (left <= right) {
            if (left % 2 == 1) {
                int u2 = up, d2 = down;
                while (u2 <= d2) {
                    if (u2 % 2 == 1) left_result = merge_nodes(left_result, tree[u2][left]); ++u2;
                    if (d2 % 2 == 0) left_result = merge_nodes(left_result, tree[d2][left]); --d2;
                    u2 >>= 1;
                    d2 >>= 1;
                }
                ++left;
            }
            if (right % 2 == 0) {
                int u2 = up, d2 = down;
                while (u2 <= d2) {
                    if (u2 % 2 == 1) right_result = merge_nodes(right_result, tree[u2][right]); ++u2;
                    if (d2 % 2 == 0) right_result = merge_nodes(right_result, tree[d2][right]); --d2;
                    u2 >>= 1;
                    d2 >>= 1;
                }
                --right;
            }
            left >>= 1;
            right >>= 1;
        }
        return merge_nodes(left_result, right_result);
    }

    void display(ostream& os) const {
        display_helper(os, 0, 1);
    }

private:
    void apply_update_x(int index_x, int index_y, int value) {
        tree[index_y][index_x] = update_node(value, tree[index_y][index_x], lazy_multiplier[index_y][index_x]);
        if (index_x < tree_capacity_x) {
            lazy[index_y][index_x] = compose_lazies(value, lazy[index_y][index_x]);
        }
    }

    void apply_update_y(int index_x, int index_y, int value) {
        tree[index_y][index_x] = update_node(value, tree[index_y][index_x], lazy_multiplier[index_y][index_x]);
        if (index_y < tree_capacity_y) {
            lazy[index_y][index_x] = compose_lazies(value, lazy[index_y][index_x]);
        }
    }

    void push_x(int index_x, int index_y) {
        apply_update_x(2 * index_x, index_y, lazy[index_y][index_x]);
        apply_update_x(2 * index_x + 1, index_y, lazy[index_y][index_x]);
        lazy[index_y][index_x] = identity_val;
    }

    void push_y(int index_x, int index_y) {
        apply_update_y(index_x, 2 * index_y, lazy[index_y][index_x]);
        apply_update_y(index_x, 2 * index_y + 1, lazy[index_y][index_x]);
        lazy[index_y][index_x] = identity_val;
    }

    void pull_x(int index_x, int index_y) {
        tree[index_y][index_x] = merge_nodes(tree[index_y][2 * index_x], tree[index_y][2 * index_x + 1]);
        lazy_multiplier[index_y][index_x] = lazy_multiplier[index_y][2 * index_x] + lazy_multiplier[index_y][2 * index_x + 1];
    }

    void pull_y(int index_x, int index_y) {
        tree[index_y][index_x] = merge_nodes(tree[2 * index_y][index_x], tree[2 * index_y + 1][index_x]);
        lazy_multiplier[index_y][index_x] = lazy_multiplier[2 * index_y][index_x] + lazy_multiplier[2 * index_y + 1][index_x];
    }

    int merge_nodes(int left, int right) {
        // Change this part for various operations
        return left + right;
    }

    int update_node(int lazy_value, int node_value, int lazy_multiplier) {
        // Change this part for various operations
        return node_value + lazy_value * lazy_multiplier;
    }

    int compose_lazies(int lazy_value1, int lazy_value2) {
        // Change this part for various operations
        return lazy_value1 + lazy_value2;
    }

    void display_helper(ostream& os, int level, int pos) const {
        string indent = string(level * 4, ' ');
        if (level == 0) {
            os << indent << "root=" << tree[pos] << " (" << lazy[pos] << ")\n";
        }
        else {
            os << indent << tree[pos] << " (" << lazy[pos] << ")\n";
        }
        if (level < log_size_y) {
            display_helper(os, level + 1, 2 * pos);
            display_helper(os, level + 1, 2 * pos + 1);
        }
    }
};

ostream& operator<<(ostream& os, const SegmentForest& sf) {
    sf.display(os);
    return os;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    SegmentForest sf(matrix, 0, 0, 1, 1);

    vector<int> answer;
    for (int i = 0; i < m; ++i) {
        int q;
        cin >> q;
        if (q == 0) {
            int y, x, v;
            cin >> y >> x >> v;
            v -= sf.point_query(x, y);
            sf.point_update(x, y, v);
        }
        else {
            int y1, x1, y2, x2;
            cin >> y1 >> x1 >> y2 >> x2;
            answer.push_back(sf.range_query(x1, x2, y1, y2));
        }
    }

    for (int ans : answer) {
        cout << ans << "\n";
    }

    return 0;
}
