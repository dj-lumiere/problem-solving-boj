/* 26161 트리의 팔 */

#include <iostream>
#include <cstdint>
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
#include <type_traits>
#include <bit>
#include <bitset>
#include <numbers>
#include <regex>
#include <numeric>
#include <array>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

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

template <typename T>
T max(vector<T> &target)
{
    return *max_element(target.begin(), target.end());
}

template <typename T>
T min(vector<T> &target)
{
    return *min_element(target.begin(), target.end());
}

template <typename T>
int32 bit_length(T target)
{
    return bit_width(target);
}

int64_t randint(int64_t lower_bound, int64_t upper_bound)
{
    static random_device rd;
    static mt19937 gen(rd());
    uniform_int_distribution<int64_t> dist(lower_bound, upper_bound);
    int64_t x = dist(gen);
    return x;
}

namespace ntt
{
    const uint64_t MOD = 4255901651992313857;
    const uint32_t INT32_BITMASK = 0xffffffff;

    const uint32_t MOD1 = 2013265921;
    const uint64_t MOD1_MAGIC = 2459565875272927297;
    const uint32_t MOD1_MULINV = 21;
    const uint32_t MOD1_SHIFT = 28;
    const uint32_t ROOT1 = 31;

    const uint32_t MOD2 = 2113929217;
    const uint64_t MOD2_MAGIC = 2342443690791526205;
    const uint32_t MOD2_MULINV = 2013265901;
    const uint32_t MOD2_SHIFT = 28;
    const uint32_t ROOT2 = 5;

    uint64_t multiply_int128_high(uint64_t a, uint64_t b);
    int64_t merge_remainder(int64_t remainder1, int64_t remainder2);
    int64_t find_bit_ceil(int64_t a);
    void bit_reversal_permutation(std::vector<int64_t> &a);
    std::vector<int64_t> polynomial_multiplication(std::vector<int64_t> &a, std::vector<int64_t> &b);

    int64_t multiply_mod1(int64_t a, int64_t b);
    int64_t power_with_mod1(int64_t base, int64_t index);
    int64_t modular_inverse1(int64_t base);
    void coefficient_normalization1(std::vector<int64_t> &a);
    void transform_mod1(std::vector<int64_t> &a, bool invert);

    int64_t multiply_mod2(int64_t a, int64_t b);
    int64_t power_with_mod2(int64_t base, int64_t index);
    int64_t modular_inverse2(int64_t base);
    void coefficient_normalization2(std::vector<int64_t> &a);
    void transform_mod2(std::vector<int64_t> &a, bool invert);
}

