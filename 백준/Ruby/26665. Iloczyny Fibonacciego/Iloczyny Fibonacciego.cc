#include <iostream>
#include <algorithm>
#include <complex>
#include <random>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <queue>
#include <cmath>
#include <list>
#include <set>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

typedef __int128_t int128;
typedef int64_t int64;
typedef int32_t int32;
typedef __uint128_t uint128;
typedef uint64_t uint64;
typedef uint32_t uint32;
typedef long double float80;
typedef double float64;
typedef float float32;
typedef complex<float80> complex80;
typedef complex<float64> complex64;
typedef complex<float32> complex32;
typedef string str;
typedef void None;
#define vec std::vector
#define linked_list std::list
#define dict std::unordered_map
#define tree_set std::set
#define heap std::priority_queue
#define print std::cout
#define input std::cin
#define append std::push_back
#define appendleft std::push_front
#define popleft std::pop_front
constexpr float64 pi = 3.14159265358979323846264338327950288419716939937510;

std::ostream &operator<<(std::ostream &os, vec<int64> &target)
{
    os << target.size() << " ";
    for (int64 index = 0; index < target.size(); index++)
    {
        os << target[index];
        if (index + 1 != target.size())
        {
            os << " ";
        }
    }
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
            swap(a[i], a[j]);
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
        for (int32 i = 0; i < n; i += len)
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
    int64 a_size = a.size();
    int64 b_size = b.size();
    // 리스트 사이즈 변경
    int64 n = 2;
    while (1)
    {
        if (n >= (int64)(a_size + b_size))
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

    int64 result_size = a_size + b_size - 1;
    vec<int64> result(result_size);
    for (int64 i = 0; i < result_size; i++)
    {
        result[i] = round(transformed_a[i].real());
    }
    return result;
}

// Converts Zeckendorf Representation to Lucas Representation.
vec<int64> zeckendorf_to_lucas(vec<int64> &target)
{
    if (target.size() < static_cast<uint64>(3))
    {
        target.resize(3);
    }
    // 마지막의 계수 정리는 돌려야하니 길이를 정해두기
    // Zeckendorf와 다르게 L(0)부터 시작함(Zeckendorf에서는 F(2)부터 시작함.)
    vec<int64> result(target.size() + 1, 0);
    // 왼쪽(높은 자릿수, 리스트 뒷쪽)에서 오른쪽(낮은 자릿수, 리스트 앞쪽)으로 다음과 같이 옮기기
    for (int64 index = target.size() - 1; index >= 3; index--)
    {
        // x001 -> x110
        if ((target[index - 2] == 0) and (target[index - 1] == 0) and (target[index - 0] == 1))
        {
            target[index - 2] = 1;
            target[index - 1] = 1;
            target[index - 0] = 0;
        }
        // x101 -> x0'0'0, i-1자리 +1
        else if ((target[index - 2] == 1) and (target[index - 1] == 0) and (target[index - 0] == 1))
        {
            target[index - 2] = 0;
            target[index - 1] = 0;
            target[index - 0] = 0;
            result[index + 1] += 1;
        }
        // 0011 -> 1101 -> 10'0'0, i-1자리 +1
        else if ((target[index - 3] == 0) and (target[index - 2] == 0) and (target[index - 1] == 1) and (target[index - 0] == 1))
        {
            target[index - 3] = 1;
            target[index - 2] = 0;
            target[index - 1] = 0;
            target[index - 0] = 0;
            result[index + 1] += 1;
        }
        // 1011 -> 0'0'01 -> 0'1'10, i-2자리 +1
        else if ((target[index - 3] == 1) and (target[index - 2] == 0) and (target[index - 1] == 1) and (target[index - 0] == 1))
        {
            target[index - 3] = 0;
            target[index - 2] = 1;
            target[index - 1] = 1;
            target[index - 0] = 0;
            result[index + 0] += 1;
        }
        // 0111 -> 00'1'0, i-1자리 +1
        else if ((target[index - 3] == 0) and (target[index - 2] == 1) and (target[index - 1] == 1) and (target[index - 0] == 1))
        {
            target[index - 3] = 0;
            target[index - 2] = 0;
            target[index - 1] = 1;
            target[index - 0] = 0;
            result[index + 1] += 1;
        }
    }
    // 1
    if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 1)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[1] += 1;
    }
    // 2
    else if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 2)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[0] += 1;
    }
    // 3
    if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 3)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[2] += 1;
    }
    // 4
    else if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 4)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[3] += 1;
    }
    // 5
    else if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 5)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[1] += 1;
        result[3] += 1;
    }
    // 6
    else if (target[0] * 1 + target[1] * 2 + target[2] * 3 == 6)
    {
        target[0] == 0;
        target[1] == 0;
        target[2] == 0;
        result[0] += 1;
        result[3] += 1;
    }
    // 어차피 중간단계라 마지막은 딱히 정리하지 않음.
    return result;
}

