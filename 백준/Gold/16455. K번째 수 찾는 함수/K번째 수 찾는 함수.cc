#include <vector>
#include <algorithm>
int kth(std::vector<int> &a, int k)
{
    k -= 1;
    nth_element(a.begin(), a.begin() + k, a.end());
    int ans = a[k];
    return ans;
}