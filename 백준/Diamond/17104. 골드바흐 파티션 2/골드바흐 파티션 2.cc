/* 17104 골드바흐 파티션 2 */

#include <iostream>
#include <algorithm>
#include <complex>
#include <random>

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
#define pi acos(-1)

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
    int64 n = 2;
    while (n < (int64)a.size() + (int64)b.size())
    {
        n <<= 1;
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

vec<int64> sieve(int32 upper_limit)
{
    vec<int64> result((upper_limit - 3) / 2 + 1);
    std::fill_n(result.begin(), result.size(), 1);
    // 홀수인 소수들만 골라내서 계산을 조금 더 편하게 하기 위함
    // result[n] -> 2*n+3의 소수 여부 체크 (합성수면 0이 됨)
    for (int32 i = 0; (2 * i + 3) * (2 * i + 3) <= upper_limit; i++)
    {
        if (result[i])
        {
            int32 current_prime = i * 2 + 3;
            for (int32 j = (current_prime * current_prime - 3) / 2; j < result.size(); j += current_prime)
            {
                result[j] = 0;
            }
        }
    }
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
    fastIO();
    int32 T;
    vec<int64> answer_vec;
    vec<int64> prime_under_1000000 = sieve(1000001);
    answer_vec = multiply_fft(prime_under_1000000, prime_under_1000000);
    input >> T;
    for (int32 i = 0; i < T; i++)
    {
        int32 target;
        input >> target;
        // 4 = 2 + 2.
        if (target == 4)
        {
            print << 1 << "\n";
        }
        else
        {
            int32 target_modify = (target - 6) / 2;
            // 동일한 소수 두 개의 합으로 가능한 경우
            if ((target_modify % 2 == 0) and prime_under_1000000[target_modify / 2])
            {
                print << ((answer_vec[target_modify] - 1) >> 1) + 1 << "\n";
            }
            // 그렇지 않은 경우
            else
            {
                print << (answer_vec[target_modify] >> 1) << "\n";
            }
        }
    }
}