/* 14958 Rock Paper Scissors */

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
    int32 N, K;
    input >> N >> K;
    vec<int64> max_win(N);
    str machine_choices, player_choices;
    input >> machine_choices >> player_choices;
    std::reverse(player_choices.begin(), player_choices.end());
    for (int32 i = 0; i < 3; i++)
    {
        vec<int64> a(N);
        vec<int64> b(K);
        for (int32 j = 0; j < N; j++)
        {
            if (machine_choices[j] == "RPS"[i])
            {
                a[j] = 1;
            }
        }
        for (int32 j = 0; j < K; j++)
        {
            if (player_choices[j] == "PSR"[i])
            {
                b[j] = 1;
            }
        }
        vec<int64> max_win_sub = multiply_fft(a, b);
        for (int32 j = 0; j < N; j++)
        {
            max_win[j] += max_win_sub[j + K - 1];
        }
    }
    int64 answer = 0;
    for (int32 i = 0; i < max_win.size(); i++)
    {
        if (answer < max_win[i])
        {
            answer = max_win[i];
        }
    }
    print << answer;
}