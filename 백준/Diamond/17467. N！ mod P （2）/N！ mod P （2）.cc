/* 17467 N! mod P (2) */

#include <bits/stdc++.h>
#include <iostream>
#include <math.h>

#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

#define int128 __int128_t
#define int64 long long int
#define int32 int
#define uint128 __uint128_t
#define uint64 uint64_t

uint64 barrett_reduction(uint64 a, uint64 N)
{
    uint64 q;
    uint64 r;
    q = (uint64)(((uint128)(-1ULL / N) * a) >> 64);
    r = a - q * N;
    return r;
}

uint64 factorial_mod(uint64 n, uint64 p)
{
    uint64 fact1 = 1;
    uint64 fact2 = 1;
    for (uint64 i = 1; i < (n + 1) >> 1; ++i)
    {
        fact1 = barrett_reduction(fact1 * (i<<1), p);
        fact2 = barrett_reduction(fact2 * ((i<<1)+1), p);
    }
    if (n % 2 == 0)
    {
        return barrett_reduction(barrett_reduction(fact1 * fact2, p) * n, p);
    }
    else
    {
        return barrett_reduction(fact1 * fact2, p);
    }
}

int main()
{
    int64 n, p;
    int64 answer;
    answer = 1;
    std::cin >> n >> p;
    answer = factorial_mod(n, p);
    std::cout << answer;
}