// Converts Lucas Representation to Golden ratio base.
vec<int64> lucas_to_phinary(vec<int64> &target)
{
    vec<int64> result(target.size() * 2 - 1, 0);
    result[target.size() - 1] = target[0] * 2;
    for (int64 index = 1; index < target.size(); index++)
    {
        result[target.size() + index - 1] += target[index];
        result[target.size() - index - 1] += -target[index];
        if (index % 2 == 0)
        {
            result[target.size() - index - 1] += target[index] * 2;
        }
    }
    return result;
}

// Converts golden ration base to Lucas representation
vec<int64> phinary_to_lucas(vec<int64> &target)
{
    int64 index_zero_point = (target.size() - 1) / 2;
    int64 digits_in_lucas = target.size() - index_zero_point;
    vec<int64> result(digits_in_lucas, 0);
    result[0] = target[index_zero_point] / 2;
    for (int64 index = 1; index < result.size(); index++)
    {
        result[index] = target[index + index_zero_point];
    }
    return result;
}
// Converts Lucas representation to Zeckendorf representation
vec<int64> lucas_to_zeckendorf(vec<int64> &target)
{
    // L(N) = F(N+1) + F(N-1)
    vec<int64> result(target.size() - 1, 0);
    for (int64 index = 1; index < target.size(); index++)
    {
        result[index - 1] += target[index];
    }
    for (int64 index = 3; index < target.size(); index++)
    {
        result[index - 3] += target[index];
    }
    result[0] += target[0] * 2 + target[2];
    return result;
}

None remove_trailing_zero(vec<int64> &target)
{
    for (auto element = target.rbegin(); element != target.rend(); ++element)
    {
        if (*element == 0)
        {
            target.pop_back();
        }
        else
        {
            break;
        }
    }
}

