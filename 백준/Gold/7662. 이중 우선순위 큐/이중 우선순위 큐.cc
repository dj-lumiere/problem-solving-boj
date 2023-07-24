/* 7662 이중 우선순위 큐 */

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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

None solve(int32 commands)
{
    multiset<int32> my_set;
    str operation;
    int32 operand;
    for (int32 i = 0; i < commands; i++)
    {
        input >> operation >> operand;
        if (operation == "I")
        {
            my_set.emplace(operand);
        }
        if (operation == "D" and not my_set.empty() and operand == -1)
        {
            my_set.erase(my_set.begin());
        }
        if (operation == "D" and not my_set.empty() and operand == 1)
        {
            my_set.erase(prev(my_set.end()));
        }
    }
    if (my_set.empty())
    {
        print << "EMPTY\n";
    }
    else
    {
        print << *my_set.rbegin() << " " << *my_set.begin() << "\n";
    }
}

int32 main()
{
    fastIO();
    int32 t, commands;
    input >> t;
    for (int32 i = 0; i < t; i++)
    {
        input >> commands;
        solve(commands);
    }
}