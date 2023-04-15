/* 17648 N! mod P (3) */

#include <iostream>
#include <algorithm>
#include <complex>
#include <random>

#define int128 __int128_t
#define int64 int64_t
#define int32 int32_t
#define uint128 __uint128_t
#define uint64 uint64_t
#define uint32 uint32_t
#define float128 __float128
#define float80 long double
#define float64 double
#define float32 float
#define complex128 std::complex<float128>
#define complex80 std::complex<float80>
#define complex64 std::complex<float64>
#define complex32 std::complex<float32>
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
#define pi (float80)3.14159265358979323846264338327950288419716939937510

None print_list(list<int64>& A) {
    print << "[";
    for (int64 i = 0; i < (int64)A.size(); i++) {
        if (i + 1 == (int64)A.size()) {
            print << A[i] << "]\n";
        }
        else {
            print << A[i] << ", ";
        }
    }
}

None fft(list<complex80>& a, bool invert)
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
    list<complex80> root_of_unity(n / 2);
    for (int64 i = 0; i < n / 2; i++) {
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
    if (invert) {
        for (int64 i = 0; i < n; i++) {
            a[i] /= n;
        }
    }
}

list<int64> multiply_fft(list<int64>& v, list<int64>& w, int64 mod)
{
    int64 n = 2;
    while (n < (int64)v.size() + (int64)w.size())
    {
        n <<= 1;
    }
    list<complex80> v_split(n), w_split(n), result_sub1(n), result_sub2(n);
    //리스트의 값을 반으로 쪼개 조금 더 효율적인 계산을 도모
    //17번째 자리를 기준으로 자름
    //v_split = v_front + i * v_rear
    for (int64 i = 0; i < (int64)v.size(); i++)
    {
        v_split[i] = complex80(v[i] >> 17, v[i] & 131071);
    }
    //w_split = w_front + i * w_rear
    for (int64 i = 0; i < w.size(); i++)
    {
        w_split[i] = complex80(w[i] >> 17, w[i] & 131071);
    }
    fft(v_split, 0);
    fft(w_split, 0);
    for (int64 i = 0; i < n; i++) {
        int64 j = 0;
        //i=0이면 j=0, i>0이면 j=n-i 왜냐면 (a+bi)w^{i}의 conjugate는 (a-bi)w^{-i}=(a-bi)w^{n-i}이기 때문.
        if (i) {
            j = n - i;
        }
        else {
            j = i;
        }
        complex80 new_v_front = (v_split[i] + std::conj(v_split[j])) * complex80(0.5, 0);
        complex80 new_v_rear = (v_split[i] - std::conj(v_split[j])) * complex80(0, -0.5);
        complex80 new_w_front = (w_split[i] + std::conj(w_split[j])) * complex80(0.5, 0);
        complex80 new_w_rear = (w_split[i] - std::conj(w_split[j])) * complex80(0, -0.5);
        result_sub1[i] = (new_v_front * new_w_front) + (new_v_front * new_w_rear) * complex80(0, 1);
        result_sub2[i] = (new_v_rear * new_w_front) + (new_v_rear * new_w_rear) * complex80(0, 1);
    }
    fft(result_sub1, 1);
    fft(result_sub2, 1);
    list<int64> result1(n);
    for (int64 i = 0; i < n; i++) {
        int128 result_high_digit = (int128)round(result_sub1[i].real());
        int128 result_mid_digit = (int128)round(result_sub1[i].imag()) + (int128)round(result_sub2[i].real());
        int128 result_low_digit = (int128)round(result_sub2[i].imag());
        result_high_digit %= mod;
        result_mid_digit %= mod;
        result_low_digit %= mod;
        result1[i] = (int64)(((result_high_digit << 34) + (result_mid_digit << 17) + result_low_digit) % mod);
        result1[i] = (result1[i] + mod) % mod;
    }
    return result1;
}

int64 multiply_mod(int64 a, int64 b, int64 P) {
    return (int64)((int128)a * b % P);
};

int64 power_with_mod(int64 base, int64 index, int64 mod) {
    int64 answer = 1;
    while (index) {
        if (index & 1) {
            answer = multiply_mod(answer, base, mod);
        }
        base = multiply_mod(base, base, mod);
        index >>= 1;
    }
    return answer;
}

