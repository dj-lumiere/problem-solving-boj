#include <iostream>
#include <cstdint>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<int64_t> dp(2001*12, 0);
    for (int32_t j = 1; j < 2001; j++) {
        dp[j] = 1;
    }
    for (int32_t i = 1; i < 12; i++) {
        for (int32_t j = 1; j < 2001; j++) {
            for (int32_t k = 1; k < 2001; k++) {
                if ((j << 1) <= k) {
                    dp[i*2001 + k] += dp[(i - 1)*2001 + j];
                }
            }
        }
    }
    int32_t t, n, m;
    cin >> t;
    for (int32_t _ = 0; _ < t; _++) {
        cin >> n >> m;
        int64_t a = 0;
        if ((1ll << (n - 1)) > m) {
            cout << 0 << "\n";
            continue;
        }
        for (int32_t i = (n-1)*2001; i <= (n - 1) * 2001+m; i++) {
            a += dp[i];
        }
        cout << a << "\n";
    }

}