int64_t ntt::merge_remainder(int64_t remainder1, int64_t remainder2)
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
int64_t ntt::find_bit_ceil(int64_t a)
{
    return static_cast<int64_t>(ceil(log2(a)));
}
void ntt::bit_reversal_permutation(std::vector<int64_t> &a)
{
    int64_t n = a.size();
    for (int64_t i = 1, j = 0; i < n; ++i)
    {
        int64_t bit = n >> 1;
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
std::vector<int64_t> ntt::polynomial_multiplication(std::vector<int64_t> &a, std::vector<int64_t> &b)
{
    int64_t original_size = a.size() + b.size();
    int64_t n = 1 << ntt::find_bit_ceil(original_size);
    std::vector<int64_t> result(original_size);

    std::vector<int64_t> transform_a_mod1(a.begin(), a.end());
    transform_a_mod1.resize(n);
    ntt::transform_mod1(transform_a_mod1, false);

    std::vector<int64_t> transform_b_mod1(b.begin(), b.end());
    transform_b_mod1.resize(n);
    ntt::transform_mod1(transform_b_mod1, false);

    std::vector<int64_t> transform_a_mod2(a.begin(), a.end());
    transform_a_mod2.resize(n);
    ntt::transform_mod2(transform_a_mod2, false);

    std::vector<int64_t> transform_b_mod2(b.begin(), b.end());
    transform_b_mod2.resize(n);
    ntt::transform_mod2(transform_b_mod2, false);

    for (int64_t i = 0; i < n; i++)
    {
        transform_a_mod1[i] = multiply_mod1(transform_a_mod1[i], transform_b_mod1[i]);
        transform_a_mod2[i] = multiply_mod2(transform_a_mod2[i], transform_b_mod2[i]);
    }

    ntt::transform_mod1(transform_a_mod1, true);
    transform_a_mod1.resize(original_size);

    ntt::transform_mod2(transform_a_mod2, true);
    transform_a_mod2.resize(original_size);

    for (int64_t i = 0; i < original_size; i++)
    {
        result[i] = merge_remainder(transform_a_mod1[i], transform_a_mod2[i]);
    }

    return result;
}

int64_t ntt::multiply_mod1(int64_t a, int64_t b)
{
    uint64_t product = static_cast<uint64_t>(a) * b;
    uint64_t quotient = static_cast<__uint128_t>(product) * MOD1_MAGIC >> (MOD1_SHIFT + 64);
    uint64_t result = product - quotient * MOD1;
    if (result >= MOD1)
    {
        result -= MOD1;
    }
    return static_cast<int64_t>(result);
}
int64_t ntt::power_with_mod1(int64_t base, int64_t index)
{
    int64_t answer = 1;
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
int64_t ntt::modular_inverse1(int64_t base)
{
    return power_with_mod1(base, MOD1 - 2);
}
void ntt::coefficient_normalization1(std::vector<int64_t> &a)
{
    int64_t n = a.size();
    int64_t n_inv = modular_inverse1(n);
    for (int64_t i = 0; i < n; ++i)
    {
        a[i] = multiply_mod1(a[i], n_inv);
    }
}
void ntt::transform_mod1(std::vector<int64_t> &a, bool invert)
{
    int64_t n = a.size();
    bit_reversal_permutation(a);
    std::vector<int64_t> root_of_unity(n / 2, 0);
    int64_t angle = (MOD1 - 1) / n;
    if (invert)
    {
        angle = MOD1 - 1 - angle;
    }
    root_of_unity[0] = 1;
    int64_t angleth_power = power_with_mod1(ROOT1, angle);
    for (int64_t i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod1(root_of_unity[i - 1], angleth_power);
    }
    for (int64_t len = 2; len <= n; len <<= 1)
    {
        int64_t step = n / len;
        for (int64_t i = 0; i < n; i += len)
        {
            for (int64_t j = 0; j < len / 2; j++)
            {
                int64_t u = a[i + j];
                int64_t v = multiply_mod1(a[i + j + len / 2], root_of_unity[step * j]);
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

int64_t ntt::multiply_mod2(int64_t a, int64_t b)
{
    uint64_t product = static_cast<uint64_t>(a) * b;
    uint64_t quotient = static_cast<__uint128_t>(product) * MOD2_MAGIC >> (MOD2_SHIFT + 64);
    uint64_t result = product - quotient * MOD2;
    if (result >= MOD2)
    {
        result -= MOD2;
    }
    return result;
}
int64_t ntt::power_with_mod2(int64_t base, int64_t index)
{
    int64_t answer = 1;
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
int64_t ntt::modular_inverse2(int64_t base)
{
    return power_with_mod2(base, MOD2 - 2);
}
void ntt::coefficient_normalization2(std::vector<int64_t> &a)
{
    int64_t n = a.size();
    int64_t n_inv = modular_inverse2(n);
    for (int64_t i = 0; i < n; ++i)
    {
        a[i] = multiply_mod2(a[i], n_inv);
    }
}
void ntt::transform_mod2(std::vector<int64_t> &a, bool invert)
{
    int64_t n = a.size();
    bit_reversal_permutation(a);
    std::vector<int64_t> root_of_unity(n / 2, 0);
    int64_t angle = (MOD2 - 1) / n;
    if (invert)
    {
        angle = MOD2 - 1 - angle;
    }
    root_of_unity[0] = 1;
    int64_t angleth_power = power_with_mod2(ROOT2, angle);
    for (int64_t i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod2(root_of_unity[i - 1], angleth_power);
    }
    for (int64_t len = 2; len <= n; len <<= 1)
    {
        int64_t step = n / len;
        for (int64_t i = 0; i < n; i += len)
        {
            for (int64_t j = 0; j < len / 2; j++)
            {
                int64_t u = a[i + j];
                int64_t v = multiply_mod2(a[i + j + len / 2], root_of_unity[step * j]);
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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

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

int32_t main()
{
    fastIO();
    const int64 MOD = 1000000007;
    int32 N, R;
    input >> N >> R;
    vector<vector<int32>> tree(N + 1);
    vector<int64> leaf_count_in_depth_i(N + 1, 0);
    vector<bool> visited(N + 1, false);
    for (int32 i = 0; i < N - 1; ++i)
    {
        int32 u, v;
        input >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    vector<vector<int32>> s;
    s.push_back({R, 0});

    while (not s.empty())
    {
        int32 node = s[s.size() - 1][0];
        int32 depth = s[s.size() - 1][1];
        s.pop_back();

        visited[node] = true;

        if (tree[node].size() == 1 and node != R)
        {
            leaf_count_in_depth_i[depth] += 1;
        }

        for (const int32 &next_node : tree[node])
        {
            if (not visited[next_node])
            {
                s.push_back({next_node, depth + 1});
            }
        }
    }
    //print << leaf_count_in_depth_i << "\n";
    vector<int64> result = ntt::polynomial_multiplication(leaf_count_in_depth_i, leaf_count_in_depth_i);
    //print << result << "\n";
    result.resize(N + 1);
    vector<int64> result_accumulated_sum = {};
    for (int32 i = 0; i <= N; i++)
    {
        if (i == 0)
        {
            result_accumulated_sum.append(result[0]);
            continue;
        }
        result_accumulated_sum.append((result_accumulated_sum[result_accumulated_sum.size() - 1] + result[i]) % MOD);
    }
    int32 Q;
    //print << result_accumulated_sum << "\n";
    input >> Q;
    for (int32 i = 0; i < Q; ++i)
    {
        int32 W, V;
        input >> W >> V;
        print << (result_accumulated_sum[V] - result_accumulated_sum[W - 1] + MOD) % MOD << "\n";
    }
}
