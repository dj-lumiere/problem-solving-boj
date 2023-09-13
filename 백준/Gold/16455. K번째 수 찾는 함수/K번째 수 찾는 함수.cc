#include <vector>
#include <algorithm>
#include <random>
#include <vector>

int kth(std::vector<int> &a, int k)
{
    std::random_device rd;
    std::mt19937 generator(rd());
 
    std::shuffle(a.begin(), a.begin() + a.size() / 2, generator);
    k -= 1;
    nth_element(a.begin(), a.begin() + k, a.end());
    int ans = a[k];
    return ans;
}