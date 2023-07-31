/* 11385 씽크스몰 */

#include <iostream>
#include <algorithm>
#include <complex>
#include <cstdint>
#include <vector>
#include <fstream>

#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

#define print std::cout
#define input std::cin

template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
    os << "[";
    for (auto it = target.begin(); it != target.end(); ++it)
    {
        os << *it;
        if (std::next(it) != target.end())
        {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

namespace ntt
{
    const uint64_t MOD = 1002772198720536577;
    const uint32_t INT32_BITMASK = 0xffffffff;

    const uint32_t MOD1 = 998244353;
    const uint64_t MOD1_MAGIC = 155014655926305585;
    const uint32_t MOD1_MULINV = 669690699;
    const uint32_t MOD1_SHIFT = 23;
    const uint32_t ROOT1 = 3;

    const uint32_t MOD2 = 1004535809;
    const uint64_t MOD2_MAGIC = 154043791693913158;
    const uint32_t MOD2_MULINV = 332747959;
    const uint32_t MOD2_SHIFT = 23;
    const uint32_t ROOT2 = 3;

    uint64_t multiply_int128_high(uint64_t a, uint64_t b);
    int64_t merge_remainder(int32_t remainder1, int32_t remainder2);
    int32_t find_bit_ceil(int32_t a);
    void bit_reversal_permutation(std::vector<int32_t> &a);
    std::vector<int64_t> polynomial_multiplication(std::vector<int32_t> &a, std::vector<int32_t> &b);

    int32_t multiply_mod1(int32_t a, int32_t b);
    int32_t power_with_mod1(int32_t base, int32_t index);
    int32_t modular_inverse1(int32_t base);
    void coefficient_normalization1(std::vector<int32_t> &a);
    void transform_mod1(std::vector<int32_t> &a, bool invert);

    int32_t multiply_mod2(int32_t a, int32_t b);
    int32_t power_with_mod2(int32_t base, int32_t index);
    int32_t modular_inverse2(int32_t base);
    void coefficient_normalization2(std::vector<int32_t> &a);
    void transform_mod2(std::vector<int32_t> &a, bool invert);
}

uint64_t ntt::multiply_int128_high(uint64_t a, uint64_t b)
{
    uint64_t a_high = a >> 32;
    uint64_t a_low = a & INT32_BITMASK;
    uint64_t b_high = b >> 32;
    uint64_t b_low = b & INT32_BITMASK;
    uint64_t product_high = a_high * b_high;
    uint64_t product_low = a_low * b_low;
    uint64_t product_mid1 = a_high * b_low;
    uint64_t product_mid2 = a_low * b_high;
    uint64_t carry = 0;
    product_high += product_mid1 >> 32;
    product_high += product_mid2 >> 32;
    if (product_low > product_low + ((product_mid1 & INT32_BITMASK) << 32))
    {
        carry += 1;
    }
    product_low += ((product_mid1 & INT32_BITMASK) << 32);
    if (product_low > product_low + ((product_mid2 & INT32_BITMASK) << 32))
    {
        carry += 1;
    }
    product_low += ((product_mid2 & INT32_BITMASK) << 32);
    product_high += carry; // Carry from the low 64 bits
    return product_high;
}
int64_t ntt::merge_remainder(int32_t remainder1, int32_t remainder2)
{
    uint64_t t1 = multiply_mod1(remainder1, MOD2_MULINV);
    uint64_t t2 = multiply_mod2(remainder2, MOD1_MULINV);
    t1 *= MOD2;
    t2 *= MOD1;
    t1 %= MOD;
    t2 %= MOD;
    t1 += t2;
    t1 %= MOD;
    return t1;
}
int32_t ntt::find_bit_ceil(int32_t a)
{
    return static_cast<int32_t>(ceil(log2(a)));
}
void ntt::bit_reversal_permutation(std::vector<int32_t> &a)
{
    int32_t n = a.size();
    for (int32_t i = 1, j = 0; i < n; ++i)
    {
        int32_t bit = n >> 1;
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
}
std::vector<int64_t> ntt::polynomial_multiplication(std::vector<int32_t> &a, std::vector<int32_t> &b)
{
    int32_t original_size = a.size() + b.size();
    int32_t n = 1 << ntt::find_bit_ceil(original_size);
    std::vector<int64_t> result(original_size);

    std::vector<int32_t> transform_a_mod1(a.begin(), a.end());
    transform_a_mod1.resize(n);
    ntt::transform_mod1(transform_a_mod1, false);

    std::vector<int32_t> transform_b_mod1(b.begin(), b.end());
    transform_b_mod1.resize(n);
    ntt::transform_mod1(transform_b_mod1, false);

    std::vector<int32_t> transform_a_mod2(a.begin(), a.end());
    transform_a_mod2.resize(n);
    ntt::transform_mod2(transform_a_mod2, false);

    std::vector<int32_t> transform_b_mod2(b.begin(), b.end());
    transform_b_mod2.resize(n);
    ntt::transform_mod2(transform_b_mod2, false);

    for (int32_t i = 0; i < n; i++)
    {
        transform_a_mod1[i] = multiply_mod1(transform_a_mod1[i], transform_b_mod1[i]);
        transform_a_mod2[i] = multiply_mod2(transform_a_mod2[i], transform_b_mod2[i]);
    }

    ntt::transform_mod1(transform_a_mod1, true);
    transform_a_mod1.resize(original_size);

    ntt::transform_mod2(transform_a_mod2, true);
    transform_a_mod2.resize(original_size);

    for (int32_t i = 0; i < original_size; i++)
    {
        result[i] = merge_remainder(transform_a_mod1[i], transform_a_mod2[i]);
    }

    return result;
}

int32_t ntt::multiply_mod1(int32_t a, int32_t b)
{
    uint64_t product = static_cast<uint64_t>(a) * b;
    uint64_t quotient = multiply_int128_high(product, MOD1_MAGIC) >> MOD1_SHIFT;
    uint64_t result = product - quotient * MOD1;
    if (result >= MOD1)
    {
        result -= MOD1;
    }
    return static_cast<int32_t>(result);
}
int32_t ntt::power_with_mod1(int32_t base, int32_t index)
{
    int32_t answer = 1;
    while (index > 0)
    {
        if (index & 1)
        {
            answer = multiply_mod1(answer, base);
        }
        base = multiply_mod1(base, base);
        index >>= 1;
    }
    return answer;
}
int32_t ntt::modular_inverse1(int32_t base)
{
    return power_with_mod1(base, MOD1 - 2);
}
void ntt::coefficient_normalization1(std::vector<int32_t> &a)
{
    int32_t n = a.size();
    int32_t n_inv = modular_inverse1(n);
    for (int32_t i = 0; i < n; ++i)
    {
        a[i] = multiply_mod1(a[i], n_inv);
    }
}
void ntt::transform_mod1(std::vector<int32_t> &a, bool invert)
{
    int32_t n = a.size();
    bit_reversal_permutation(a);
    std::vector<int32_t> root_of_unity(n / 2, 0);
    int32_t angle = (MOD1 - 1) / n;
    if (invert)
    {
        angle = MOD1 - 1 - angle;
    }
    root_of_unity[0] = 1;
    int32_t angleth_power = power_with_mod1(ROOT1, angle);
    for (int32_t i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod1(root_of_unity[i - 1], angleth_power);
    }
    for (int32_t len = 2; len <= n; len <<= 1)
    {
        int32_t step = n / len;
        for (int32_t i = 0; i < n; i += len)
        {
            for (int32_t j = 0; j < len / 2; j++)
            {
                int32_t u = a[i + j];
                int32_t v = multiply_mod1(a[i + j + len / 2], root_of_unity[step * j]);
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                if (u + v >= MOD1)
                {
                    a[i + j] -= MOD1;
                }
                if (u - v < 0)
                {
                    a[i + j + len / 2] += MOD1;
                }
            }
        }
    }
    if (invert)
    {
        coefficient_normalization1(a);
    }
}

int32_t ntt::multiply_mod2(int32_t a, int32_t b)
{
    uint64_t product = static_cast<uint64_t>(a) * b;
    uint64_t quotient = multiply_int128_high(product, MOD2_MAGIC) >> MOD2_SHIFT;
    uint64_t result = product - quotient * MOD2;
    if (result >= MOD2)
    {
        result -= MOD2;
    }
    return result;
}
int32_t ntt::power_with_mod2(int32_t base, int32_t index)
{
    int32_t answer = 1;
    while (index > 0)
    {
        if (index & 1)
        {
            answer = multiply_mod2(answer, base);
        }
        base = multiply_mod2(base, base);
        index >>= 1;
    }
    return answer;
}
int32_t ntt::modular_inverse2(int32_t base)
{
    return power_with_mod2(base, MOD2 - 2);
}
void ntt::coefficient_normalization2(std::vector<int32_t> &a)
{
    int32_t n = a.size();
    int32_t n_inv = modular_inverse2(n);
    for (int32_t i = 0; i < n; ++i)
    {
        a[i] = multiply_mod2(a[i], n_inv);
    }
}
void ntt::transform_mod2(std::vector<int32_t> &a, bool invert)
{
    int32_t n = a.size();
    bit_reversal_permutation(a);
    std::vector<int32_t> root_of_unity(n / 2, 0);
    int32_t angle = (MOD2 - 1) / n;
    if (invert)
    {
        angle = MOD2 - 1 - angle;
    }
    root_of_unity[0] = 1;
    int32_t angleth_power = power_with_mod2(ROOT2, angle);
    for (int32_t i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod2(root_of_unity[i - 1], angleth_power);
    }
    for (int32_t len = 2; len <= n; len <<= 1)
    {
        int32_t step = n / len;
        for (int32_t i = 0; i < n; i += len)
        {
            for (int32_t j = 0; j < len / 2; j++)
            {
                int32_t u = a[i + j];
                int32_t v = multiply_mod2(a[i + j + len / 2], root_of_unity[step * j]);
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                if (u + v >= MOD2)
                {
                    a[i + j] -= MOD2;
                }
                if (u - v < 0)
                {
                    a[i + j + len / 2] += MOD2;
                }
            }
        }
    }
    if (invert)
    {
        coefficient_normalization2(a);
    }
}

void fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int32_t main()
{
    fastIO();
    int64_t element;
    int64_t N;
    int64_t M;
    std::vector<int32_t> a_list;
    std::vector<int32_t> b_list;
    std::vector<int64_t> answer_list;
    int64_t answer = 0;
    input >> N >> M;
    for (int64_t i = 0; i < N + 1; i++)
    {
        input >> element;
        a_list.push_back(element);
    }
    for (int64_t i = 0; i < M + 1; i++)
    {
        input >> element;
        b_list.push_back(element);
    }
    answer_list = ntt::polynomial_multiplication(a_list, b_list);
    for (int64_t i = 0; i < answer_list.size(); i++)
    {
        answer ^= answer_list[i];
    }
    print << answer;
}