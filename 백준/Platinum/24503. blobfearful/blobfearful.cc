/* 24503 blobfearful */

#include <iostream>
#include <stdint.h>
#include <complex>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <random>
#include <chrono>
#include <quadmath.h>
#include <type_traits>
#include <bit>
#include <bitset>
#include <numbers>
#include <regex>
#include <numeric>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

using int128 = __int128_t;
using int64 = int64_t;
using int32 = int32_t;
using int16 = int16_t;
using int8 = int8_t;
using uint128 = __uint128_t;
using uint64 = uint64_t;
using uint32 = uint32_t;
using uint16 = uint16_t;
using uint8 = uint8_t;
using float80 = long double;
using float64 = double;
using float32 = float;
using complex80 = complex<float80>;
using complex64 = complex<float64>;
using complex32 = complex<float32>;
using str = string;
using None = void;
template <typename T>
using vec = std::vector<T>;
template <typename T, typename U>
using dict = std::map<T, U>;
template <typename T>
using set = std::set<T>;
template <typename T>
using heap = std::priority_queue<T>;
#define print cout
#define input cin
#define append push_back
#define appendleft push_front
#define pop pop_back
#define popleft pop_front

template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
    for (auto it = target.begin(); it != target.end(); ++it)
    {
        os << *it;
        if (std::next(it) != target.end())
        {
            os << " ";
        }
    }
    return os;
}

template <typename T>
bool is_in_list(T target, std::vector<T> &list)
{
    return find(list.begin(), list.end(), target) != list.end();
}

int64_t randint(int64_t lower_bound, int64_t upper_bound)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int64_t> dist(lower_bound, upper_bound);
    int64_t x = dist(gen);
    return x;
}

int64_t multiply_mod(const uint64_t a, const uint64_t b, const uint64_t mod)
{
    return (int64_t)((uint128)a * b % mod);
}

int64_t power_with_mod(int64_t base, int64_t index, int64_t mod)
{
    int64_t answer = 1;
    while (index)
    {
        if (index & 1)
        {
            answer = multiply_mod(answer, base, mod);
        }
        base = multiply_mod(base, base, mod);
        index >>= 1;
    }
    return answer;
}

int64_t next_iteration(int64_t x, int64_t n, int64_t random_number)
{
    return (multiply_mod(x, x, n) + random_number) % n;
}

bool is_composite(int64_t n, int64_t power_of_two, int64_t remainder, int64_t base)
{
    int64_t temp_base = power_with_mod(base, remainder, n);
    if (temp_base == 1 or temp_base == n - 1)
    {
        return false;
    }
    for (int i = 0; i < power_of_two - 1; i++)
    {
        temp_base = power_with_mod(temp_base, 2, n);
        if (temp_base == n - 1)
        {
            return false;
        }
    }
    return true;
}

bool is_prime(int64_t n)
{
    std::vector<int64_t> base_prime_list = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41};
    if (is_in_list(n, base_prime_list))
    {
        return true;
    }
    if (n == 1 or n % 2 == 0)
    {
        return false;
    }
    int64_t power_of_two = 0, remainder = n - 1;
    while (remainder % 2 == 0)
    {
        remainder /= 2;
        power_of_two += 1;
    }
    for (auto base : base_prime_list)
    {
        if (is_composite(n, power_of_two, remainder, base))
        {
            return false;
        }
    }
    return true;
}

int64_t find_single_prime_factor(int64_t n)
{
    if (is_prime(n))
    {
        return n;
    }
    if (n % 2 == 0)
    {
        return 2;
    }
    if (n == 1)
    {
        return 1;
    }
    int64_t x = randint(2, n - 1);
    int64_t y = x;
    int64_t random_number = randint(2, n - 1);
    int64_t gcd_value = 1;
    while (gcd_value == 1)
    {
        x = next_iteration(x, n, random_number);
        y = next_iteration(next_iteration(y, n, random_number), n, random_number);
        gcd_value = std::gcd(abs(x - y), n);
        if (gcd_value == n)
        {
            return find_single_prime_factor(n);
        }
    }
    if (is_prime(gcd_value))
    {
        return gcd_value;
    }
    return find_single_prime_factor(gcd_value);
}

