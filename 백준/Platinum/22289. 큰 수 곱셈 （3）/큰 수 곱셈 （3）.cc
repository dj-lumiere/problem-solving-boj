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

list<int64> multiply_fft(list<int64>& a, list<int64>& b)
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
    for (int32 i = 0; i < n; i++)
    {
        transformed_a[i] *= transformed_b[i];
    }
    fft(transformed_a, true);

    list<int64> result(n);
    for (int32 i = 0; i < n; i++)
    {
        result[i] = round(transformed_a[i].real());
    }
    for (int32 i = 0; i < n - 1; i++)
    {
        if (result[i] > 9)
        {
            int64 div = result[i] / 100;
            int64 mod = result[i] % 100;
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
    list<int64> answer_list;
    input >> a >> b;
    for (str::reverse_iterator rit = a.rbegin(); rit != a.rend(); ++rit)
    {
        a_list.push_back((int32)(*rit - 48));
    }
    for (str::reverse_iterator rit = b.rbegin(); rit != b.rend(); ++rit)
    {
        b_list.push_back((int32)(*rit - 48));
    }
    int32 a_digit = a_list.size();
    int32 b_digit = b_list.size();
    for (int32 i = 0; i < 4; i++)
    {
        a_list.push_back(0);
        b_list.push_back(0);
    }
    list<int64> new_a_list;
    list<int64> new_b_list;
    for (int32 i = 0; i < (a_digit >> 1) + 1; i++)
    {
        int64 element_a = 0;
        int32 multiplier = 1;
        for (int32 j = 0; j < 2; j++)
        {
            element_a += multiplier * a_list[2 * i + j];
            multiplier *= 10;
        }
        new_a_list.push_back(element_a);
    }
    for (int32 i = 0; i < (b_digit >> 1) + 1; i++)
    {
        int64 element_b = 0;
        int32 multiplier = 1;
        for (int32 j = 0; j < 2; j++)
        {
            element_b += multiplier * b_list[2 * i + j];
            multiplier *= 10;
        }
        new_b_list.push_back(element_b);
    }
    int32 new_a_digit = new_a_list.size();
    int32 new_b_digit = new_b_list.size();
    answer_list = multiply_fft(new_a_list, new_b_list);
    int32 first_digit_index = 0;
    for (int32 i = answer_list.size() - 1; i >= 0; i--) {
        if (answer_list[i] != 0) {
            first_digit_index = i;
            break;
        }
    }
    for (int32 i = first_digit_index; i >= 0; i--) {
        if (i == first_digit_index) {
            print << answer_list[i];
        }
        else {
            if (answer_list[i] < 10) {
                print << "0" << answer_list[i];
            }
            else {
                print << answer_list[i];
            }
        }
    }
}