/* 17134 르모앙의 추측 */

#include <iostream>
#include <algorithm>
#include <complex>
#include <random>

#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

#define int128 __int128_t
#define int64 int64_t
#define int32 int32_t
#define unsigned_int128 __uint128_t
#define unsigned_int64 uint64_t
#define unsigned_int32 uint32_t
#define float128 __float128
#define float80 long double
#define float64 double
#define float32 float
#define complex128 std::complex<float128>
#define complex80 std::complex<float80>
#define complex64 std::complex<float64>
#define complex32 std::complex<float32>
#define complex_int32 complex64
#define str std::string
#define vec std::vector
#define set std::unordered_set
#define dict std::map
#define deque std::deque
#define tuple std::tuple
#define heap std::priority_queue
#define print std::cout
#define input std::cin
#define None void
#define pi (float80)3.14159265358979323846264338327950288419716939937510

template <typename T>
std::ostream &operator<<(std::ostream &os, const vec<T> &target)
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

None fft(vec<complex64> &a, bool invert)
{
    int32 n = a.size();
    // Bit-reversal permutation
    for (int32 i = 1, j = 0; i < n; i++)
    {
        int32 bit = n >> 1;
        while (not((j ^= bit) & bit))
        {
            bit >>= 1;
        }
        if (i < j)
        {
            std::swap(a[i], a[j]);
        }
    }
    // 실제 FFT 계산
    for (int32 len = 2; len <= n; len <<= 1)
    {
        float64 angle;
        if (invert)
        {
            angle = -2 * pi / len;
        }
        else
        {
            angle = 2 * pi / len;
        }
        complex64 omega(cos(angle), sin(angle)); // n-th root of unity
        for (int32 i = 0; i < n; i += len)
        {
            complex64 w(1, 0);
            for (int32 j = 0; j < len / 2; j++)
            {
                complex64 u = a[i + j];
                complex64 v = a[i + j + len / 2] * w;
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                w *= omega;
            }
        }
    }
    if (invert)
    {
        for (int32 i = 0; i < n; i++)
        {
            a[i] /= n;
        }
    }
}

vec<int64> multiply_fft(vec<int64> &a, vec<int64> &b)
{
    vec<complex64> transformed_a(a.begin(), a.end());
    vec<complex64> transformed_b(b.begin(), b.end());
    // 리스트 사이즈 변경
    int32 n = 1;
    while (1)
    {
        if (n > (int32)(a.size() + b.size()))
        {
            break;
        }
        else
        {
            n <<= 1;
        }
    }
    transformed_a.resize(n);
    transformed_b.resize(n);
    fft(transformed_a, false);
    fft(transformed_b, false);
    for (int32 i = 0; i < n; i++)
    {
        transformed_a[i] *= transformed_b[i];
    }
    fft(transformed_a, true);

    vec<int64> result(n);
    for (int32 i = 0; i < n; i++)
    {
        result[i] = round(transformed_a[i].real());
    }
    return result;
}

vec<int32> sieve(int32 upper_limit)
{
    vec<bool> not_prime_check(upper_limit + 1);
    not_prime_check[0] = true;
    not_prime_check[1] = true;
    for (int32 i = 2; i * i <= upper_limit; i++)
    {
        if (not not_prime_check[i])
        {
            for (int32 j = 2; i * j <= upper_limit; j++)
            {
                not_prime_check[i * j] = true;
            }
        }
    }
    vec<int32> prime_list;
    for (int32 i = 2; i <= upper_limit; i++)
    {
        if (not not_prime_check[i])
        {
            prime_list.push_back(i);
        }
    }
    return prime_list;
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
    int32 T;
    vec<int64> semi_prime_vec(1000001);
    vec<int64> semi_prime_vec_sub;
    vec<int64> odd_prime_vec(1000001);
    vec<int64> answer_vec;
    vec<int32> prime_under_1000000 = sieve(1000000);
    for (int32 i = 0; i < prime_under_1000000.size(); i++)
    {
        if (prime_under_1000000[i] * 2 <= 1000000)
        {
            semi_prime_vec_sub.push_back(prime_under_1000000[i] * 2);
        }
        else
        {
            break;
        }
    }

    for (int32 i = 0; i < semi_prime_vec_sub.size(); i++)
    {
        semi_prime_vec[semi_prime_vec_sub[i]] = 1;
    }
    for (int32 i = 1; i < prime_under_1000000.size(); i++)
    {
        odd_prime_vec[prime_under_1000000[i]] = 1;
    }
    answer_vec = multiply_fft(semi_prime_vec, odd_prime_vec);
    input >> T;
    for (int32 i = 0; i < T; i++)
    {
        int32 target;
        input >> target;
        print << answer_vec[target] << "\n";
    }
}