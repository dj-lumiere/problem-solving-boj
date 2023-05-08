/* 13055 K-Inversions */

#include <iostream>
#include <algorithm>
#include <complex>
#include <vector>
#include <hash_map>
#include <map>
#include <hash_set>
#include <set>
#include <deque>
#include <queue>
#include <tuple>

using namespace std;

typedef int64_t int64;
typedef int32_t int32;
typedef __uint128_t unsigned_int128;
typedef uint64_t unsigned_int64;
typedef uint32_t unsigned_int32;
typedef __float128 float128;
typedef long double float80;
typedef double float64;
typedef float float32;
typedef complex<float128> complex128;
typedef complex<float80> complex80;
typedef complex<float64> complex64;
typedef complex<float32> complex32;
typedef string str;
typedef void None;
#define vec vector
#define set unordered_set
#define dict unordered_map
#define heap priority_queue
#define print cout
#define input cin

constexpr float64 pi = 3.14159265358979323846264338327950288419716939937510;

None fft(vec<complex64> &a, bool invert)
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
    vec<complex64> root_of_unity(n / 2);
    for (int64 i = 0; i < n / 2; i++)
    {
        float64 angle;
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
                complex64 u = a[i + j];
                complex64 v = a[i + j + len / 2] * root_of_unity[step * j];
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
    vec<complex64> transformed_a(a.begin(), a.end());
    vec<complex64> transformed_b(b.begin(), b.end());
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
    str target_string;
    input >> target_string;
    vec<int64> a, b;
    for (int32 i = 0; i < target_string.size(); i++)
    {
        if (target_string[i] == 'A')
        {
            a.push_back(1);
            b.push_back(0);
        }
        else if (target_string[i] == 'B')
        {
            a.push_back(0);
            b.push_back(1);
        }
    }
    reverse(a.begin(), a.end());
    vec<int64> inversion = multiply_fft(a, b);
    const int64 inversion_center = target_string.size() - 1;
    for (int32 i = 1; i < target_string.size(); i++)
    {
        print << inversion[inversion_center - i] << "\n";
    }
}