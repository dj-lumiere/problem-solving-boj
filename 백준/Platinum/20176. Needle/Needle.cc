/* 20176 Needle */

#include <iostream>
#include <algorithm>
#include <complex>
#include <vector>

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

None fft(vec<complex80> &a, bool invert)
{
    int64 n = a.size();
    // Bit-reversal permutation
    for (int64 i = 1, j = 0; i < n; i++)
    {
        int64 bit = n >> 1;
        while (not((j ^= bit) & bit))
        {
            bit >>= 1;
        }
        if (i < j)
        {
            std::swap(a[i], a[j]);
        }
    }
    vec<complex80> root_of_unity(n / 2);
    for (int64 i = 0; i < n / 2; i++)
    {
        float80 angle;
        if (invert)
        {
            angle = -2 * pi / n;
        }
        else
        {
            angle = 2 * pi / n;
        }
        root_of_unity[i] = complex80(cos(angle * i), sin(angle * i));
    }
    // 실제 FFT 계산
    for (int64 len = 2; len <= n; len <<= 1)
    {
        int64 step = n / len;
        // n-th root of unity
        for (int64 i = 0; i < n; i += len)
        {
            for (int64 j = 0; j < len / 2; j++)
            {
                complex80 u = a[i + j];
                complex80 v = a[i + j + len / 2] * root_of_unity[step * j];
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
            }
        }
    }
    if (invert)
    {
        for (int64 i = 0; i < n; i++)
        {
            a[i] /= n;
        }
    }
}

vec<int64> multiply_fft(vec<int64> &a, vec<int64> &b)
{
    vec<complex80> transformed_a(a.begin(), a.end());
    vec<complex80> transformed_b(b.begin(), b.end());
    // 리스트 사이즈 변경
    int32 n = 2;
    while (1)
    {
        if (n >= (int32)(a.size() + b.size()))
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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int32 main()
{
    fastIO();
    int32 n_u, n_m, n_l;
    const int32 barrier_peak_to_peak = 60001;
    const int32 convert_to_positive = 30000;
    vec<int64> upper_barrier(barrier_peak_to_peak), middle_barrier(barrier_peak_to_peak), lower_barrier(barrier_peak_to_peak);
    input >> n_u;
    for (int32 i = 0; i < n_u; i++)
    {
        int64 element;
        input >> element;
        upper_barrier[element + convert_to_positive] = 1;
    }
    input >> n_m;
    for (int32 i = 0; i < n_m; i++)
    {
        int64 element;
        input >> element;
        middle_barrier[element + convert_to_positive] = 1;
    }
    input >> n_l;
    for (int32 i = 0; i < n_l; i++)
    {
        int64 element;
        input >> element;
        lower_barrier[element + convert_to_positive] = 1;
    }
    vec<int64> result = multiply_fft(upper_barrier, lower_barrier);
    int64 answer = 0;
    for (int32 i = 0; i < barrier_peak_to_peak; i++)
    {
        answer += middle_barrier[i] * result[2 * i];
    }
    print << answer << "\n";
}