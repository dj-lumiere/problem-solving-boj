#include <iostream>
#include <stdint.h>
#include <complex>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <random>
#include <chrono>
#include <quadmath.h>
#include <type_traits>
#include <bit>
#include <bitset>
#include <numbers>
#include <regex>
#include <numeric>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

using int128 = __int128_t;
using int64 = int64_t;
using int32 = int32_t;
using int16 = int16_t;
using int8 = int8_t;
using uint128 = __uint128_t;
using uint64 = uint64_t;
using uint32 = uint32_t;
using uint16 = uint16_t;
using uint8 = uint8_t;
using float80 = long double;
using float64 = double;
using float32 = float;
using complex80 = complex<float80>;
using complex64 = complex<float64>;
using complex32 = complex<float32>;
using str = string;
using None = void;
template <typename T>
using vec = std::vector<T>;
template <typename T, typename U>
using dict = std::map<T, U>;
template <typename T>
using set = std::set<T>;
template <typename T>
using heap = std::priority_queue<T>;
#define print cout
#define input cin
#define append push_back
#define appendleft push_front
#define pop pop_back
#define popleft pop_front

class Fraction
{
private:
    int64_t numerator;
    int64_t denominator;

public:
    template <typename integers>
    Fraction(integers numerator = 0, integers denominator = 1);
    bool operator==(Fraction other);
    bool operator!=(Fraction other);
    bool operator>=(Fraction other);
    bool operator>(Fraction other);
    bool operator<=(Fraction other);
    bool operator<(Fraction other);
    Fraction operator+(Fraction other);
    Fraction operator-();
    Fraction operator-(Fraction other);
    Fraction operator*(Fraction other);
    Fraction multiplicative_inverse();
    Fraction operator/(Fraction other);
    Fraction &operator+=(Fraction other);
    Fraction &operator-=(Fraction other);
    Fraction &operator*=(Fraction other);
    Fraction &operator/=(Fraction other);
    int64_t retrieve_denominator() const;
    int64_t retrieve_numerator() const;
    explicit operator long double() const
    {
        return static_cast<long double>(numerator) / static_cast<long double>(denominator);
    }
    explicit operator double() const
    {
        return static_cast<double>(numerator) / static_cast<double>(denominator);
    }
    explicit operator float() const
    {
        return static_cast<float>(numerator) / static_cast<float>(denominator);
    }
    explicit operator int64_t() const
    {
        return static_cast<int64_t>(numerator) / static_cast<int64_t>(denominator);
    }
    explicit operator int32_t() const
    {
        return static_cast<int32_t>(numerator) / static_cast<int32_t>(denominator);
    }
    explicit Fraction(int32_t numerator) : numerator(numerator), denominator(1) {}
    explicit Fraction(int64_t numerator) : numerator(numerator), denominator(1) {}
    friend std::ostream &operator<<(std::ostream &os, const Fraction &fraction);

protected:
    void reduce()
    {
        if (this->denominator == 0)
        {
            throw "Invalid Denominator";
        }
        if (this->denominator < 0)
        {
            this->numerator *= -1;
            this->denominator *= -1;
        }
        int64_t normalize_number = gcd(this->numerator, this->denominator);
        this->numerator /= normalize_number;
        this->denominator /= normalize_number;
    }
    void reduce_denominator(Fraction &other)
    {
        int64_t normalize_number = lcm(this->denominator, other.denominator);
        this->numerator *= normalize_number / this->denominator;
        this->denominator = normalize_number;
        other.numerator *= normalize_number / other.denominator;
        other.denominator = normalize_number;
    }
};

template <typename integers>
Fraction::Fraction(integers numerator, integers denominator)
{
    this->numerator = numerator;
    this->denominator = denominator;
    reduce();
}

bool Fraction::operator==(Fraction other)
{
    return (this->numerator == other.numerator) and (this->denominator == other.denominator);
}

bool Fraction::operator!=(Fraction other)
{
    return not(*this == other);
}

bool Fraction::operator>=(Fraction other)
{
    return not(*this < other);
}

bool Fraction::operator>(Fraction other)
{
    return other < *this;
}

bool Fraction::operator<=(Fraction other)
{
    return not(other < *this);
}

bool Fraction::operator<(Fraction other)
{
    reduce_denominator(other);
    int64_t compare = this->numerator - other.numerator;
    reduce();
    other.reduce();
    return compare < 0;
}

Fraction Fraction::operator-()
{
    return Fraction(-(this->numerator), this->denominator);
}

Fraction Fraction::operator+(Fraction other)
{
    reduce_denominator(other);
    int64_t new_denominator = this->denominator;
    int64_t new_numerator = this->numerator + other.numerator;
    reduce();
    return Fraction(new_numerator, new_denominator);
}

Fraction Fraction::operator-(Fraction other)
{
    return *this + -other;
}

Fraction Fraction::operator*(Fraction other)
{
    int64_t new_denominator = this->denominator * other.denominator;
    int64_t new_numerator = this->numerator * other.numerator;
    return Fraction(new_numerator, new_denominator);
}

Fraction Fraction::multiplicative_inverse()
{
    if (this->numerator == 0)
    {
        throw "ZeroDivisionError";
    }
    return Fraction(this->denominator, this->numerator);
}

Fraction Fraction::operator/(Fraction other)
{
    if (other.numerator == 0)
    {
        throw "ZeroDivisionError";
    }
    int64_t new_denominator = this->denominator * other.numerator;
    int64_t new_numerator = this->numerator * other.denominator;
    return Fraction(new_numerator, new_denominator);
}

Fraction &Fraction::operator+=(Fraction other)
{
    *this = *this + other;
    return *this;
}

Fraction &Fraction::operator-=(Fraction other)
{
    *this = *this - other;
    return *this;
}

Fraction &Fraction::operator*=(Fraction other)
{
    *this = *this * other;
    return *this;
}

Fraction &Fraction::operator/=(Fraction other)
{
    *this = *this / other;
    return *this;
}

int64_t Fraction::retrieve_denominator() const
{
    return this->denominator;
}

int64_t Fraction::retrieve_numerator() const
{
    return this->numerator;
}

std::ostream &operator<<(std::ostream &os, const Fraction &fraction)
{
    os << fraction.retrieve_numerator() << "/" << fraction.retrieve_denominator();
    return os;
}

int32_t main(){
    int32_t a, b, c, d;
    input >> a >> b >> c >> d;
    Fraction fraction1(a,b);
    Fraction fraction2(c,d);
    Fraction fraction_sum = fraction1 + fraction2;
    print << fraction_sum.retrieve_numerator() << " " << fraction_sum.retrieve_denominator();
}