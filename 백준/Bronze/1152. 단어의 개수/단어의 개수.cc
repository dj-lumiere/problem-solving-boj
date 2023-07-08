/* 1152 단어의 갯수 */

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
#include <quadmath.h>
#include <type_traits>

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

const int64 MAXIMUM_LETTERS = 1000000;

bool is_valid_alphabet_upper(int8 target)
{
    return ('A' <= target) and (target <= 'Z');
}
bool is_valid_alphabet_lower(int8 target)
{
    return ('a' <= target) and (target <= 'z');
}

bool is_valid_letter(int8 target)
{
    return (is_valid_alphabet_lower(target)) or (is_valid_alphabet_upper(target)) or (target == ' ');
}

int32 main()
{
    vec<int8> sentence;
    int8 letter;
    int64 answer = 1;
    for (int64 i = 0; i < MAXIMUM_LETTERS; i++)
    {
        scanf("%c", &letter);
        if (not(is_valid_letter(letter)))
        {
            break;
        }
        sentence.append(letter);
    }
    for (int64 i = 0; i < sentence.size(); i++)
    {
        if ((i == 0) and (sentence[i] == ' '))
        {
            answer -= 1;
        }
        if ((i + 1 == sentence.size()) and (sentence[i] == ' '))
        {
            answer -= 1;
        }
        if (sentence[i] == ' ')
        {
            answer += 1;
        }
    }
    print << answer;
}