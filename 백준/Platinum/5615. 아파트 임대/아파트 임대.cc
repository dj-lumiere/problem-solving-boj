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

template <typename T>
T max(vec<T> &target)
{
    return *max_element(target.begin(), target.end());
}

template <typename T>
T min(vec<T> &target)
{
    return *min_element(target.begin(), target.end());
}

template <typename T>
int32 bit_length(T target)
{
    return bit_width(target);
}

template <typename T, typename U>
std::ostream &operator<<(std::ostream &os, const std::map<T, U> &target)
{
    os << "{";
    for (auto it = target.begin(); it != target.end(); ++it)
    {
        os << it->first << ": " << it->second;
        if (std::next(it) != target.end())
        {
            os << ", ";
        }
    }
    os << "}";
    return os;
}

int64_t randint(int64_t lower_bound, int64_t upper_bound)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int64_t> dist(lower_bound, upper_bound);
    int64_t x = dist(gen);
    return x;
}

int64_t multiply_mod(int64_t a, int64_t b, int64_t mod)
{
    return (int64_t)((__int128_t)a * b % mod);
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
    vector<int64_t> base_prime_list = {2, 7, 61};
    if (find(base_prime_list.begin(), base_prime_list.end(), n) != base_prime_list.end())
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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int32 main()
{
    fastIO();
    int32 t, impossible_cases = 0;
    int64 target;
    input >> t;
    for (int32 i = 0; i < t; i++)
    {
        input >> target;
        target = target * 2 + 1;
        if (is_prime(target))
        {
            impossible_cases += 1;
        }
    }
    print << impossible_cases;
}