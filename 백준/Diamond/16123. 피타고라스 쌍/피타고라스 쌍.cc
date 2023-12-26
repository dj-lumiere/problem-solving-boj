// 16123 피타고라스 쌍

#include <iostream>
#include <array>
#include <cmath>
#include <cstdint>
#include <unordered_map>

const int32_t MAX = 350'000;
std::unordered_map<uint64_t, uint64_t> euler_phi_large;
std::array<uint64_t, MAX + 1> euler_phi_sum;

void precompute_euler_phi()
{
    euler_phi_sum[0] = 0;
    for (int32_t i = 1; i <= MAX; ++i)
    {
        euler_phi_sum[i] += i;
        for (int32_t j = 2; i * j <= MAX; ++j)
        {
            euler_phi_sum[j * i] -= euler_phi_sum[i];
        }
        euler_phi_sum[i] += euler_phi_sum[i - 1];
    }
}

uint64_t euler_phi(uint64_t x)
{
    uint64_t i, j;
    if (x <= MAX)
    {
        return euler_phi_sum[x];
    }
    if (euler_phi_large.find(x) != euler_phi_large.end())
    {
        return euler_phi_large[x];
    }
    uint64_t result = (uint64_t)((__uint128_t)x * (x + 1) / 2);
    for (i = 2; i <= x; i = j + 1)
    {
        j = x / (x / i);
        result -= (j - i + 1) * euler_phi(x / i);
    }
    return euler_phi_large[x] = result;
}

uint64_t euler_phi_even_sum(uint64_t x)
{
    if (x == 1)
    {
        return 1;
    }
    return euler_phi_even_sum(x / 2) + euler_phi(x);
}

uint64_t result(uint64_t x)
{
    if (x == 1)
    {
        return 0;
    }
    return (euler_phi(x) + euler_phi_even_sum(x / 2) - 1) / 2;
}

int main()
{
    precompute_euler_phi();
    uint64_t N;
    std::cin >> N;
    std::cout << result(N);
}