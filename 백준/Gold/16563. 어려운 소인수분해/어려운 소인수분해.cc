/* 16563 어려운 소인수분해 */

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

vector<bool> get_prime_sieve(int32_t limit)
{
    vector<bool> prime_flags(limit + 1, true);
    prime_flags[0] = prime_flags[1] = false;
    for (int32_t i = 2; i <= sqrt(limit); ++i)
    {
        if (not prime_flags[i])
        {
            continue;
        }
        for (int32_t j = i * 2; j <= limit; j += i)
        {
            prime_flags[j] = false;
        }
    }
    return prime_flags;
}

vector<int32_t> extract_primes_from_sieve(int32_t limit)
{
    vector<bool> prime_flags = get_prime_sieve(limit);
    vector<int32_t> primes;
    for (int32_t i = 0; i < prime_flags.size(); ++i)
    {
        if (prime_flags[i])
        {
            primes.push_back(i);
        }
    }
    return primes;
}

vector<int32_t> get_prime_factors(int32_t value, vector<int32_t> &primes)
{
    vector<int32_t> prime_factors;
    for (auto prime : primes)
    {
        if (prime * prime > value)
        {
            break;
        }
        while (value % prime == 0)
        {
            prime_factors.push_back(prime);
            value /= prime;
        }
    }
    if (value != 1)
    {
        prime_factors.push_back(value);
    }
    return prime_factors;
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
    int32 n, test;
    vec<int32> primes = extract_primes_from_sieve(5000001);
    input >> n;
    for (int32 i = 0; i < n; i++){
        input >> test;
        print << get_prime_factors(test, primes) << "\n";
    }
}