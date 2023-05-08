/* 14756 Telescope */

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
#define pi (float64)3.14159265358979323846264338327950288419716939937510

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
std::ostream &operator<<(std::ostream &os, const int128 &num)
{
    // If the int128 is zero, just print it and return
    if (num == 0)
    {
        os << '0';
        return os;
    }

    // If the int128 is negative, print the minus sign and take its absolute value
    int128 temp = num;
    if (temp < 0)
    {
        os << '-';
        temp = -temp;
    }

    // Convert the int128 to a string in reverse order
    str answer;
    while (temp > 0)
    {
        answer.push_back(static_cast<char>('0' + temp % 10));
        temp /= 10;
    }

    // Reverse the string and print it
    std::reverse(answer.begin(), answer.end());
    os << answer;
    return os;
}

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
        root_of_unity[i] = complex64(cos(angle * i), sin(angle * i));
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
    int64 n = 2;
    while (1)
    {
        if (n >= (int64)(a.size() + b.size()))
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
    for (int64 i = 0; i < n; i++)
    {
        transformed_a[i] *= transformed_b[i];
    }
    fft(transformed_a, true);
    vec<int64> result(n);
    for (int64 i = 0; i < n; i++)
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
    int64 N, L, M, W;
    int64 element;
    vec<int64> raw_path_sub, raw_telescope_sub;
    vec<vec<int64>> raw_path, raw_telescope;
    vec<int64> path_processed_sub;
    input >> N >> L >> M >> W;
    vec<int64> path_processed(N - L + 1);
    for (int64 i = 0; i < M; i++)
    {
        for (int64 j = 0; j < N; j++)
        {
            input >> element;
            raw_path_sub.push_back(element);
        }
        raw_path.push_back(raw_path_sub);
        raw_path_sub.clear();
    }
    for (int64 i = 0; i < M; i++)
    {
        for (int64 j = 0; j < L; j++)
        {
            input >> element;
            raw_telescope_sub.push_back(element);
        }
        reverse(raw_telescope_sub.begin(), raw_telescope_sub.end());
        raw_telescope.push_back(raw_telescope_sub);
        raw_telescope_sub.clear();
    }
    for (int64 h = 0; h < M; h++)
    {
        path_processed_sub = multiply_fft(raw_path[h], raw_telescope[h]);
        for (int64 i = 0; i < path_processed.size(); i++)
        {
            path_processed[i] += path_processed_sub[i + L - 1];
        }
    }
    int64 answer = 0;
    for (int64 i = 0; i < path_processed.size(); i++)
    {
        if (path_processed[i] > W)
        {
            answer += 1;
        }
    }
    print << answer;
}