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

vector<int64_t> int64_extended_euclidean_algorithm(int64_t a, int64_t b, int64_t d)
{
    vector<vector<int64_t>> xy_sequence = {{1, 0}, {0, 1}};
    vector<int64_t> remainder_sequence = {a, b};
    int64_t quotient = 0;
    int64_t sequence_index = 2;
    while (true)
    {
        quotient = remainder_sequence[(sequence_index - 2) % 2] / remainder_sequence[(sequence_index - 1) % 2];
        remainder_sequence[sequence_index % 2] = remainder_sequence[(sequence_index - 2) % 2] - quotient * remainder_sequence[(sequence_index - 1) % 2];
        for (int64_t j = 0; j < 2; ++j)
        {
            xy_sequence[sequence_index % 2][j] = xy_sequence[(sequence_index - 2) % 2][j] - xy_sequence[(sequence_index - 1) % 2][j] * quotient;
        }
        if (remainder_sequence[sequence_index % 2] == d)
        {
            break;
        }
        ++sequence_index;
    }
    return xy_sequence[sequence_index % 2];
}

int64_t adding_reverse(int64_t a, int64_t mod)
{
    return (-a % mod + mod) % mod;
}

int64_t multiplying_reverse(int64_t a, int64_t mod)
{
    if (gcd(a, mod) != 1)
    {
        return -1;
    }
    return ((int64_extended_euclidean_algorithm(a, mod, 1)[0] % mod) + mod) % mod;
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
    int64 n, a;
    input >> n >> a;
    print << adding_reverse(a, n) << " " << multiplying_reverse(a, n);
}