int64 modular_inverse(int64 base, int64 mod) {
    return power_with_mod(base, mod - 2, mod);
}

list<int64> lagrange(list<int64>& h, int64 mod) {

    int64 dimension = (int64)h.size() - 1;
    list<int64> poly_a_values(2 * dimension + 1);

    /* h(x) = prod(j=0..dimension){(x-j)}*sum(i=0..dimension){fft(h(i)/(i!(dimension-i)!(-1)^(dimension-i)),1/(x-i))}*/
    list<int64> factorial(4 * dimension + 2);
    factorial[0] = 1;
    for (int64 i = 1; i <= 4 * dimension + 1; ++i) {
        factorial[i] = multiply_mod(factorial[i - 1], i, mod);
    }
    list<int64> inverse_factorial(4 * dimension + 2);
    inverse_factorial[4 * dimension + 1] = modular_inverse(factorial[4 * dimension + 1], mod);
    for (int64 i = 4 * dimension; i >= 0; i--) {
        inverse_factorial[i] = multiply_mod(inverse_factorial[i + 1], i + 1, mod) % mod;
    }
    /* part 1 : prod(j=0..dimension){(x-j)}*/
    list<int64> lagrange_sub1(4 * dimension + 2);
    for (int64 i = 0; i < 4 * dimension + 2; i++) {
        /* x! / (x-(d+1))! */
        if (i >= dimension + 1) {
            lagrange_sub1[i] = multiply_mod(factorial[i], inverse_factorial[i - (dimension + 1)], mod);
        }
    }

    /* part 2 : 1/(i!(dimension-i)!(-1)^(dimension-i))*/
    list<int64> lagrange_sub2(dimension + 1);
    for (int64 i = 0; i <= dimension; i++) {
        lagrange_sub2[i] = h[i];
        /* part 2-1 : 1/i! */
        lagrange_sub2[i] = multiply_mod(lagrange_sub2[i], inverse_factorial[i], mod);
        /* part 2-2 : 1/(dimension-i)! */
        lagrange_sub2[i] = multiply_mod(lagrange_sub2[i], inverse_factorial[dimension - i], mod);
        /* part 2-3 : 1/(-1)^(dimension-i) */
        if ((dimension - i) % 2 == 1) {
            lagrange_sub2[i] = mod - lagrange_sub2[i];
        }
        if (lagrange_sub2[i] == mod) {
            lagrange_sub2[i] = 0;
        }
    }

    /* part 3 : 1/(x-i)*/
    list<int64> inverse_number(4 * dimension + 2);
    inverse_number[0] = 0;
    for (int64 i = 1; i < 4 * dimension + 2; i++) {
        inverse_number[i] = multiply_mod(factorial[i - 1], inverse_factorial[i], mod);
    }

    /* part 4 : multiple_fft(part 2, part 3)*/
    list<int64> lagrange_sub4 = multiply_fft(lagrange_sub2, inverse_number, mod);

    /* part 5 : complete the h-value list*/
    list<int64> result(4 * dimension + 2);
    for (int64 i = 0; i <= dimension; i++) {
        result[i] = h[i];
    }
    for (int64 i = dimension + 1; i < 4 * dimension + 2; i++) {
        result[i] = multiply_mod(lagrange_sub4[i], lagrange_sub1[i], mod);
    }
    return result;
}

list<int64> polynomial_doubling(list<int64>& poly_a, int64 mod) {
    list<int64> polynomial_values = lagrange(poly_a, mod);
    list<int64> result2(polynomial_values.size() / 2);
    for (int64 i = 0; i < (int64)result2.size(); i++) {
        result2[i] = multiply_mod(polynomial_values[2 * i + 0], polynomial_values[2 * i + 1], mod);
    }
    return result2;
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
    int64 N, P;
    int64 d = 1;
    int64 answer = 1;
    list<int64> factorial_sub = { (int64)1, (int64)2 };
    input >> N >> P;
    while (N > d * (d + 1)) {
        factorial_sub = polynomial_doubling(factorial_sub, P);
        d <<= 1;
    }
    int64 bucket = N / d;
    for (int64 i = 0; i < bucket; i++) {
        answer = multiply_mod(answer, factorial_sub[i], P);
    }
    for (int64 i = bucket * d + 1; i <= N; i++) {
        answer = multiply_mod(answer, i, P);
    }
    print << answer;
}