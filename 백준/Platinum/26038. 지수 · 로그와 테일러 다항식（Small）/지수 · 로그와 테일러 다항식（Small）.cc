/* 26038 지수 · 로그와 테일러 다항식(Small) */

#include <iostream>
#include <stdint-gcc.h>
#include <array>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>
#include <tuple>
#include <cmath>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

typedef __int128_t int128;
typedef int64_t int64;
typedef int32_t int32;
typedef __uint128_t uint128;
typedef uint64_t uint64;
typedef uint32_t uint32;
typedef long double float80;
typedef double float64;
typedef float float32;
typedef void None;
#define vec vector
#define linked_list list
#define dict unordered_map
#define set unordered_set
#define heap priority_queue
#define print cout
#define input cin
#define append push_back

constexpr int64 MOD = 998244353;
constexpr int64 ROOT = 3;

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

int64 multiply_mod(int64 a, int64 b, int64 mod)
{
    return (int64)((int128)a * b % mod);
};

int64 power_with_mod(int64 base, int64 index, int64 mod)
{
    int64 answer = 1;
    while (index)
    {
        if (index & 1)
        {
            answer = multiply_mod(answer, base, mod);
        }
        base = multiply_mod(base, base, mod);
        index >>= 1;
    }
    return answer;
}

int64 modular_inverse(int64 base, int64 mod)
{
    return power_with_mod(base, mod - 2, mod);
}

None ntt(vec<int64> &a, bool invert, int64 root, int64 mod)
{
    int64 n = a.size();

    for (int64 i = 1, j = 0; i < n; ++i)
    {
        int64 bit = n >> 1;
        for (; j & bit; bit >>= 1)
        {
            j ^= bit;
        }
        j ^= bit;

        if (i < j)
        {
            std::swap(a[i], a[j]);
        }
    }

    vec<int64> root_of_unity(n / 2,0);
    int64 angle;
    if (invert)
    {
        angle = mod - 1 - (mod - 1) / n;
    }
    else
    {
        angle = (mod - 1) / n;
    }
    root_of_unity[0] = 1;
    int64 angleth_power = power_with_mod(root, angle, mod);
    for (int64 i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod(root_of_unity[i-1],angleth_power,mod);
    }

    for (int64 len = 2; len <= n; len <<= 1)
    {
        int64 step = n / len;
        for (int64 i = 0; i < n; i += len)
        {
            int64 w = 1;
            for (int64 j = 0; j < len / 2; ++j)
            {
                int64 u = a[i + j];
                int64 v = (a[i + j + len / 2] * root_of_unity[step * j]) % mod;
                // limit the value in range [0, mod)
                if (u + v < mod)
                {
                    a[i + j] = u + v;
                }
                else
                {
                    a[i + j] = u + v - mod;
                }
                if (u - v >= 0)
                {
                    a[i + j + len / 2] = u - v;
                }
                else
                {
                    a[i + j + len / 2] = u - v + mod;
                }
            }
        }
    }
    // Normalize
    if (invert)
    {
        int64 n_inv = modular_inverse(n, mod);
        for (int64 i = 0; i < n; ++i)
        {
            a[i] = multiply_mod(a[i], n_inv, mod);
        }
    }
}

vec<int64> multiply_ntt(vec<int64> &a, vec<int64> &b)
{
    vec<int64> transformed_a1(a.begin(), a.end());
    vec<int64> transformed_b1(b.begin(), b.end());
    // 리스트 사이즈 변경
    int32 n = 1;
    while (n < a.size() + b.size())
    {
        n <<= 1;
    }
    transformed_a1.resize(n);
    transformed_b1.resize(n);
    ntt(transformed_a1, false, ROOT, MOD);
    ntt(transformed_b1, false, ROOT, MOD);
    for (int64 i = 0; i < n; i++)
    {
        transformed_a1[i] = multiply_mod(transformed_a1[i], transformed_b1[i], MOD);
    }
    ntt(transformed_a1, true, ROOT, MOD);
    return transformed_a1;
}

