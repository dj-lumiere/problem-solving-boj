#include <iostream>
#include <vector>
#include <cmath>
#include <cstdint>
#include <unordered_map>
#include <algorithm>

using i64 = int64_t;
using i32 = int32_t;
using namespace std;

void fastIO()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
}

int main()
{
    fastIO();
    i32 n, a2, b2, c2, d2;
    i64 answer = 0;
    vector<i32> a, b, c, d;
    vector<i32> a_b;
    vector<i32> c_d;
    cin >> n;
    for (i32 _ = 0; _ < n; _++) {
        cin >> a2 >> b2 >> c2 >> d2;
        a.push_back(a2);
        b.push_back(b2);
        c.push_back(c2);
        d.push_back(d2);
    }
    for (i32 i : a) {
        for (i32 j : b) {
            a_b.push_back(i + j);
        }
    }
    for (i32 i : c) {
        for (i32 j : d) {
            c_d.push_back(i + j);
        }
    }
    sort(a_b.begin(), a_b.end());
    sort(c_d.begin(), c_d.end());
    for (const auto& v : a_b) {
        answer += (upper_bound(c_d.begin(), c_d.end(), -v) - lower_bound(c_d.begin(), c_d.end(), -v));
    }
    cout << answer;
}
