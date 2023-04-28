/* 17105 골드바흐 트리플 */

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
typedef long double float80;
typedef double float64;
typedef float float32;
typedef complex<float80> complex80;
typedef complex<float64> complex64;
typedef complex<float32> complex32;
typedef string str;
typedef void None;
#define vec vector
#define print cout
#define input cin

constexpr float64 pi = 3.14159265358979323846264338327950288419716939937510;

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
    vec<int64> result(upper_limit + 1);
    std::fill_n(result.begin(), result.size(), 1);
    result[0] = 0;
    result[1] = 0;
    for (int32 i = 2; i * i <= upper_limit; i++)
    {
        if (result[i])
        {
            for (int32 j = 2; i * j <= upper_limit; j++)
            {
                result[i * j] = 0;
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
    int64 T;
    vec<int64> raw_prime_under_1000000 = sieve(1000000);
    vec<int64> odd_prime_under_1000000(500000);
    vec<int64> raw_odd_prime_under_500000(500000);
    for (int32 i = 3; i < 1000000; i++)
    {
        if (raw_prime_under_1000000[i])
        {
            odd_prime_under_1000000[(i - 1) / 2] = 1;
            if (i - 1 < 500000)
            {
                raw_odd_prime_under_500000[i - 1] = 1;
            }
        }
    }
    // Case for a pair of odd prime and one different prime
    vec<int64> case_for_one_different_odd = multiply_fft(odd_prime_under_1000000, raw_odd_prime_under_500000);
    vec<int64> prime_under_1000000_squared = multiply_fft(odd_prime_under_1000000, odd_prime_under_1000000);
    // Case for three different odd prime
    vec<int64> case_for_three_different_odd = multiply_fft(odd_prime_under_1000000, prime_under_1000000_squared);
    // print << prime_under_1000000 << "\n" << prime_under_500000 << endl;
    // print << case_for_one_different_odd << "\n" << case_for_three_different_odd << endl;
    input >> T;
    for (int64 i = 0; i < T; i++)
    {
        int64 target;
        input >> target;
        // 7 = 2 + 2 + 3.
        if (target == 7)
        {
            print << 1 << "\n";
        }
        else
        {
            int64 target_1 = (target - 3) / 2;
            int64 target_2 = (target - 5) / 2;
            int64 answer = 0;
            // 일단 경우를 중복해서 구하기
            answer += case_for_three_different_odd[target_1];
            // p, p, r의 경우 (이거는 이미 case_for_three_different_odd에서 3배됨)
            answer += 3 * case_for_one_different_odd[target_1];
            if (not(target % 3) and (odd_prime_under_1000000[target_1 / 3]))
            {
                // p, p, p의 경우 (이거는 이미 case_for_three_different_odd에서 3배됨)
                answer += 2;
            }
            answer /= 6;
            // 2, 2, r의 경우 (이거는 처음부터 안 구해짐)
            answer += odd_prime_under_1000000[target_2];
            print << answer << "\n";
        }
    }
}