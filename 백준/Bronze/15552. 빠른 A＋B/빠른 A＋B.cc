#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int main()
{
    fastIO();
    int32_t t;
    cin >> t;

    vector<int32_t> answer;
    for (int32_t i = 0; i < t; ++i)
    {
        int32_t a, b;
        cin >> a >> b;
        answer.push_back(a + b);
    }

    for (int32_t ans : answer)
    {
        cout << ans << "\n";
    }
}