vec<int64> coefficient_normalization_for_add_and_sub(bool subtraction_check, vec<int64> &result)
{
    if (subtraction_check)
    {
        for (int64 index = result.size() - 2; index > -1; index--)
        {
            // 00z -> 11'x'
            if ((result[index + 0] == 0) and (result[index + 1] == 0) and ((result[index + 2] == 1) or (result[index + 2] == 2)))
            {
                result[index + 0] = 1;
                result[index + 1] = 1;
                result[index + 2] -= 1;
            }
            // 0'1'z -> 10'x'
            else if ((result[index + 0] == 0) and (result[index + 1] == -1) and ((result[index + 2] == 1) or (result[index + 2] == 2)))
            {
                result[index + 0] = 1;
                result[index + 1] = 0;
                result[index + 2] -= 1;
            }
            // 1'1'z -> 20'x'
            else if ((result[index + 0] == 1) and (result[index + 1] == -1) and ((result[index + 2] == 1) or (result[index + 2] == 2)))
            {
                result[index + 0] = 2;
                result[index + 1] = 0;
                result[index + 2] -= 1;
            }
            // '1'0x -> 01'x'
            else if ((result[index + 0] == -1) and (result[index + 1] == 0) and ((result[index + 2] == 1) or (result[index + 2] == 2)))
            {
                result[index + 0] = 0;
                result[index + 1] = 1;
                result[index + 2] -= 1;
            }
        }
    }
    for (int64 index = result.size() - 3; index > -1; index--)
    {
        // x020 -> 'x'001
        if ((result[index + 1] == 0) and (result[index + 2] == 2) and (result[index + 3] == 0))
        {
            result[index + 0] += 1;
            result[index + 1] = 0;
            result[index + 2] = 0;
            result[index + 3] = 1;
        }
        // x030 -> 'x'011
        if ((result[index + 1] == 0) and (result[index + 2] == 3) and (result[index + 3] == 0))
        {
            result[index + 0] += 1;
            result[index + 1] = 0;
            result[index + 2] = 1;
            result[index + 3] = 1;
        }
        // x120 -> x011
        if ((result[index + 1] == 1) and (result[index + 2] == 2) and (result[index + 3] == 0))
        {
            result[index + 1] = 0;
            result[index + 2] = 1;
            result[index + 3] = 1;
        }
        // x210 -> x101
        if ((result[index + 1] == 2) and (result[index + 2] == 1) and (result[index + 3] == 0))
        {
            result[index + 1] = 1;
            result[index + 2] = 0;
            result[index + 3] = 1;
        }
    }
    // 0
    if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 0)
    {
        result[0] = 0;
        result[1] = 0;
        result[2] = 0;
    }
    // 1
    if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 1)
    {
        result[0] = 1;
        result[1] = 0;
        result[2] = 0;
    }
    // 2
    else if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 2)
    {
        result[0] = 0;
        result[1] = 1;
        result[2] = 0;
    }
    // 3
    else if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 3)
    {
        result[0] = 0;
        result[1] = 0;
        result[2] = 1;
    }
    // 4
    else if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 4)
    {
        result[0] = 1;
        result[1] = 0;
        result[2] = 1;
    }
    // 5
    else if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 5)
    {
        result[0] = 0;
        result[1] = 1;
        result[2] = 1;
    }
    // 6
    else if (result[0] * 1 + result[1] * 2 + result[2] * 3 == 6)
    {
        result[0] = 1;
        result[1] = 1;
        result[2] = 1;
    }
    for (int64 index = 0; index <= result.size() - 2; index++)
    {
        if ((result[index + 0] == 1) and (result[index + 1] == 1) and (result[index + 2] == 0))
        {
            result[index + 0] = 0;
            result[index + 1] = 0;
            result[index + 2] = 1;
        }
    }
    for (int64 index = result.size() - 3; index > -1; index--)
    {
        if ((result[index + 0] == 1) and (result[index + 1] == 1) and (result[index + 2] == 0))
        {
            result[index + 0] = 0;
            result[index + 1] = 0;
            result[index + 2] = 1;
        }
    }
    return result;
}
vec<int64> zeckendorf_addition(vec<int64> &target1, vec<int64> &target2)
{
    vec<int64> result(target1.size());
    for (int64 index = 0; index < target1.size(); index++)
    {
        result[index] += target1[index];
    }
    for (int64 index = 0; index < target2.size(); index++)
    {
        result[index] += target2[index];
    }
    result = coefficient_normalization_for_add_and_sub(false, result);
    return result;
}

vec<int64> zeckendorf_subtraction(vec<int64> &target1, vec<int64> &target2)
{
    vec<int64> result(target1.size());
    for (int64 index = 0; index < target1.size(); index++)
    {
        result[index] += target1[index];
    }
    for (int64 index = 0; index < target2.size(); index++)
    {
        result[index] -= target2[index];
    }
    result = coefficient_normalization_for_add_and_sub(true, result);
    return result;
}

