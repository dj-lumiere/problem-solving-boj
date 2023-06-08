/* 14882 다항식과 쿼리 */

#include <iostream>
#include <algorithm>
#include <stdint-gcc.h>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

typedef __int128_t int128;
typedef int_fast64_t int64;
typedef int32_t int32;
typedef string str;
typedef void None;
#define vec std::vector
#define print std::cout
#define input std::cin
constexpr int64 MOD = 786433;

int64 multiply_mod(int64 a, int64 b, int64 mod)
{
    return (int64)((int128)a * b % mod);
}

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

    vec<int64> root_of_unity(n / 2);
    for (int64 i = 0; i < n / 2; ++i)
    {
        int64 angle;
        if (invert)
        {
            angle = mod - 1 - (mod - 1) / n;
        }
        else
        {
            angle = (mod - 1) / n;
        }
        root_of_unity[i] = power_with_mod(root, angle * i, mod);
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

vec<int64> polynomial_values(vec<int64> &a)
{
    vec<int64> transformed_a1(a.begin(), a.end());
    // 리스트 사이즈 변경
    int64 n = 262144;
    int64 mod1 = MOD;
    int64 root1 = 10;
    transformed_a1.resize(n);
    ntt(transformed_a1, false, root1, mod1);
    return transformed_a1;
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
    int64 element;
    int64 query;
    int64 N;
    int64 M;
    int64 polynomial_fetch_index;
    int64 where_to_find;
    vec<int64> poly_0_mod_3_coefficient;
    vec<int64> poly_1_mod_3_coefficient;
    vec<int64> poly_2_mod_3_coefficient;
    input >> N;
    vec<int64> power_of_10_with_mod(MOD);
    vec<int64> power_of_10_with_mod_reversed(MOD);
    int64 next_value = 1;
    for (int64 i = 0; i < MOD; i++)
    {
        power_of_10_with_mod[i] = next_value;
        power_of_10_with_mod_reversed[next_value] = i;
        next_value = next_value * 10 % MOD;
    }
    power_of_10_with_mod_reversed[1] = 0;
    for (int64 i = 0; i < N + 1; i++)
    {
        input >> element;
        poly_0_mod_3_coefficient.push_back(element);
        poly_1_mod_3_coefficient.push_back(element * power_of_10_with_mod[i]);
        poly_2_mod_3_coefficient.push_back(element * power_of_10_with_mod[2 * i]);
    }
    vec<int64> result0 = polynomial_values(poly_0_mod_3_coefficient);
    vec<int64> result1 = polynomial_values(poly_1_mod_3_coefficient);
    vec<int64> result2 = polynomial_values(poly_2_mod_3_coefficient);
    input >> M;
    for (int64 i = 0; i < M; i++)
    {
        input >> query;
        where_to_find = power_of_10_with_mod_reversed[query];
        polynomial_fetch_index = where_to_find / 3;
        if (query == 0){
            print << poly_0_mod_3_coefficient[0];
        }
        else if (where_to_find % 3 == 0)
        {
            print << result0[polynomial_fetch_index];
        }
        else if (where_to_find % 3 == 1)
        {
            print << result1[polynomial_fetch_index];
        }
        else if (where_to_find % 3 == 2)
        {
            print << result2[polynomial_fetch_index];
        }
        print << "\n";
    }
}