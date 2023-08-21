/* 27519 소수의 합 */

#include <iostream>
#include <cstdint>
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
#include <type_traits>
#include <bit>
#include <bitset>
#include <numbers>
#include <regex>
#include <numeric>
#include <array>

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
const int32 MOD = 1000000007;

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

vector<int32> extract_primes_from_sieve(int32 limit)
{
    vector<bool> prime_flags(limit + 1, 1);
    prime_flags[0] = false;
    prime_flags[1] = false;

    for (int32 i = 2; i <= sqrt(limit); ++i)
    {
        if (not prime_flags[i])
            continue;
        for (int32 j = i * 2; j <= limit; j += i)
        {
            prime_flags[j] = false;
        }
    }

    vector<int32> primes;
    for (int32 i = 2; i <= limit; ++i)
    {
        if (prime_flags[i])
        {
            primes.append(i);
        }
    }

    return primes;
}

int32 main()
{
    fastIO();
    int32 limit = 100000;
    vector<int32> prime_list = extract_primes_from_sieve(limit);
    int32 prime_count = prime_list.size();
    vector<vector<int32>> result(2, vector<int32>(limit + 1, 0));
    bool toggle = true;
    for (int32 j = 0; j < prime_count; ++j)
    {
        toggle ^= true;
        for (int32 i = 0; i <= limit; ++i)
        {
            int32 prime = prime_list[j];
            int32 toggle = j % 2;
            result[toggle][i] = 0;
            if (i >= prime)
            {
                result[toggle][i] += result[toggle][i - prime];
            }

            if (i == prime)
            {
                result[toggle][i] += 1;
            }

            result[toggle][i] += result[not toggle][i];
            if (result[toggle][i] >= MOD)
            {
                result[toggle][i] -= MOD;
            }
        }
    }

    int32 T;
    input >> T;
    for (int32 t = 0; t < T; ++t)
    {
        int32 n;
        input >> n;
        print << result[toggle][n] << "\n";
    }
}
