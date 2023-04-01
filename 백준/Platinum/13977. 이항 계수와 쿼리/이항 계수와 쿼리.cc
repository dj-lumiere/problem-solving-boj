#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#define int128 __int128_t
#define int64 long long int
#define int32 int
#define uint128 __uint128_t
#define uint64 uint64_t
#define uint32 uint32_t
#define float64 double
#define float32 float
#define mod 1000000007



uint64 factorial_array[4000001];
uint64 factorial_reverse_array[4000001];

uint64 powmod(uint64 base, uint64 exp)
{
	uint128 result = 1;
	base %= mod;
	while (exp > 0)
	{
		if (exp % 2 == 1)
		{
			result = (result * base) % mod;
		}
		base = (base * base) % mod;
		exp /= 2;
	}
	return (uint64)result;
}

uint64 factorial_mod()
{
	for (uint64 i = 0; i <= 4000000; i++)
	{
		if (i == 0)
		{
			factorial_array[i] = (uint64)1;
		}
		else
		{
			factorial_array[i] = ((factorial_array[i - 1] * i) % mod);
		}
	}
	return 0;
}

uint64 factorial_reverse_mod()
{
	for (uint64 i = 0; i <= 4000000; i++)
	{
		if (i == 0)
		{
			factorial_reverse_array[i] = (uint64)1;
		}
		else
		{
			factorial_reverse_array[i] = powmod(factorial_array[i], mod - 2);
		}
	}
	return 0;
}

int32 main()
{
	int32 m, n, k;
	uint64 answer;
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	std::cin >> m;
	factorial_mod();
	factorial_reverse_mod();

	for (int32 i = 0; i < m; i++)
	{
		std::cin >> n >> k;
		answer = (uint64)((uint128)factorial_array[n] * factorial_reverse_array[k] * factorial_reverse_array[n - k] % mod);
		std::cout << answer << "\n";
	}
}