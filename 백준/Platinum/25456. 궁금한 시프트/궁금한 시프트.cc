/* 25456 궁금한 시프트 */

#include <iostream>
#include <algorithm>
#include <complex>
#include <vector>

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
#define print cout
#define input cin

constexpr float64 pi = 3.14159265358979323846264338327950288419716939937510;

// Print vector
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

None fft(vec<complex64>& a, bool invert)
{
    int64 n = a.size();
    // Bit-reversal permutation
    for (int64 i = 1, j = 0; i < n; i++)
    {
        int64 bit = n >> 1;
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
    for (int64 len = 2; len <= n; len <<= 1)
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
        for (int64 i = 0; i < n; i += len)
        {
            complex64 w(1, 0);
            for (int64 j = 0; j < len / 2; j++)
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

vec<int64> multiply_fft(vec<int64>& a, vec<int64>& b)
{
    vec<complex64> transformed_a(a.begin(), a.end());
    vec<complex64> transformed_b(b.begin(), b.end());

    // 리스트 사이즈 변경
    int64 n = 1;
    while (1)
    {
        if (n > (int64)(a.size() + b.size()))
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
    for (int64 i = 0; i < n; i++) {
        transformed_a[i] *= transformed_b[i];
    }

    fft(transformed_a, true);

    vec<int64> result(n);
    for (int64 i = 0; i < n; i++)
    {
        result[i] = round(transformed_a[i].real() / n);
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
    vec<int64> a_list;
    vec<int64> b_list;
    vec<int64> answer_list;
    int64 answer = 0;
    str target_string_a;
    str target_string_b;
    input >> target_string_a;
    input >> target_string_b;

    int64 string_size = target_string_a.size();
    for (int64 i = 0; i < string_size; i++)
    {
        if (target_string_a[i] == '0')
        {
            a_list.push_back(0);
        }
        else if (target_string_a[i] == '1')
        {
            a_list.push_back(1);
        }
    }
    for (int64 i = 0; i < string_size; i++)
    {
        if (target_string_b[i] == '0')
        {
            b_list.push_back(0);
        }
        else if (target_string_b[i] == '1')
        {
            b_list.push_back(1);
        }
    }
    for (int64 i = 0; i < string_size; i++)
    {
        if (target_string_b[i] == '0')
        {
            b_list.push_back(0);
        }
        else if (target_string_b[i] == '1')
        {
            b_list.push_back(1);
        }
    }
    reverse(a_list.begin(), a_list.end());
    answer_list = multiply_fft(a_list, b_list);
    for (int64 i = string_size; i < 2 * string_size; i++)
    {
        if (answer < answer_list[i])
        {
            answer = answer_list[i];
        }
    }
    print << answer;
}