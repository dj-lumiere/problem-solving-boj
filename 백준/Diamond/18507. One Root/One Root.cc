/* 18507 One Root */

#include <iostream>
#include <stdint.h>
#include <complex>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <random>
#include <chrono>
#include <type_traits>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

using int128 = __int128_t;
using int64 = int64_t;
using int32 = int32_t;
using uint128 = __uint128_t;
using uint64 = uint64_t;
using uint32 = uint32_t;
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
template <typename T>
using linked_list = std::list<T>;
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

int64 n, m, p, q;

None fastIO()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
}

float80 f(float80 x)
{
    return powl(x, n) + x * static_cast<float80>(p);
}

float80 f_prime(float80 x)
{
    return static_cast<float80>(n) * powl(x, static_cast<float80>(n) - 1) + static_cast<float80>(p);
}

float80 f_prime_root(float80 p)
{
    return powl(p / n, 1 / (static_cast<float80>(n) - 1));
}

int32 main()
{
    input >> n >> m;
    int64 answer = 0;
    if (n % 2 == 0)
    {
        for (int64 i = 1; i <= m; i++)
        {
            p = -i;
            if (max(n * powl(p, n - 1), (n - 1) * powl(p, n)) > m)
            {
                break;
            }
            else
            {
                answer += 2;
            }
        }
        answer += 1;
    }
    else
    {
        for (int64 p = 1; p <= m; p++)
        {
            answer += 2 * max(static_cast<int64>(0), m - static_cast<int64>(floorl((p - static_cast<float80>(p) / n) * f_prime_root(p))));
        }
        answer += (2 * m + 1) * (m + 1);
    }
    print << answer << "\n";
}