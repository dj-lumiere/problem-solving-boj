#include <iostream>
#include <cstdint>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int32_t n, k;
    cin >> n >> k;
    vector<int64_t> volumes(n, 0);
    for (int32_t i = 0; i < n; i++) {
        cin >> volumes[i];
    }
    int64_t start = 0;
    int64_t end = 1ll<<31;
    while (start + 1 < end) {
        int64_t mid = (start + end) >> 1;
        int64_t glasses = 0;
        for (auto v : volumes) {
            glasses += v / mid;
        }
        if (glasses >= k) {
            start = mid;
        }
        else {
            end = mid;
        }
    }
    cout << start;
}