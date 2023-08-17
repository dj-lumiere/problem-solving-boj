/* 교수님 계산기가 고장났어요! */

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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

vec<uint32> parse_integer(str number)
{
    uint32 sign = 1, digit = 0;
    for (int32 i = 0; i < number.size(); i++)
    {
        if (number[i] == '-')
        {
            sign = -1U;
            continue;
        }
        if (number[i] == '.')
        {
            continue;
        }
        digit = digit * 10 + (number[i] - '0');
    }
    vec<uint32> result;
    result.append(sign);
    result.append(digit);
    return result;
}

None calculate_multiplication(str &A, str &B)
{
    vec<uint32> a = parse_integer(A);
    vec<uint32> b = parse_integer(B);
    uint32 sign = a[0] * b[0];
    uint64 integer_part = uint64(a[1]) * b[1] / 1'000'000'000'000'000'000;
    uint64 fraction_part = uint64(a[1]) * b[1] % 1'000'000'000'000'000'000;
    str result;
    for (int32 i = 0; i < 18; i++)
    {
        result += '0' + fraction_part % 10;
        fraction_part /= 10;
    }
    reverse(result.begin(), result.end());
    if (sign == -1U)
    {
        print << "-";
    }
    print << integer_part << "." << result << "\n";
}

int32_t main()
{
    fastIO();
    int32 N;
    str A, B;
    input >> N;
    for (int32 i = 0; i < N; i++)
    {
        input >> A >> B;
        calculate_multiplication(A, B);
    }
}