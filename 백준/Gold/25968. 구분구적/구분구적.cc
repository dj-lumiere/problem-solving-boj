/* 25968 구분구적 */

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

float64 f(vec<float64> &poly, float64 x)
{
    float64 result = 0.0;
    for (int64 i = 0; i < poly.size(); i++)
    {
        result += poly[i] * pow(x, 2 * i);
    }
    return result;
}

float64 f_integral(vec<float64> &poly, float64 x)
{
    float64 result = 0.0;
    for (int64 i = 0; i < poly.size(); i++)
    {
        result += poly[i] * pow(x, 2 * i + 1) / (2 * i + 1);
    }
    return result;
}

float64 find_root(vec<float64> &poly)
{
    float64 start = 0.0;
    float64 end = 40.0;
    while (start + 0.0000005 < end)
    {
        float64 mid = (start + end) / 2;
        if (f(poly, mid) * poly[0] < 0)
        { 
            end = mid;
        }
        else
        {
            start = mid;
        }
    }
    return start;
}

float64 find_area(vec<float64> &poly, int64 pieces)
{

    float64 end = find_root(poly);
    float64 start = -end;
    float64 answer = 0.0;
    float64 width = 2 * end / pieces;
    float64 current_x = start + width / 2;
    if (pieces > 2000000)
    {
        return 2 * abs(f_integral(poly, end));
    }
    for (int64 i = 0; i < pieces; i++)
    {
        answer += abs(f(poly, current_x)) * width;
        current_x += width;
    }
    return answer;
}

int32_t main()
{
    fastIO();
    int64 n, p;
    vec<float64> poly;
    float64 element;
    input >> n;
    for (int64 i = 0; i <= n; i++)
    {
        input >> element;
        poly.append(element);
    }
    reverse(poly.begin(), poly.end());
    input >> p;
    print << fixed;
    print << find_area(poly, p);
}