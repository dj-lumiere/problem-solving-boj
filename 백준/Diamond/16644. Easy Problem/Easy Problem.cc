// 16644 Easy Problem in C++

#include <iostream>
#include <vector>
#include <cmath>
#include <cstdint>
#include <unordered_map>

const int32_t MAX = 12'000'000;
std::unordered_map<int32_t, int64_t> mobius_large;
std::array<int32_t, MAX + 1> mobius_sum;

void precompute_mobius()
{
    mobius_sum[0] = 0;
    mobius_sum[1] = 1;
    for (int32_t i = 1; i <= MAX; ++i)
    {
        for (int32_t j = 2; i * j <= MAX; ++j)
        {
            mobius_sum[j * i] -= mobius_sum[i];
        }
        mobius_sum[i] += mobius_sum[i - 1];
    }
}

int64_t mobius(int32_t x)
{
    int32_t i, j;
    if (x <= MAX)
    {
        return mobius_sum[x];
    }
    if (mobius_large.contains(x))
    {
        return mobius_large[x];
    }
    int64_t result = 1;
    for (i = 2; i <= x; i = j + 1)
    {
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
    if ((int64_t)m_sqrt * m_sqrt < m)
    {
        m_sqrt += 1;
    }
    for (int32_t i = 1; i < m_sqrt; i = j + 1)
    {
        j = sqrt(m / (m / ((int64_t) i * i)));
        answer += (mobius(j) - mobius(i - 1)) * (m / ((int64_t) i * i));
    }
    return answer;
}

int64_t find_kth_square_free_number(int64_t k)
{
    if (k == 4)
    {
        return 5;
    }
    if (k == 1)
    {
        return 1;
    }
    int64_t left;
    int64_t right;
    //1.6449340668482264364724151
    if (k < (int64_t) 1e12)
    {
        left = 1;
        right = k << 1;
    }
    else if (k <= (int64_t) 1e16)
    {
        left = int64_t((__int128) k * 164'493'406ll / 100'000'000ll);
        right = int64_t((__int128) k * 164'493'407ll / 100'000'000ll);
    }
    else if (k <= (int64_t) 1e17)
    {
        left = int64_t((__int128) k * 164'493'406'684ll / 100'000'000'000ll);
        right = int64_t((__int128) k * 164'493'406'685ll / 100'000'000'000ll);
    }
    else if (k <= (int64_t) 1e18)
    {
        left = int64_t((__int128) k * 1'644'934'066'848'000ll / 1'000'000'000'000'000ll);
        right = int64_t((__int128) k * 1'644'934'066'848'400ll / 1'000'000'000'000'000ll);
    }
//    int64_t iteration_count = 1;
    while (left < right)
    {
//        const auto time1 = std::chrono::high_resolution_clock::now();
        int64_t mid = (left + right) >> 1;
        int64_t count = count_square_free_numbers(mid);
//        std::cout << mid << " " << count << "\n";
        if (count < k)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
//        const auto time2 = std::chrono::high_resolution_clock::now();
//        std::cout << "Try #" << iteration_count << ":"
//                  << std::chrono::duration_cast<std::chrono::milliseconds>(time2 - time1).count() << "ms\n";
//        iteration_count += 1;
    }
    return left;
}

int main()
{
    int64_t n;
    std::cin >> n;
//    const auto time1 = std::chrono::high_resolution_clock::now();
    precompute_mobius();
//    const auto time2 = std::chrono::high_resolution_clock::now();
//    std::cout << "Precomputation time:" << std::chrono::duration_cast<std::chrono::milliseconds>(time2 - time1).count()
//              << "ms\n";
    std::cout << find_kth_square_free_number(n) << "\n";
//    const auto time3 = std::chrono::high_resolution_clock::now();
//    std::cout << "Total time:" << std::chrono::duration_cast<std::chrono::milliseconds>(time3 - time1).count()
//              << "ms\n";
}