std::map<int64_t, int64_t> factorize_large_number(int64_t N)
{
    int64_t temp_N = N;
    std::vector<int64_t> factors;
    std::vector<int64_t> base_prime_list = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41};
    for (auto prime : base_prime_list)
    {
        while (temp_N % prime == 0)
        {
            factors.push_back(prime);
            temp_N /= prime;
        }
    }
    while (temp_N > 1)
    {
        int64_t factor = find_single_prime_factor(temp_N);
        factors.push_back(factor);
        temp_N /= factor;
    }
    std::map<int64_t, int64_t> count_map;
    for (auto factor : factors)
    {
        count_map[factor]++;
    }
    return count_map;
}

vec<int64> factorize_n_factorial(int64 n, vec<int64> &K_factor_list)
{
    vec<int64> result(K_factor_list.size(), 0);
    int32 i = 0;
    for (auto it = K_factor_list.begin(); it != K_factor_list.end(); ++it)
    {
        int64_t next_n = n;
        int64_t v = *it;
        while (next_n > 0)
        {
            next_n /= v;
            result[i] += next_n;
        }
        i++;
    }
    return result;
}

vec<int64> factorize_n(int64 n, vec<int64> &K_factor_list)
{
    vec<int64> result(K_factor_list.size(), 0);
    int32 i = 0;
    for (auto it = K_factor_list.begin(); it != K_factor_list.end(); ++it)
    {
        int64_t v = *it;
        while (not(n % v))
        {
            result[i] += 1;
            n /= v;
        }
        i++;
    }
    return result;
}

int64 find_blobunfearful_day_base(int64 K, vec<int64> &K_factor_list, vec<int64> &K_multiplier)
{
    int64 start = 0;
    int64 end = K + 1;
    while (start + 1 < end)
    {
        int64 mid = (start + end) / 2;
        vec<int64> mid_fact = factorize_n_factorial(mid, K_factor_list);
        bool is_divisible = true;
        int32 i = 0;
        for (
            auto it1 = mid_fact.begin(), it2 = K_multiplier.begin();
            it1 != mid_fact.end() and it2 != K_multiplier.end();
            ++it1, ++it2)
        {
            if (*it1 < *it2)
            {
                is_divisible = false;
                break;
            }
        }
        if (is_divisible)
        {
            end = mid;
        }
        else
        {
            start = mid;
        }
    }
    return end;
}

int64 find_blobunfearful_day(int64 init, int64 K, int64 base, vec<int64> &K_factor_list, vec<int64> &K_multiplier)
{
    vec<int64> init_factorized = factorize_n(init, K_factor_list);
    int64 start = 0;
    int64 end = base + 1;
    while (start + 1 < end)
    {
        int64 mid = (start + end) / 2;
        vec<int64> mid_fact = factorize_n_factorial(mid, K_factor_list);
        bool is_divisible = true;
        int32 i = 0;
        for (
            auto it1 = mid_fact.begin(), it2 = K_multiplier.begin(), it3 = init_factorized.begin();
            it1 != mid_fact.end() and it2 != K_multiplier.end() and it3 != init_factorized.end();
            ++it1, ++it2, ++it3)
        {
            if (*it1 + *it3 < *it2)
            {
                is_divisible = false;
                break;
            }
        }
        if (is_divisible)
        {
            end = mid;
        }
        else
        {
            start = mid;
        }
    }
    return end;
}

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int32_t main()
{
    fastIO();
    int64 K, Q, element;
    vec<int64_t> A, result;
    input >> K >> Q;
    auto K_factorized = factorize_large_number(K);
    vec<int64_t> K_factor_list = {};
    vec<int64_t> K_multiplier = {};
    for (int64 i = 0; i < Q; i++)
    {
        input >> element;
        A.append(element);
    }
    for (auto it = K_factorized.begin(); it != K_factorized.end(); ++it)
    {
        K_factor_list.append(it->first);
        K_multiplier.append(it->second);
    }
    int64 base = find_blobunfearful_day_base(K, K_factor_list, K_multiplier);
    for (auto &element : A)
    {
        if (element == 1)
        {
            result.append(base);
            continue;
        }
        result.append(find_blobunfearful_day(element, K, base, K_factor_list, K_multiplier));
    }
    print << result;
}