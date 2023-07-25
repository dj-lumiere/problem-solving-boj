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

template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
    os << target.size() << "\n";
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

vector<int32_t> find_lis(vector<int32_t> &target)
{
    int32_t target_length = target.size();
    vector<int32_t> sequence_indices(target_length + 1, 0);
    vector<int32_t> previous_indices(target_length + 1, -1);
    vector<int32_t> lis_subsequence;
    vector<int32_t> lis;
    int32_t lis_length = 0;
    for (int32_t current_index = 0; current_index < target_length; current_index++)
    {
        int32_t current_value = target[current_index];
        auto it = lower_bound(lis_subsequence.begin(), lis_subsequence.end(), current_value);
        int32_t position = distance(lis_subsequence.begin(), it);
        if (it == lis_subsequence.end())
        {
            lis_subsequence.push_back(current_value);
        }
        else
        {
            *it = current_value;
        }
        if (position == lis_length)
        {
            sequence_indices[lis_length] = current_index;
            previous_indices[current_index] = lis_length > 0 ? sequence_indices[lis_length - 1] : -1;
            lis_length++;
        }
        else if (current_value < target[sequence_indices[position]])
        {
            sequence_indices[position] = current_index;
            previous_indices[current_index] = position > 0 ? sequence_indices[position - 1] : -1;
        }
    }
    int32_t final_index = sequence_indices[lis_length - 1];
    while (final_index != -1)
    {
        lis.push_back(target[final_index]);
        final_index = previous_indices[final_index];
    }
    reverse(lis.begin(), lis.end());
    return lis;
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
    int32 n;
    vec<int32> a;
    vec<int32> lis;
    input >> n;
    for (int32 i = 0; i < n; i++)
    {
        int32 element;
        input >> element;
        a.push_back(element);
    }
    lis = find_lis(a);
    print << lis;
}