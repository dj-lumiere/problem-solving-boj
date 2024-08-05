#include <vector>
#include <iostream>
#include <deque>
#include <cstdint>
#include <utility>
#include <tuple>

using namespace std;

int main() {
    int32_t n;
    cin >> n;
    vector<int32_t> a(n);
    for (int32_t i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    bool result = std::next_permutation(a.begin(), a.end());
    if (result)
    {
        for (int32_t i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
    } else
    {
        cout << -1;
    }
}