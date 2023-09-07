/* 1271 엄청난 부자2 */

#include <iostream>
#include <cstdint>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
const int32_t MOD = 998244353;
const int32_t ROOT = 3;
class BigInt
{
private:
    static const int32_t PLUS = 1;
    static const int32_t MINUS = -1;
    static const int32_t ZERO = 0;
    int32_t sign = 1;
    int32_t digit = 1;
    std::vector<int32_t> mantissa;

public:
    BigInt(const std::string &target);
    BigInt(const char *target);
    BigInt(int32_t sign, const std::vector<int32_t> &mantissa);
    BigInt(int32_t target);
    BigInt(int64_t target);
    bool operator==(const BigInt &other);
    bool operator!=(const BigInt &other);
    bool operator>=(const BigInt &other);
    bool operator>(const BigInt &other);
    bool operator<=(const BigInt &other);
    bool operator<(const BigInt &other);
    BigInt operator-() const;
    BigInt operator+(const BigInt &other);
    BigInt operator-(const BigInt &other);
    BigInt operator*(const BigInt &other);
    BigInt operator/(const BigInt &other);
    BigInt operator%(const BigInt &other);
    BigInt &operator+=(const BigInt &other);
    BigInt &operator-=(const BigInt &other);
    BigInt &operator*=(const BigInt &other);
    BigInt &operator/=(const BigInt &other);
    BigInt &operator%=(const BigInt &other);
    int32_t retrieve_sign() const;
    int32_t retrieve_digit() const;
    std::vector<int32_t> retrieve_mantissa() const;
    friend std::istream &operator>>(std::istream &is, BigInt &target);
    friend std::ostream &operator<<(std::ostream &os, const BigInt &target);
    friend BigInt abs(BigInt target);
    friend std::vector<BigInt> divmod(BigInt target1, BigInt target2);
    friend BigInt gcd(BigInt target1, BigInt target2);
    friend BigInt lcm(BigInt target1, BigInt target2);
    friend BigInt isqrt(BigInt target1);

protected:
    void remove_trailing_zero(std::vector<int32_t> &target);
    bool is_smaller_than_other(const BigInt &other);
    bool is_smaller_than_other_same_digit(const BigInt &other);
    BigInt add_mantissa(const BigInt &other);
    BigInt subtract_mantissa(const BigInt &other);
    BigInt multiply_mantissa(const BigInt &other);
    std::vector<BigInt> divmod_mantissa(const BigInt &other);
    std::vector<BigInt> divmod(const BigInt &other);
    int32_t multiply_mod(int32_t a, int32_t b);
    int32_t power_with_mod(int32_t base, int32_t index);
    int32_t modular_inverse(int32_t base);
    int32_t find_bit_ceil(int32_t a);
    void bit_reversal_permutation(std::vector<int32_t> &a);
    void coefficient_normalization(std::vector<int32_t> &a);
    void ntt(std::vector<int32_t> &a, bool invert);
};
void BigInt::remove_trailing_zero(std::vector<int32_t> &target)
{
    while (target.size() > 1 and target.back() == 0)
    {
        target.pop_back();
    }
}
bool BigInt::is_smaller_than_other(const BigInt &other)
{
    if (this->digit > other.digit)
    {
        return false;
    }
    else if (this->digit < other.digit)
    {
        return true;
    }
    return is_smaller_than_other_same_digit(other);
}
bool BigInt::is_smaller_than_other_same_digit(const BigInt &other)
{
    return std::lexicographical_compare(this->mantissa.rbegin(), this->mantissa.rend(),
                                        other.mantissa.rbegin(), other.mantissa.rend());
}
BigInt BigInt::add_mantissa(const BigInt &other)
{
    std::vector<int32_t> result;
    int32_t carry = 0;
    for (size_t i = 0; i < std::max(this->mantissa.size(), other.mantissa.size()); i++)
    {
        int32_t sum = carry;
        if (i < this->mantissa.size())
            sum += this->mantissa[i];
        if (i < other.mantissa.size())
            sum += other.mantissa[i];
        carry = sum / 10;
        result.push_back(sum % 10);
    }
    if (carry)
        result.push_back(carry);
    return BigInt(this->sign, result);
}
BigInt BigInt::subtract_mantissa(const BigInt &other)
{
    bool negate = false;
    int32_t sign = ZERO;
    if (is_smaller_than_other(other))
    {
        negate = true;
    }
    std::vector<int32_t> result;
    int32_t borrow = 0;
    for (size_t i = 0; i < std::max(this->mantissa.size(), other.mantissa.size()); i++)
    {
        int32_t diff = -borrow;
        if (negate and i < this->mantissa.size())
        {
            diff -= this->mantissa[i];
        }
        if (negate and i < other.mantissa.size())
        {
            diff += other.mantissa[i];
        }
        if (not negate and i < this->mantissa.size())
        {
            diff += this->mantissa[i];
        }
        if (not negate and i < other.mantissa.size())
        {
            diff -= other.mantissa[i];
        }
        if (diff < 0)
        {
            diff += 10;
            borrow = 1;
        }
        else
        {
            borrow = 0;
        }
        result.push_back(diff);
    }
    remove_trailing_zero(result);
    if (result.size() == 1 and result.back() == 0)
    {
        sign = ZERO;
    }
    else
    {
        sign = (negate ? MINUS : PLUS);
    }
    return BigInt(sign, result);
}
int32_t BigInt::multiply_mod(int32_t a, int32_t b)
{
    return static_cast<int32_t>((static_cast<int64_t>(a) * b) % MOD);
}
int32_t BigInt::power_with_mod(int32_t base, int32_t index)
{
    int32_t answer = 1;
    while (index)
    {
        if (index & 1)
        {
            answer = multiply_mod(answer, base);
        }
        base = multiply_mod(base, base);
        index >>= 1;
    }
    return answer;
}
int32_t BigInt::modular_inverse(int32_t base)
{
    return power_with_mod(base, MOD - 2);
}
int32_t BigInt::find_bit_ceil(int32_t a)
{
    return static_cast<int32_t>(ceil(log2(a)));
}
void BigInt::bit_reversal_permutation(std::vector<int32_t> &a)
{
    int32_t n = a.size();
    for (int32_t i = 1, j = 0; i < n; ++i)
    {
        int32_t bit = n >> 1;
        for (; j & bit; bit >>= 1)
        {
            j ^= bit;
        }
        j ^= bit;
        if (i < j)
        {
            std::swap(a[i], a[j]);
        }
    }
}
void BigInt::coefficient_normalization(std::vector<int32_t> &a)
{
    int32_t n = a.size();
    int32_t n_inv = modular_inverse(n);
    for (int32_t i = 0; i < n; ++i)
    {
        a[i] = multiply_mod(a[i], n_inv);
    }
}
void BigInt::ntt(std::vector<int32_t> &a, bool invert)
{
    int32_t n = a.size();
    bit_reversal_permutation(a);
    std::vector<int32_t> root_of_unity(n / 2, 0);
    int32_t angle;
    if (invert)
    {
        angle = MOD - 1 - (MOD - 1) / n;
    }
    else
    {
        angle = (MOD - 1) / n;
    }
    root_of_unity[0] = 1;
    int32_t angleth_power = power_with_mod(ROOT, angle);
    for (int32_t i = 1; i < n / 2; ++i)
    {
        root_of_unity[i] = multiply_mod(root_of_unity[i - 1], angleth_power);
    }
    for (int32_t len = 2; len <= n; len <<= 1)
    {
        int32_t step = n / len;
        for (int32_t i = 0; i < n; i += len)
        {
            for (int32_t j = 0; j < len / 2; j++)
            {
                int32_t u = a[i + j];
                int32_t v = multiply_mod(a[i + j + len / 2], root_of_unity[step * j]);
                if (u + v < MOD)
                {
                    a[i + j] = u + v;
                }
                else
                {
                    a[i + j] = u + v - MOD;
                }
                if (u - v >= 0)
                {
                    a[i + j + len / 2] = u - v;
                }
                else
                {
                    a[i + j + len / 2] = u - v + MOD;
                }
            }
        }
    }
    if (invert)
    {
        coefficient_normalization(a);
    }
}
BigInt BigInt::multiply_mantissa(const BigInt &other)
{
    int32_t original_size = this->mantissa.size() + other.mantissa.size() + 1;
    int32_t sign = PLUS;
    std::vector<int32_t> transformed_a1(this->mantissa.begin(), this->mantissa.end());
    std::vector<int32_t> transformed_b1(other.mantissa.begin(), other.mantissa.end());
    int32_t n = 1 << find_bit_ceil(original_size);
    transformed_a1.resize(n);
    transformed_b1.resize(n);
    ntt(transformed_a1, false);
    ntt(transformed_b1, false);
    for (int32_t i = 0; i < n; i++)
    {
        transformed_a1[i] = multiply_mod(transformed_a1[i], transformed_b1[i]);
    }
    ntt(transformed_a1, true);
    std::vector<int32_t> result(original_size);
    for (int32_t i = 0; i < original_size; i++)
    {
        result[i] = transformed_a1[i];
    }
    for (int32_t i = 0; i < original_size - 1; i++)
    {
        if (result[i] > 9)
        {
            result[i + 1] += result[i] / 10;
            result[i] %= 10;
        }
    }
    remove_trailing_zero(result);
    if (result.size() == 1 and result.back() == 0)
    {
        sign = ZERO;
    }
    return BigInt(sign, result);
}
std::vector<BigInt> BigInt::divmod_mantissa(const BigInt &other)
{
    if (other.sign == ZERO)
    {
        throw std::invalid_argument("DivisionError");
    }
    BigInt absolute_dividend = abs(other);
    std::vector<int32_t> quotient_mantissa;
    int32_t sign = PLUS;
    BigInt remainder(0);
    for (std::reverse_iterator rit = this->mantissa.rbegin(); rit != this->mantissa.rend(); ++rit)
    {
        remainder = remainder * 10 + *rit;
        int32_t digit = 0;
        while (remainder >= absolute_dividend and digit < 10)
        {
            remainder -= absolute_dividend;
            digit += 1;
        }
        remove_trailing_zero(remainder.mantissa);
        quotient_mantissa.push_back(digit);
    }
    std::reverse(quotient_mantissa.begin(), quotient_mantissa.end());
    remove_trailing_zero(quotient_mantissa);
    if (quotient_mantissa.size() == 1 and quotient_mantissa.back() == 0)
    {
        sign = ZERO;
    }
    return {BigInt(sign, quotient_mantissa), remainder};
}
std::vector<BigInt> BigInt::divmod(const BigInt &other)
{
    std::vector<BigInt> division_result = divmod_mantissa(other);
    if ((this->sign == MINUS) and other.sign == PLUS)
    {
        division_result[0] = -(division_result[1].sign == ZERO ? division_result[0] : division_result[0] + 1);
        division_result[1] = (division_result[1].sign == ZERO ? division_result[1] : -(division_result[1] - other));
    }
    else if ((this->sign >= ZERO) and other.sign == MINUS)
    {
        division_result[0] = -division_result[0];
    }
    else if ((this->sign == MINUS) and other.sign == MINUS)
    {
        division_result[0] = (division_result[1].sign == ZERO ? division_result[0] : division_result[0] + 1);
        division_result[1] = (division_result[1].sign == ZERO ? division_result[1] : -division_result[1] - other);
    }
    return division_result;
}
BigInt::BigInt(const std::string &target)
{
    this->mantissa.clear();
    for (std::reverse_iterator rit = target.rbegin(); rit != target.rend(); ++rit)
    {
        if (*rit == *target.begin() and *rit == '-')
        {
            sign = -1;
            continue;
        }
        if (not('0' <= *rit and *rit <= '9'))
        {
            throw std::invalid_argument("InvalidNumeralDigitError");
        }
        this->mantissa.push_back(static_cast<int32_t>(*rit - '0'));
    }
    remove_trailing_zero(this->mantissa);
    if (this->mantissa.size() == 1 and this->mantissa.back() == 0)
    {
        this->sign = ZERO;
    }
    this->digit = this->mantissa.size();
}
BigInt::BigInt(const char *target)
{
    this->mantissa.clear();
    auto p = target;
    while (*p != '\0')
    {
        if (p == target and *p == '-')
        {
            sign = -1;
            ++p;
            continue;
        }
        if (not('0' <= *p and *p <= '9'))
        {
            throw std::invalid_argument("InvalidNumeralDigitError");
        }
        this->mantissa.push_back(static_cast<int32_t>(*p - '0'));
        ++p;
    }
    reverse(this->mantissa.begin(), this->mantissa.end());
    remove_trailing_zero(this->mantissa);
    if (this->mantissa.size() == 1 and this->mantissa.back() == 0)
    {
        this->sign = ZERO;
    }
    this->digit = this->mantissa.size();
}
BigInt::BigInt(int32_t target)
{
    this->mantissa.clear();
    if (target < 0)
    {
        this->sign = MINUS;
        target = -target;
    }
    else if (target == 0)
    {
        this->sign = ZERO;
    }
    else
    {
        this->sign = PLUS;
    }
    while (target != 0)
    {
        this->mantissa.push_back(target % 10);
        target /= 10;
    }
    if (this->mantissa.empty())
    {
        this->mantissa.push_back(0);
    }
    this->digit = mantissa.size();
}
BigInt::BigInt(int64_t target)
{
    this->mantissa.clear();
    if (target < 0)
    {
        this->sign = MINUS;
        target = -target;
    }
    else if (target == 0)
    {
        this->sign = ZERO;
    }
    else
    {
        this->sign = PLUS;
    }
    while (target != 0)
    {
        this->mantissa.push_back(target % 10);
        target /= 10;
    }
    if (this->mantissa.empty())
    {
        this->mantissa.push_back(0);
    }
    this->digit = mantissa.size();
}
BigInt::BigInt(int32_t sign, const std::vector<int32_t> &mantissa)
{
    this->mantissa.clear();
    if (sign > 0)
    {
        sign = 1;
    }
    else if (sign < 0)
    {
        sign = -1;
    }
    this->sign = sign;
    this->mantissa = mantissa;
    remove_trailing_zero(this->mantissa);
    this->digit = mantissa.size();
}
bool BigInt::operator==(const BigInt &other)
{
    return this->sign == other.sign and this->mantissa == other.mantissa;
}
bool BigInt::operator!=(const BigInt &other)
{
    return not(*this == other);
}
bool BigInt::operator>=(const BigInt &other)
{
    return not(*this < other);
}
bool BigInt::operator>(const BigInt &other)
{
    return not(*this <= other);
}
bool BigInt::operator<=(const BigInt &other)
{
    return (*this < other) or (*this == other);
}
bool BigInt::operator<(const BigInt &other)
{
    if (*this == other)
    {
        return false;
    }
    if (this->sign < other.sign)
    {
        return true;
    }
    else if (this->sign > other.sign)
    {
        return false;
    }
    else if (this->sign == PLUS and other.sign == PLUS)
    {
        return is_smaller_than_other(other);
    }
    else if (this->sign == MINUS and other.sign == MINUS)
    {
        return not is_smaller_than_other(other);
    }
    return true;
}
BigInt abs(BigInt target)
{
    int32_t target_sign = target.retrieve_sign();
    if (target_sign == -1)
    {
        return -target;
    }
    return target;
}
BigInt BigInt::operator+(const BigInt &other)
{
    if (this->sign == ZERO)
    {
        return other;
    }
    if (other.sign == ZERO)
    {
        return *this;
    }
    if (this->sign == PLUS and other.sign == PLUS)
    {
        return add_mantissa(other);
    }
    if (this->sign == MINUS and other.sign == MINUS)
    {
        return -add_mantissa(other);
    }
    if (this->sign == PLUS and other.sign == MINUS)
    {
        return subtract_mantissa(-other);
    }
    if (this->sign == MINUS and other.sign == PLUS)
    {
        return -subtract_mantissa(-other);
    }
}
BigInt BigInt::operator-() const
{
    BigInt result = BigInt(-1 * this->sign, this->mantissa);
    return result;
}
BigInt BigInt::operator-(const BigInt &other)
{
    if (this->sign == ZERO)
    {
        return -other;
    }
    if (other.sign == ZERO)
    {
        return *this;
    }
    if (this->sign == PLUS and other.sign == PLUS)
    {
        return subtract_mantissa(other);
    }
    if (this->sign == MINUS and other.sign == MINUS)
    {
        return -subtract_mantissa(other);
    }
    if (this->sign == PLUS and other.sign == MINUS)
    {
        return add_mantissa(-other);
    }
    if (this->sign == MINUS and other.sign == PLUS)
    {
        return -add_mantissa(-other);
    }
}
BigInt BigInt::operator*(const BigInt &other)
{
    if (this->sign == ZERO or other.sign == ZERO)
    {
        return BigInt("0");
    }
    if ((this->sign == PLUS and other.sign == PLUS) or (this->sign == MINUS and other.sign == MINUS))
    {
        return multiply_mantissa(other);
    }
    if ((this->sign == PLUS and other.sign == MINUS) or (this->sign == MINUS and other.sign == PLUS))
    {
        return -multiply_mantissa(other);
    }
}
BigInt BigInt::operator/(const BigInt &other)
{
    return divmod(other)[0];
}
BigInt BigInt::operator%(const BigInt &other)
{
    return divmod(other)[1];
}
BigInt &BigInt::operator+=(const BigInt &other)
{
    *this = *this + other;
    return *this;
}
BigInt &BigInt::operator-=(const BigInt &other)
{
    *this = *this - other;
    return *this;
}
BigInt &BigInt::operator*=(const BigInt &other)
{
    *this = *this * other;
    return *this;
}
BigInt &BigInt::operator/=(const BigInt &other)
{
    *this = *this / other;
    return *this;
}
BigInt &BigInt::operator%=(const BigInt &other)
{
    *this = *this % other;
    return *this;
}
int32_t BigInt::retrieve_sign() const
{
    return this->sign;
}
int32_t BigInt::retrieve_digit() const
{
    return this->digit;
}
std::vector<int32_t> BigInt::retrieve_mantissa() const
{
    return this->mantissa;
}
std::istream &operator>>(std::istream &is, BigInt &target)
{
    std::string mantissa;
    if (is >> mantissa)
    {
        target = BigInt(mantissa);
    }
    return is;
}
std::ostream &operator<<(std::ostream &os, const BigInt &target)
{
    int64_t sign = target.retrieve_sign();
    const std::vector<int32_t> &mantissa = target.retrieve_mantissa();
    if (sign == -1)
    {
        os << '-';
    }
    for (auto it = mantissa.rbegin(); it != mantissa.rend(); ++it)
    {
        os << *it;
    }
    return os;
}
std::vector<BigInt> divmod(BigInt target1, BigInt target2)
{
    return target1.divmod(target2);
}
BigInt gcd(BigInt target1, BigInt target2)
{
    if (target1 < target2)
    {
        return gcd(target2, target1);
    }
    if (target1 % target2 == BigInt(0))
    {
        return target2;
    }
    return gcd(target2, target1 % target2);
}
BigInt lcm(BigInt target1, BigInt target2)
{
    return target1 * target2 / gcd(target1, target2);
}
BigInt isqrt(BigInt target1)
{
    if (target1.retrieve_sign() == -1)
    {
        throw std::invalid_argument("Cannot find root of negative integer");
    }
    if (target1.retrieve_sign() == 0)
    {
        return BigInt(0);
    }
    BigInt start = 0;
    BigInt end = target1 + 1;
    while (start + 1 < end)
    {
        BigInt mid = (start + end) / 2;
        if (mid * mid > target1)
        {
            end = mid;
        }
        else
        {
            start = mid;
        }
    }
    return start;
}

template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
    for (auto it = target.begin(); it != target.end(); ++it)
    {
        os << *it;
        if (std::next(it) != target.end())
        {
            os << "\n";
        }
    }
    return os;
}
void fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}
int32_t main()
{
    fastIO();
    BigInt a = 0, b = 0;
    std::cin >> a >> b;
    std::cout << divmod(a, b);
}