// 16644 Easy Problem in C++

#include <iostream>
#include <vector>
#include <cmath>
#include <cstdint>
#include <unordered_map>
#include <bitset>
#include <array>

const int32_t MAX = 15'840'000;
std::unordered_map<int32_t, int64_t> mobius_large;
std::vector<int32_t> mobius_sum(MAX+1, 1);

void precompute_mobius()
{
    //mobius_sum.fill(1);
    mobius_sum[0] = 0;
    std::bitset<MAX + 1> is_prime;
    for (int32_t i = 2; i <= MAX; i++) {
        if (not is_prime[i]) {
            for (int32_t j = i; j <= MAX; j += i) {
                mobius_sum[j] *= -1;
                is_prime[j] = true;
            }
            for (int64_t j = (int64_t) i * i; j <= MAX; j += (int64_t) i * i) {
                mobius_sum[j] = 0;
            }
        }
    }
    for (int32_t i = 1; i <= MAX; i++) {
        mobius_sum[i] += mobius_sum[i - 1];
    }
}

int64_t mobius(int32_t x)
{
    int32_t i, j;
    if (x <= MAX) {
        return mobius_sum[x];
    }
    if (mobius_large.contains(x)) {
        return mobius_large[x];
    }
    int64_t result = 1;
    for (i = 2; i <= x; i = j + 1) {
        j = x / (x / i);
        result -= (j - i + 1) * mobius(x / i);
    }
    return mobius_large[x] = result;
}

int64_t count_square_free_numbers(int64_t m)
{
    int64_t answer = 0;
    int32_t j = 0;
    int32_t m_sqrt = sqrt(m);
    if ((int64_t) m_sqrt * m_sqrt < m) {
        m_sqrt += 1;
    }
    for (int32_t i = 1; i < m_sqrt; i = j + 1) {
        j = sqrt(m / (m / ((int64_t) i * i)));
        answer += (mobius(j) - mobius(i - 1)) * (m / ((int64_t) i * i));
    }
    return answer;
}

int64_t find_kth_square_free_number(int64_t k)
{
    if (k == 4) {
        return 5;
    }
    if (k == 1) {
        return 1;
    }
    int64_t left;
    int64_t right;
    if (k < (int64_t) 1e12) {
        left = 1;
        right = k << 1;
    } else if (k <= (int64_t) 1e16) {
        left = int64_t((__int128) k * 164'493'406ll / 100'000'000ll);
        right = int64_t((__int128) k * 164'493'407ll / 100'000'000ll);
    } else if (k <= (int64_t) 1e17) {
        left = int64_t((__int128) k * 164'493'406'684ll / 100'000'000'000ll);
        right = int64_t((__int128) k * 164'493'406'685ll / 100'000'000'000ll);
    } else if (k <= (int64_t) 1e18) {
        left = int64_t((__int128) k * 1'644'934'066'848'000ll / 1'000'000'000'000'000ll);
        right = int64_t((__int128) k * 1'644'934'066'848'400ll / 1'000'000'000'000'000ll);
    }
    while (left < right) {
        int64_t mid = (left + right) >> 1;
        int64_t count = count_square_free_numbers(mid);
        if (count < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

int main()
{
    int64_t n;
    std::cin >> n;
    precompute_mobius();
    std::cout << find_kth_square_free_number(n) << "\n";
}
