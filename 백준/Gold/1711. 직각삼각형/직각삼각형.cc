/* 1711 직각삼각형 */

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

int64 find_right_angled_triangle(vector<vector<int64>> &triangles)
{
    int32 N = triangles.size();
    int64 answer = 0;
    for (int32 i = 0; i < N - 2; i++)
    {
        for (int32 j = i + 1; j < N - 1; j++)
        {
            for (int32 k = j + 1; k < N; k++)
            {
                int64 i1 = triangles[i][0];
                int64 i2 = triangles[i][1];
                int64 j1 = triangles[j][0];
                int64 j2 = triangles[j][1];
                int64 k1 = triangles[k][0];
                int64 k2 = triangles[k][1];
                int64 v11 = i1 - j1;
                int64 v12 = i2 - j2;
                int64 v21 = j1 - k1;
                int64 v22 = j2 - k2;
                int64 v31 = k1 - i1;
                int64 v32 = k2 - i2;
                int64 d1 = v11 * v11 + v12 * v12;
                int64 d2 = v21 * v21 + v22 * v22;
                int64 d3 = v31 * v31 + v32 * v32;
                if (d1 + d2 == d3 or d2 + d3 == d1 or d3 + d1 == d2)
                {
                    answer += 1;
                }
            }
        }
    }
    return answer;
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
    int32 N, element;
    input >> N;
    vector<vector<int64>> triangles(N, vector<int64>(2, 0));
    for (int32 i = 0; i < N; i++)
    {
        for (int32 j = 0; j < 2; j++)
        {
            input >> element;
            triangles[i][j] = element;
        }
    }
    print << find_right_angled_triangle(triangles);
}