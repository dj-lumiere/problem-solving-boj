/* 26038 지수 · 로그와 테일러 다항식(Small) */

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

const int32 MOD = 998244353;
const int32 ROOT = 3;

// Print vector
template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
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

int32 multiply_mod(int32 a, int32 b)
{
    return static_cast<int32>((static_cast<int64>(a) * b) % MOD);
}

int32 power_with_mod(int32 base, int32 index)
{
    int32 answer = 1;
    while (index)
    {
        if (index & 1)
        {
            answer = multiply_mod(answer, base);
        }
        base = multiply_mod(base, base);
        index >>= 1;
    }
    return answer;
}

int32 modular_inverse(int32 base)
{
    return power_with_mod(base, MOD - 2);
}

int32 degree_conversion(int32 a)
{
    return static_cast<int32>(ceil(log2(a)));
}

None bit_reversal_permutation(vec<int32> &a)
{
    int32 n = a.size();
    for (int32 i = 1, j = 0; i < n; ++i)
    {
        int32 bit = n >> 1;
        for (; j & bit; bit >>= 1)
        {
            j ^= bit;
        }
        j ^= bit;
        if (i < j)
        {
            swap(a[i], a[j]);
        }
    }
}

None coefficient_normalization(vec<int32> &a)
{
    int32 n = a.size();
    int32 n_inv = modular_inverse(n);
    for (int32 i = 0; i < n; ++i)
    {
        a[i] = multiply_mod(a[i], n_inv);
    }
}

None ntt(vec<int32> &a, bool invert)
{
    int32 n = a.size();
    bit_reversal_permutation(a);
    vec<int32> root_of_unity(n / 2, 0);
    int32 angle;
    if (invert)
    {
        angle = MOD - 1 - (MOD - 1) / n;
    }
    else
    {
        angle = (MOD - 1) / n;
    }
    root_of_unity[0] = 1;
    int32 angleth_power = power_with_mod(ROOT, angle);
    for (int32 i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod(root_of_unity[i - 1], angleth_power);
    }
    for (int32 len = 2; len <= n; len <<= 1)
    {
        int32 step = n / len;
        for (int32 i = 0; i < n; i += len)
        {
            for (int32 j = 0; j < len / 2; j++)
            {
                int32 u = a[i + j];
                int32 v = multiply_mod(a[i + j + len / 2], root_of_unity[step * j]);
                // limit the value in range [0, mod)
                if (u + v < MOD)
                {
                    a[i + j] = u + v;
                }
                else
                {
                    a[i + j] = u + v - MOD;
                }
                if (u - v >= 0)
                {
                    a[i + j + len / 2] = u - v;
                }
                else
                {
                    a[i + j + len / 2] = u - v + MOD;
                }
            }
        }
    }
    if (invert)
    {
        coefficient_normalization(a);
    }
}

vec<int32> multiply_ntt(vec<int32> &a, vec<int32> &b)
{
    vec<int32> transformed_a1(a.begin(), a.end());
    vec<int32> transformed_b1(b.begin(), b.end());
    // 리스트 사이즈 변경
    int32 n = 1 << degree_conversion(a.size() + b.size());
    transformed_a1.resize(n);
    transformed_b1.resize(n);
    ntt(transformed_a1, false);
    ntt(transformed_b1, false);
    for (int32 i = 0; i < n; i++)
    {
        transformed_a1[i] = multiply_mod(transformed_a1[i], transformed_b1[i]);
    }
    ntt(transformed_a1, true);
    return transformed_a1;
}

vec<int32> minus_list(vec<int32> &a)
{
    vec<int32> result(a.begin(), a.end());
    for (int32 index = 0; index < a.size(); index++)
    {
        result[index] = MOD - result[index];
        if (result[index] == MOD)
        {
            result[index] -= MOD;
        }
    }
    return result;
}

vec<int32> add_list(vec<int32> &a, vec<int32> &b)
{
    vec<int32> result(min(a.size(), b.size()), 0);
    for (int32 index = 0; index < result.size(); index++)
    {
        result[index] = a[index] + b[index];
        if (result[index] >= MOD)
        {
            result[index] -= MOD;
        }
    }
    return result;
}

vec<int32> derivation(vec<int32> &target)
{
    vec<int32> result;
    for (int32 index = 1; index < target.size(); index++)
    {
        result.append(multiply_mod(index, target[index]));
    }
    return result;
}

vec<int32> integration(vec<int32> &target, int32 C)
{
    vec<int32> result;
    result.append(C);
    for (int32 index = 0; index < target.size(); index++)
    {
        result.append(multiply_mod(modular_inverse(index + 1), target[index]));
    }
    return result;
}

vec<int32> find_inverse(vec<int32> &target)
{
    int32 degree = degree_conversion(target.size());
    target.resize(1 << degree);
    int32 result_length = 1;
    vec<int32> result(result_length, 0);
    result[0] = 1;
    for (int32 iteration = 0; iteration < degree; iteration++)
    {
        result_length <<= 1;
        result.resize(result_length);
        vec<int32> target_sub(target.begin(), target.begin() + result_length);
        vec<int32> right_term_sub = multiply_ntt(result, target_sub);
        vec<int32> right_term = minus_list(right_term_sub);
        right_term[0] += 2;
        result = multiply_ntt(result, right_term);
        result.resize(result_length);
    }
    for (int32 index = 0; index < result_length; index++)
    {
        result[index] += MOD;
        if (result[index] >= MOD)
        {
            result[index] -= MOD;
        }
    }
    return result;
}

vec<int32> find_log(vec<int32> &target, int32 N)
{
    if ((target.size() == 1) and target[0] == 1)
    {
        return {0};
    }
    vec<int32> target_inverse = find_inverse(target);
    vec<int32> target_prime = derivation(target);
    vec<int32> result_sub = multiply_ntt(target_inverse, target_prime);
    result_sub.resize(N + 1);
    vec<int32> result = integration(result_sub, 0);
    result.pop_back();
    return result;
}

vec<int32> find_exp(vec<int32> &target, int32 N)
{
    int32 degree = degree_conversion(N + 1);
    target.resize(1 << degree);
    int32 result_length = 1;
    vec<int32> result(result_length, 0);
    result[0] = 1;
    for (int32 iteration = 0; iteration < degree; iteration++)
    {
        result_length <<= 1;
        result.resize(result_length);
        vec<int32> target_sub(target.begin(), target.begin() + result_length);
        vec<int32> log_result = find_log(result, result_length - 1);
        log_result = minus_list(log_result);
        vec<int32> right_term = add_list(target, log_result);
        right_term[0] += 1;
        result = multiply_ntt(result, right_term);
        result.resize(result_length);
    }
    result.resize(N + 1);
    result[0] -= 1;
    return result;
}
None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}
int32 main()
{
    int32 N = 0;
    int32 element = 0;
    vec<int32> f, f2;
    input >> N;
    for (int32 index = 0; index < N + 1; index++)
    {
        input >> element;
        f.append(element);
        f2.append(element);
    }
    f2[0] = 1;
    print << find_log(f2, N) << "\n"
          << find_exp(f, N);
}