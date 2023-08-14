/* 1238 파티 */

/* 11438 LCA 2 */

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

using namespace std;

const int32 INF = 1e9;

template <typename T>
T max(vec<T> &target)
{
    return *max_element(target.begin(), target.end());
}

int32 main() {
    int32 N, M, X;
    input >> N >> M >> X;

    vector<vector<int32>> distance(N + 1, vector<int32>(N + 1, INF));
    
    for (int32 i = 1; i <= N; i++) {
        distance[i][i] = 0;
    }

    for (int32 i = 0; i < M; i++) {
        int32 start, end, cost;
        input >> start >> end >> cost;
        distance[start][end] = cost;
    }

    // Floyd-Warshall algorithm
    for (int32 mid = 1; mid <= N; mid++) {
        for (int32 start = 1; start <= N; start++) {
            for (int32 end = 1; end <= N; end++) {
                if (distance[start][end] > distance[start][mid] + distance[mid][end]) {
                    distance[start][end] = distance[start][mid] + distance[mid][end];
                }
            }
        }
    }

    vector<int32> result(N + 1, -1);
    for (int32 i = 1; i <= N; i++) {
        result[i] = distance[i][X] + distance[X][i];
    }

    print << max(result) << "\n";
}