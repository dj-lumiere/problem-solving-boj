/* 4134 다음 소수 */

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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

bool is_prime(int64 target)
{
    if (target <= 1){
        return 0;
    }
    if (target == 2){
        return 1;
    }
    if (target == 3){
        return 1;
    }
    int64 i = 2;
    while (i * i <= target)
    {
        if (not (target % i))
        {
            return 0;
        }
        i += 1;
    }
    return 1;
}

int32 main()
{
    fastIO();
    int64 test_case = 0;
    input >> test_case;
    for (int64 index = 0; index < test_case; index++)
    {
        int64 target = 0;
        input >> target;
        while (1)
        {
            if (is_prime(target))
            {
                print << target << "\n";
                break;
            }
            target += 1;
        }
    }
    return 0;
}