// Converts the result of multiplication of two golden base numbers to proper Zeckendorf representation
vec<int64> coefficient_normalization(vec<int64> &target)
{
    target.resize(target.size());
    vec<int64> negative_coefficient(target.size() + 3, 0);
    vec<int64> positive_coefficient(target.size() + 3, 0);
    for (int64 index = 0; index < target.size(); index++)
    {
        if (target[index] > 0)
        {
            positive_coefficient[index] = target[index];
        }
        else if (target[index] < 0)
        {
            negative_coefficient[index] = -target[index];
        }
    }
    int64 delta = 0;
    for (int64 index = 0; index < positive_coefficient.size() - 1; index++)
    {
        if ((positive_coefficient[index + 0] > 0) and (positive_coefficient[index + 1] > 0))
        {
            delta = min(positive_coefficient[index + 0], positive_coefficient[index + 1]);
            positive_coefficient[index + 0] -= delta;
            positive_coefficient[index + 1] -= delta;
            positive_coefficient[index + 2] += delta;
        }
        if ((negative_coefficient[index + 0] > 0) and (negative_coefficient[index + 1] > 0))
        {
            delta = min(negative_coefficient[index + 0], negative_coefficient[index + 1]);
            negative_coefficient[index + 0] -= delta;
            negative_coefficient[index + 1] -= delta;
            negative_coefficient[index + 2] += delta;
        }
    }
    vec<int64> positive_result(target.size() + 3, 0);
    vec<int64> negative_result(target.size() + 3, 0);
    vec<int64> positive_indexth_bit(target.size() + 3, 0);
    vec<int64> negative_indexth_bit(target.size() + 3, 0);
    vec<int64> result;
    int64 positive_bit_size = ceil(log2(*max_element(positive_coefficient.begin(), positive_coefficient.end())));
    int64 negative_bit_size = ceil(log2(*max_element(negative_coefficient.begin(), negative_coefficient.end())));
    int64 bit_size = max(positive_bit_size, negative_bit_size) + 1;
    for (int64 index = bit_size; index >= 0; index--)
    {
        for (int64 index2 = 0; index2 < positive_coefficient.size(); index2++)
        {
            positive_indexth_bit[index2] = (positive_coefficient[index2] & (1 << index)) >> index;
            negative_indexth_bit[index2] = (negative_coefficient[index2] & (1 << index)) >> index;
        }
        positive_result = zeckendorf_addition(positive_result, positive_result);
        negative_result = zeckendorf_addition(negative_result, negative_result);
        positive_result = zeckendorf_addition(positive_result, positive_indexth_bit);
        negative_result = zeckendorf_addition(negative_result, negative_indexth_bit);
    }
    result = zeckendorf_subtraction(positive_result, negative_result);
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
    int64 test_cases;
    vec<int64> target1;
    vec<int64> target2;
    int64 target1_size, target2_size;
    int64 element;
    input >> test_cases;
    for (int64 index1 = 0; index1 < test_cases; index1++)
    {
        input >> target1_size;
        for (int64 target1_index = 0; target1_index < target1_size; target1_index++)
        {
            input >> element;
            target1.push_back(element);
        }
        input >> target2_size;
        for (int64 target2_index = 0; target2_index < target2_size; target2_index++)
        {
            input >> element;
            target2.push_back(element);
        }
        target1 = zeckendorf_to_lucas(target1);
        target2 = zeckendorf_to_lucas(target2);
        target1 = lucas_to_phinary(target1);
        target2 = lucas_to_phinary(target2);
        vec<int64> result = multiply_fft(target1, target2);
        vec<int64> result_sub = phinary_to_lucas(result);
        vec<int64> result_sub2 = lucas_to_zeckendorf(result_sub);
        vec<int64> result_sub3 = coefficient_normalization(result_sub2);
        remove_trailing_zero(result_sub3);
        if (result_sub3.size() == 0)
        {
            result_sub3.push_back(0);
        }
        print << result_sub3 << "\n";
        target1.clear();
        target2.clear();
    }
}