int64 degree_conversion(int64 a)
{
    return static_cast<int64>(ceil(log2(a)));
}

vec<int64> minus_list(vec<int64> &a)
{
    vec<int64> result(a.begin(), a.end());
    for (int64 index = 0; index < a.size(); index++)
    {
        result[index] = (MOD - result[index]) % MOD;
    }
    return result;
}

vec<int64> add_list(vec<int64> &a, vec<int64> &b)
{
    vec<int64> result(min(a.size(), b.size()), 0);
    for (int64 index = 0; index < result.size(); index++)
    {
        result[index] += (a[index] + b[index]) % MOD;
    }
    return result;
}

vec<int64> derivation(vec<int64> &target)
{
    vec<int64> result;
    for (int64 index = 1; index < target.size(); index++)
    {
        result.append(multiply_mod(index, target[index], MOD));
    }
    return result;
}

vec<int64> integration(vec<int64> &target, int64 C)
{
    vec<int64> result;
    result.append(C);
    for (int64 index = 0; index < target.size(); index++)
    {
        result.append(multiply_mod(modular_inverse(index + 1, MOD), target[index], MOD));
    }
    return result;
}

vec<int64> find_inverse(vec<int64> &target)
{
    int64 degree = degree_conversion(target.size());
    target.resize(1<<degree);
    int64 result_length = 1;
    vec<int64> result(result_length, 0);
    result[0] = 1;
    for (int64 iteration = 0; iteration < degree; iteration++)
    {
        result_length <<= 1;
        result.resize(result_length);
        vec<int64> target_sub(target.begin(), target.begin() + result_length);
        vec<int64> right_term_sub = multiply_ntt(result, target_sub);
        vec<int64> right_term = minus_list(right_term_sub);
        right_term[0] += 2;
        result = multiply_ntt(result, right_term);
        result.resize(result_length);
        //print << iteration << " " << result << "\n";
    }
    for (int64 index=0;index < result_length;index++){
        result[index] += MOD;
        result[index] %= MOD;
    }
    return result;
}

vec<int64> find_log(vec<int64> &target, int64 N)
{
    if ((target.size() == 1) and target[0] == 1){
        return {0};
    }
    vec<int64> target_inverse = find_inverse(target);
    //print <<"target_inverse "<<target_inverse<<"\n";
    vec<int64> target_prime = derivation(target);
    //print <<"target_prime "<<target_prime<<"\n";
    vec<int64> result_sub = multiply_ntt(target_inverse, target_prime);
    result_sub.resize(N+1);
    vec<int64> result = integration(result_sub, 0);
    result.pop_back();
    //print << result << "\n";
    return result;
}

vec<int64> find_exp(vec<int64> &target, int64 N)
{
    int64 degree = degree_conversion(N+1);
    target.resize(1<<degree);
    int64 result_length = 1;
    vec<int64> result(result_length, 0);
    result[0] = 1;
    for (int64 iteration = 0; iteration < degree; iteration++)
    {
        result_length <<= 1;
        result.resize(result_length);
        vec<int64> target_sub(target.begin(), target.begin() + result_length);
        vec<int64> log_result = find_log(result, result_length-1);
        log_result = minus_list(log_result);
        vec<int64> right_term = add_list(target, log_result);
        right_term[0] += 1;
        result = multiply_ntt(result, right_term);
        result.resize(result_length);
        //print << iteration << " " << result << "\n";
    }
    result.resize(N+1);
    result[0] -= 1;
    return result;
}

int32 main()
{
    int64 N = 0;
    int64 element = 0;
    vec<int64> f, f2;
    input >> N;
    for (int64 index = 0; index < N + 1; index++)
    {
        input >> element;
        f.append(element);
        f2.append(element);
    }
    f2[0] = 1;
    print << find_log(f2, N) << "\n"
          << find_exp(f, N);
}