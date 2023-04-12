/* 15576번 큰 수 곱셈 (2) */

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
#define list std::vector
#define set std::unordered_set
#define dict std::map
#define deque std::deque
#define tuple std::tuple
#define heap std::priority_queue
#define print std::cout
#define input std::cin
#define None void
#define pi acos(-1)

None fft(list<complex64>& a, bool invert)
{
    int32 n = a.size();
    // Bit-reversal permutation
    for (int32 i = 1, j = 0; i < n; i++)
    {
        int32 bit = n >> 1;
        while (not ((j ^= bit) & bit))
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
}

list<int32> multiply_fft(list<int32>& a, list<int32>& b)
{
    list<complex64> transformed_a(a.begin(), a.end());
    list<complex64> transformed_b(b.begin(), b.end());

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
    for (int32 i = 0; i < n; i++) {
        transformed_a[i] *= transformed_b[i];
    }
    fft(transformed_a, true);

    list<int32> result(n);
    for (int32 i = 0; i < n; i++)
    {
        result[i] = round(transformed_a[i].real() / n);
    }
    for (int32 i = 0; i < n - 1; i++) {
        if (result[i] > 9){
            int32 div = result[i] / 10;
            int32 mod = result[i] % 10;
            result[i + 1] += div;
            result[i] = mod;
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
    str a, b;
    list<int32> a_list;
    list<int32> b_list;
    list<int32> answer_list;
    input >> a >> b;
    for (str::reverse_iterator rit = a.rbegin(); rit != a.rend();++rit) {
        a_list.push_back((int32)(*rit - 48));
    }
    for (str::reverse_iterator rit = b.rbegin(); rit != b.rend(); ++rit) {
        b_list.push_back((int32)(*rit - 48));
    }
    int32 a_digit = a_list.size();
    int32 b_digit = b_list.size();
    answer_list = multiply_fft(a_list, b_list);
    for (int32 i = a_digit + b_digit - 1; i >= 0; i--) {
        if (i != a_digit + b_digit - 1) {
            print << answer_list[i];
        }
        else if ((i = a_digit + b_digit - 1) and (answer_list[i] != 0)) {
            print << answer_list[i];
        }
    }
}