#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdint>
#include <cassert>
#include <algorithm>
using namespace std;

void fastIO()
{
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
}

int32_t letter_to_number(char letter)
{
    if ('0' <= letter and letter <= '9')
    {
        return letter - '0';
    }
    if ('A' <= letter and letter <= 'Z')
    {
        return letter - 'A' + 10;
    }
    if ('a' <= letter and letter <= 'z')
    {
        return letter - 'a' + 36;
    }
    return -1;
}

char number_to_letter(int32_t number)
{
    if (0 <= number and number <= 9)
    {
        return number + '0';
    }
    if (10 <= number and number <= 35)
    {
        return number - 10 + 'A';
    }
    if (36 <= number and number <= 61)
    {
        return number - 36 + 'a';
    }
    return '!';
}

int32_t D(int32_t x, int32_t B)
{
    return (x % B + B) % B;
}

std::vector<int32_t> big_sub(std::vector<int32_t> &p1, std::vector<int32_t> &p2, int32_t B)
{
    std::vector<int32_t> result(p1.begin(), p1.end());
    for (int32_t i = 0; i < p2.size(); i++)
    {
        result[i] -= p2[i];
    }
    for (int32_t i = 0; i < p2.size() - 1; i++)
    {
        if (result[i] < 0)
        {
            result[i] += B;
            result[i + 1] -= 1;
        }
    }
    while (not result.empty() and result.back() == 0)
    {
        result.pop_back();
    }
    if (result.empty())
    {
        result.push_back(0);
    }
    return result;
}

std::vector<int32_t> big_three_sum(std::vector<int32_t> &p1, std::vector<int32_t> &p2, std::vector<int32_t> &p3, int32_t B)
{
    std::vector<int32_t> result(std::max(std::max(p1.size(), p2.size()), p3.size()) + 1, 0);
    for (int32_t i = 0; i < p1.size(); i++)
    {
        result[i] += p1[i];
    }
    for (int32_t i = 0; i < p2.size(); i++)
    {
        result[i] += p2[i];
    }
    for (int32_t i = 0; i < p3.size(); i++)
    {
        result[i] += p3[i];
    }
    for (int32_t i = 0; i < result.size() - 1; i++)
    {
        if (result[i] >= B)
        {
            result[i + 1] += result[i] / B;
            result[i] %= B;
        }
    }
    while (not result.empty() and result.back() == 0)
    {
        result.pop_back();
    }
    if (result.empty())
    {
        result.push_back(0);
    }
    return result;
}

int32_t determine_number_type_and_make_initial_configuration(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3, bool check_for_shorter_length = true)
{
    if (check_for_shorter_length and l < 7)
    {
        return 20;
    }
    int32_t z1 = 0;
    if ((not(0 <= K[l - 2] and K[l - 2] <= 2)) and (D(K[0] - K[l - 1] - K[l - 2] + 1, B) != 0))
    {
        z1 = D(K[0] - K[l - 1] - K[l - 2] + 1, B);
        p1.resize(l);
        p2.resize(l - 1);
        p3.resize(l - 2);
        p1[0] = p1[p1.size() - 1] = K[l - 1];
        p2[0] = p2[p2.size() - 1] = K[l - 2] - 1;
        p3[0] = p3[p3.size() - 1] = z1;
        return 1;
    }
    if ((not(0 <= K[l - 2] and K[l - 2] <= 2)) and (D(K[0] - K[l - 1] - K[l - 2] + 1, B) == 0))
    {
        p1.resize(l);
        p2.resize(l - 1);
        p3.resize(l - 2);
        p1[0] = p1[p1.size() - 1] = K[l - 1];
        p2[0] = p2[p2.size() - 1] = K[l - 2] - 2;
        p3[0] = p3[p3.size() - 1] = 1;
        return 2;
    }
    if (0 <= K[l - 2] and K[l - 2] <= 2 and K[l - 1] != 1 and (D(K[0] - K[l - 1] + 2, B) != 0))
    {
        z1 = D(K[0] - K[l - 1] + 2, B);
        p1.resize(l);
        p2.resize(l - 1);
        p3.resize(l - 2);
        p1[0] = p1[p1.size() - 1] = K[l - 1] - 1;
        p2[0] = p2[p2.size() - 1] = B - 1;
        p3[0] = p3[p3.size() - 1] = z1;
        return 3;
    }
    if (0 <= K[l - 2] and K[l - 2] <= 2 and K[l - 1] != 1 and (D(K[0] - K[l - 1] + 2, B) == 0))
    {
        p1.resize(l);
        p2.resize(l - 1);
        p3.resize(l - 2);
        p1[0] = p1[p1.size() - 1] = K[l - 1] - 1;
        p2[0] = p2[p2.size() - 1] = B - 2;
        p3[0] = p3[p3.size() - 1] = 1;
        return 4;
    }
    if (K[l - 1] == 1 and K[l - 2] == 0 and K[l - 3] <= 3 and D(K[0] - K[l - 3], B) != 0)
    {
        z1 = D(K[0] - K[l - 3], B);
        p1.resize(l - 1);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = B - 1;
        p2[0] = p2[p2.size() - 1] = K[l - 3] + 1;
        p3[0] = p3[p3.size() - 1] = z1;
        return 5;
    }
    if (K[l - 1] == 1 and K[l - 2] == 0 and K[l - 3] <= 2 and D(K[0] - K[l - 3], B) == 0)
    {
        p1.resize(l - 1);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = B - 1;
        p2[0] = p2[p2.size() - 1] = K[l - 3] + 2;
        p3[0] = p3[p3.size() - 1] = B - 1;
        return 6;
    }
    if (K[l - 1] == 1 and K[l - 2] <= 2 and K[l - 3] >= 4 and D(K[0] - K[l - 3], B) != 0)
    {
        z1 = D(K[0] - K[l - 3], B);
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2];
        p2[0] = p2[p2.size() - 1] = K[l - 3] - 1;
        p3[0] = p3[p3.size() - 1] = z1;
        return 11;
    }
    if (K[l - 1] == 1 and K[l - 2] <= 2 and K[l - 3] >= 3 and D(K[0] - K[l - 3], B) == 0)
    {
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2];
        p2[0] = p2[p2.size() - 1] = K[l - 3] - 2;
        p3[0] = p3[p3.size() - 1] = 1;
        return 12;
    }
    if (K[l - 1] == 1 and 1 <= K[l - 2] and K[l - 2] <= 2 and 0 <= K[l - 3] and K[l - 3] <= 1 and K[0] == 0)
    {
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2] - 1;
        p2[0] = p2[p2.size() - 1] = B - 2;
        p3[0] = p3[p3.size() - 1] = 1;
        return 13;
    }
    if (K[l - 1] == 1 and 1 <= K[l - 2] and K[l - 2] <= 2 and 2 <= K[l - 3] and K[l - 3] <= 3 and K[0] == 0)
    {
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2];
        p2[0] = p2[p2.size() - 1] = 1;
        p3[0] = p3[p3.size() - 1] = B - 2;
        return 14;
    }
    if (K[l - 1] == 1 and 1 <= K[l - 2] and K[l - 2] <= 2 and 0 <= K[l - 3] and K[l - 3] <= 2 and K[0] != 0)
    {
        z1 = K[0];
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2] - 1;
        p2[0] = p2[p2.size() - 1] = B - 1;
        p3[0] = p3[p3.size() - 1] = z1;
        return 15;
    }
    if (K[l - 1] == 1 and 1 <= K[l - 2] and K[l - 2] <= 2 and K[l - 3] == 3 and D(K[0] - 3, B) != 0)
    {
        z1 = D(K[0] - 3, B);
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        p1[0] = p1[p1.size() - 1] = 1;
        p1[1] = p1[p1.size() - 2] = K[l - 2];
        p2[0] = p2[p2.size() - 1] = 2;
        p3[0] = p3[p3.size() - 1] = z1;
        return 16;
    }
}

int32_t determine_algorithm_type(int32_t l, int32_t numberType, vector<int32_t> &K)
{
    int32_t algorithmType = 0;
    int32_t m = l >> 1;
    bool is_special = (K[m] == 0) or (K[m - 1] == 0);
    if (l < 7)
    {
        algorithmType = 6;
    }
    else if ((l % 2 == 1 and 1 <= numberType and numberType <= 4) or
             (l % 2 == 0 and 5 <= numberType and numberType <= 6))
    {
        algorithmType = 1;
    }
    else if ((l % 2 == 0 and 1 <= numberType and numberType <= 4) or
             (l % 2 == 1 and 5 <= numberType and numberType <= 6))
    {
        algorithmType = is_special ? 5 : 2;
    }
    else if (l % 2 == 1 and 11 <= numberType and numberType <= 16)
    {
        algorithmType = 3;
    }
    else if (l % 2 == 0 and 11 <= numberType and numberType <= 16)
    {
        algorithmType = is_special ? 5 : 4;
    }
    return algorithmType;
}

template <typename element>
std::ostream &operator<<(std::ostream &os, const std::vector<element> &target)
{
    for (auto it = target.begin(); it != target.end(); ++it)
    {
        os << number_to_letter(*it);
    }
    return os;
}

void algorithm1(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    int32_t m = l % 2 ? (l - 1) / 2 : (l - 2) / 2;
    vector<int32_t> x(m + 2, 0), y(m + 2, 0), z(m + 2, 0), c(m + 2, 0);
    for (int32_t i = 1; i <= m; ++i)
    {
        if (i == 1)
        {
            x[1] = p1[0];
            y[1] = p2[0];
            z[1] = p3[0];
            c[1] = (x[1] + y[1] + z[1]) / B;
        }
        else if (i == 2)
        {
            x[2] = z[1] < K[2 * m - 2] ? D(K[2 * m - 1] - y[1], B) : D(K[2 * m - 1] - y[1] - 1, B);
            y[2] = D(K[2 * m - 2] - z[1] - 1, B);
            z[2] = D(K[1] - x[2] - y[2] - c[1], B);
            c[2] = (x[2] + y[2] + z[2] + c[1] - K[1]) / B;
        }
        else
        {
            x[i] = z[i - 1] < K[2 * m - i] ? 1 : 0;
            y[i] = D(K[2 * m - i] - z[i - 1] - 1, B);
            z[i] = D(K[i - 1] - x[i] - y[i] - c[i - 1], B);
            c[i] = (x[i] + y[i] + z[i] + c[i - 1] - K[i - 1]) / B;
        }
    }
    // cout << x << " " << y << " " << z << " " << m << "\n";
    x[m + 1] = 0;
    for (int i = 1; i <= m; ++i)
    {
        p1[i - 1] = p1[p1.size() - i] = x[i];
        p2[i - 1] = p2[p2.size() - i] = y[i];
        p3[i - 1] = p3[p3.size() - i] = z[i];
    }
    p1[m] = x[m + 1];
    if (c[m] == 1)
    {
        // cout << "I.1" << "\n";
        //  No further action needed
    }
    else if (c[m] == 0)
    {
        // cout << "I.2" << "\n";
        p1[m] = 1;
    }
    else if (c[m] == 2 and z[m] == B - 1)
    {
        // cout << "I.3.i" << "\n";
        p1[m] = 1;
        p2[m] = p2[m - 1] = y[m] - 1;
        p3[m - 1] = 0;
    }
    else if (c[m] == 2 and z[m] != B - 1)
    {
        // cout << "I.3.ii" << "\n";
        p2[m] = p2[m - 1] = y[m] - 1;
        p3[m - 1] = z[m] + 1;
    }
}

void algorithm2(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    int32_t m = l % 2 ? (l - 1) / 2 : l / 2;
    vector<int32_t> x(m + 2, 0), y(m + 2, 0), z(m + 2, 0), c(m + 2, 0);
    for (int32_t i = 1; i < m; ++i)
    {
        if (i == 1)
        {
            x[1] = p1[0];
            y[1] = p2[0];
            z[1] = p3[0];
            c[1] = (x[1] + y[1] + z[1]) / B;
        }
        else if (i == 2)
        {
            x[2] = z[1] < K[2 * m - 3] ? D(K[2 * m - 2] - y[1], B) : D(K[2 * m - 2] - y[1] - 1, B);
            y[2] = D(K[2 * m - 3] - z[1] - 1, B);
            z[2] = D(K[1] - x[2] - y[2] - c[1], B);
            c[2] = (x[2] + y[2] + z[2] + c[1] - K[1]) / B;
        }
        else
        {
            x[i] = z[i - 1] < K[2 * m - i - 1] ? 1 : 0;
            y[i] = D(K[2 * m - i - 1] - z[i - 1] - 1, B);
            z[i] = D(K[i - 1] - x[i] - y[i] - c[i - 1], B);
            c[i] = (x[i] + y[i] + z[i] + c[i - 1] - K[i - 1]) / B;
        }
    }
    x[m] = 0;
    y[m] = D(K[m - 1] - z[m - 1] - c[m - 1], B);
    c[m] = (x[m] + y[m] + z[m - 1] + c[m - 1] - K[m - 1]) / B;
    // cout << x << " " << y << " " << z << " " << m << "\n";
    for (int32_t i = 1; i <= m; ++i)
    {
        p1[i - 1] = p1[p1.size() - i] = x[i];
        p2[i - 1] = p2[p2.size() - i] = y[i];
        if (i == m)
        {
            continue;
        }
        p3[i - 1] = p3[p3.size() - i] = z[i];
    }
    if (c[m] == 1)
    {
        // cout << "II.1" << "\n";
        //  No further action needed
    }
    else if (c[m] == 0)
    {
        // cout << "II.2" << "\n";
        if (y[m] != 0)
        {
            // cout << "II.2.i" << "\n";
            p1[m] = p1[m - 1] = 1;
            p2[m - 1] = y[m] - 1;
        }
        else if (y[m] == 0)
        {
            // cout << "II.2.ii" << "\n";
            if (y[m - 1] != 0)
            {
                // cout << "II.2.ii.a" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 2] = y[m - 1] - 1;
                p2[m - 1] = B - 2;
                p3[m - 1] = p3[m - 2] = z[m - 1] + 1;
            }
            else if (y[m - 1] == 0 and z[m - 1] != 0)
            {
                // cout << "II.2.ii.b" << "\n";
                p2[m] = p2[m - 1] = p2[m - 2] = 1;
                p3[m - 1] = p3[m - 2] = z[m - 1] - 1;
            }
            else if (y[m - 1] == 0 and z[m - 1] == 0)
            {
                // cout << "II.2.ii.c" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 1] - 1;
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 2] = B - 1;
                p2[m - 1] = B - 4;
                p3[m - 1] = p3[m - 2] = 2;
            }
        }
    }
    else if (c[m] == 2)
    {
        // cout << "II.3" << "\n";
        p1[m] = p1[m - 1] = 1;
        p2[m] = p2[m - 2] = y[m - 1] - 1;
        p2[m - 1] = B - 2;
        p3[m - 1] = p3[m - 2] = 0;
    }
}

void algorithm3(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    int32_t m = (l - 1) / 2;
    vector<int32_t> x(m + 2, 0), y(m + 2, 0), z(m + 2, 0), c(m + 2, 0);
    for (int32_t i = 1; i < m; ++i)
    {
        if (i == 1)
        {
            x[1] = p1[1];
            y[1] = p2[0];
            z[1] = p3[0];
            c[1] = (1 + y[1] + z[1]) / B;
        }
        else if (i == 2)
        {
            x[2] = z[1] < K[2 * m - 3] ? D(K[2 * m - 2] - y[1], B) : D(K[2 * m - 2] - y[1] - 1, B);
            y[2] = D(K[2 * m - 3] - z[1] - 1, B);
            z[2] = D(K[1] - x[1] - y[2] - c[1], B);
            c[2] = (x[1] + y[2] + z[2] + c[1] - K[1]) / B;
        }
        else
        {
            x[i] = z[i - 1] < K[2 * m - i - 1] ? 1 : 0;
            y[i] = D(K[2 * m - i - 1] - z[i - 1] - 1, B);
            z[i] = D(K[i - 1] - x[i - 1] - y[i] - c[i - 1], B);
            c[i] = (x[i - 1] + y[i] + z[i] + c[i - 1] - K[i - 1]) / B;
        }
    }
    x[m] = 0;
    y[m] = D(K[m - 1] - z[m - 1] - x[m - 1] - c[m - 1], B);
    c[m] = (x[m - 1] + y[m] + z[m - 1] + c[m - 1] - K[m - 1]) / B;
    // cout << x << " " << y << " " << z << " " << m << "\n";
    for (int32_t i = 1; i < m; ++i)
    {
        p1[i] = p1[p1.size() - i - 1] = x[i];
        p2[i - 1] = p2[p2.size() - i] = y[i];
        p3[i - 1] = p3[p3.size() - i] = z[i];
    }
    p1[m] = p1[p1.size() - m - 1] = x[m];
    p2[m - 1] = p2[p2.size() - m] = y[m];
    if (c[m] == 1)
    {
        // cout << "III.1" << "\n";
        //  No further action needed
    }
    else if (c[m] == 0)
    {
        // cout << "III.2" << "\n";
        p1[m] = 1;
    }
    else if (c[m] == 2)
    {
        if (y[m - 1] != 0 and z[m - 1] != B - 1)
        {
            // cout << "III.3.i" << "\n";
            p2[m] = p2[m - 2] = y[m - 1] - 1;
            p2[m - 1] = y[m] - 1;
            p3[m - 1] = p3[m - 2] = z[m - 1] + 1;
        }
        else if (y[m - 1] != 0 and z[m - 1] == B - 1)
        {
            // cout << "III.3.ii" << "\n";
            p1[m] = 1;
            p2[m] = p2[m - 2] = y[m - 1] - 1;
            p3[m - 1] = p3[m - 2] = 0;
        }
        else if (y[m - 1] == 0 and z[m - 1] != B - 1)
        {
            // cout << "III.3.iii" << "\n";
            p1[m + 1] = p1[m - 1] = x[m - 1] - 1;
            p2[m] = p2[m - 2] = B - 1;
            p2[m - 1] = y[m] - 1;
            p3[m - 1] = p3[m - 2] = z[m - 1] + 1;
        }
        else if (y[m - 1] == 0 and z[m - 1] == B - 1)
        {
            // cout << "III.3.iv" << "\n";
            p1[m + 1] = p1[m - 1] = x[m - 1] - 1;
            p1[m] = 1;
            p2[m] = p2[m - 2] = B - 1;
            p3[m - 1] = p3[m - 2] = 0;
        }
    }
}

void algorithm4(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    int m = l / 2;
    vector<int32_t> x(m + 2, 0), y(m + 2, 0), z(m + 2, 0), c(m + 2, 0);
    for (int32_t i = 1; i < m; ++i)
    {
        if (i == 1)
        {
            x[1] = p1[1];
            y[1] = p2[0];
            z[1] = p3[0];
            c[1] = (1 + y[1] + z[1]) / B;
        }
        else if (i == 2)
        {
            x[2] = z[1] < K[2 * m - 4] ? D(K[2 * m - 3] - y[1], B) : D(K[2 * m - 3] - y[1] - 1, B);
            y[2] = D(K[2 * m - 4] - z[1] - 1, B);
            z[2] = D(K[1] - x[1] - y[2] - c[1], B);
            c[2] = (x[1] + y[2] + z[2] + c[1] - K[1]) / B;
        }
        else if (i == m - 1)
        {
            x[i] = z[m - 2] < K[m - 1] ? 1 : 0;
            y[i] = D(K[m - 1] - z[m - 2] - 1, B);
            z[i] = D(K[m - 2] - x[m - 2] - y[m - 1] - c[m - 2], B);
            c[i] = (x[m - 2] + y[m - 1] + z[m - 1] + c[m - 2] - K[m - 2]) / B;
        }
        else
        {
            x[i] = z[i - 1] < K[2 * m - i - 2] ? 1 : 0;
            y[i] = D(K[2 * m - i - 2] - z[i - 1] - 1, B);
            z[i] = D(K[i - 1] - x[i - 1] - y[i] - c[i - 1], B);
            c[i] = (x[i - 1] + y[i] + z[i] + c[i - 1] - K[i - 1]) / B;
        }
    }
    // cout << x << " " << y << " " << z << " " << m << "\n";
    for (int32_t i = 1; i < m; ++i)
    {
        p1[i] = p1[p1.size() - i - 1] = x[i];
        p2[i - 1] = p2[p2.size() - i] = y[i];
        p3[i - 1] = p3[p3.size() - i] = z[i];
    }
    if (c[m - 1] + x[m - 1] == 1)
    {
        // cout << "IV.1" << "\n";
    }
    else if (x[m - 1] + c[m - 1] == 0 and y[m - 1] != B - 1)
    {
        // cout << "IV.2" << "\n";

        if (z[m - 1] != 0)
        {
            // cout << "IV.2.i" << "\n";
            p2[m - 1] = p2[m - 2] = y[m - 1] + 1;
            p3[m - 2] = z[m - 1] - 1;
        }
        else if (z[m - 1] == 0 and y[m - 2] != 0)
        {
            // cout << "IV.2.ii" << "\n";
            if (y[m - 1] != 1 and z[m - 2] != B - 1)
            {
                // cout << "IV.2.ii.a" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 1;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 1] != 1 and z[m - 2] == B - 1)
            {
                // cout << "IV.2.ii.b" << "\n";
                p1[m] = p1[m - 1] = 2;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = 0;
                p3[m - 2] = 3;
            }
            else if (y[m - 1] == 1)
            {
                // cout << "IV.2.ii.c" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = B - 1;
                p3[m - 1] = p3[m - 3] = 0;
                p3[m - 2] = 3;
            }
        }
        else if (z[m - 1] == 0 and y[m - 2] == 0)
        {
            // cout << "IV.2.iii" << "\n";
            if (z[m - 2] != B - 1)
            {
                // cout << "IV.2.iii.a" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 1;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
            else if (z[m - 2] == B - 1 and y[m - 1] != 1)
            {
                // cout << "IV.2.iii.b" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 2;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = 0;
                p3[m - 2] = 3;
            }
            else if (z[m - 2] == B - 1 and y[m - 1] == 1)
            {
                // cout << "IV.2.iii.c" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = B - 1;
                p3[m - 1] = p3[m - 3] = 0;
                p3[m - 2] = 3;
            }
        }
    }
    else if (x[m - 1] + c[m - 1] == 0 and y[m - 1] == B - 1)
    {
        // cout << "IV.3" << "\n";
        p1[m] = p1[m - 1] = 1;
        p2[m] = p2[m - 3] = y[m - 2] - 1;
        p2[m - 1] = p2[m - 2] = B - 2;
        p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
        p3[m - 2] = 1;
    }
    else if (x[m - 1] + c[m - 1] == 2 and x[m - 1] == 0 and c[m - 1] == 2)
    {
        // cout << "IV.4" << "\n";
        if (z[m - 1] != B - 1)
        {
            // cout << "IV.4.i" << "\n";
            p2[m - 1] = p2[m - 2] = y[m - 1] - 1;
            p3[m - 2] = z[m - 1] + 1;
        }
        else if (z[m - 1] == B - 1 and z[m - 2] != B - 1)
        {
            // cout << "IV.4.ii" << "\n";
            if (y[m - 2] != 0)
            {
                // cout << "IV.4.ii.a" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 2] == 0)
            {
                // cout << "IV.4.ii.b" << "\n";
                p1[m] = p1[m - 1] = 1;
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
        }
        else if (z[m - 1] == B - 1 and z[m - 2] == B - 1)
        {
            // cout << "IV.4.iii" << "\n";
            if (not(B - 2 <= y[m - 1] and y[m - 1] <= B - 1))
            {
                // cout << "IV.4.iii.a" << "\n";
                if (y[m - 2] != B - 1)
                {
                    // cout << "IV.4.iii.a.1" << "\n";
                    p1[m] = p1[m - 1] = B - 2;
                    p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                    p2[m] = p2[m - 3] = y[m - 2] + 1;
                    p2[m - 1] = p2[m - 2] = y[m - 1] + 2;
                    p3[m - 1] = p3[m - 3] = B - 2;
                    p3[m - 2] = B - 2;
                }
                else if (y[m - 2] == B - 1)
                {
                    // cout << "IV.4.iii.a.2" << "\n";
                    p1[m] = p1[m - 1] = B - 2;
                    p2[m] = p2[m - 3] = 0;
                    p2[m - 1] = p2[m - 2] = y[m - 1] + 2;
                    p3[m - 1] = p3[m - 3] = B - 2;
                    p3[m - 2] = B - 2;
                }
            }
            else if (B - 2 <= y[m - 1] <= B - 1)
            {
                // cout << "IV.4.iii.b" << "\n";
                if (y[m - 2] >= 1)
                {
                    // cout << "IV.4.iii.b.1" << "\n";
                    p1[m] = p1[m - 1] = 2;
                    p1[m + 1] = p1[m - 2] = x[m - 2];
                    p2[m] = p2[m - 3] = y[m - 2] - 1;
                    p2[m - 1] = p2[m - 2] = y[m - 1] - 3;
                    p3[m - 1] = p3[m - 3] = 0;
                    p3[m - 2] = 3;
                }
                else if (y[m - 2] == 0 and x[m - 2] >= 1)
                {
                    // cout << "IV.4.iii.b.2" << "\n";
                    p1[m] = p1[m - 1] = 2;
                    p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                    p2[m] = p2[m - 3] = B - 1;
                    p2[m - 1] = p2[m - 2] = y[m - 1] - 3;
                    p3[m - 1] = p3[m - 3] = 0;
                    p3[m - 2] = 3;
                }
            }
        }
    }
    else if (x[m - 1] + c[m - 1] == 2 and x[m - 1] == 1 and c[m - 1] == 1)
    {
        // cout << "IV.5" << "\n";
        if (z[m - 1] != B - 1 and y[m - 1] != 0)
        {
            // cout << "IV.5.i" << "\n";
            p2[m - 1] = p2[m - 2] = y[m - 1] - 1;
            p3[m - 2] = z[m - 1] + 1;
        }
        else if (z[m - 1] != B - 1 and y[m - 1] == 0)
        {
            // cout << "IV.5.ii" << "\n";
            p1[m] = p1[m - 1] = 0;
            p2[m - 1] = p2[m - 2] = B - 1;
            p3[m - 2] = z[m - 1] + 1;
        }
        else if (z[m - 1] == B - 1 and z[m - 2] != 0)
        {
            // cout << "IV.5.iii" << "\n";
            if (y[m - 2] != B - 1)
            {
                // cout << "IV.5.iii.a" << "\n";
                p1[m] = p1[m - 1] = 0;
                p2[m] = p2[m - 3] = y[m - 2] + 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] + 1;
                p3[m - 1] = p3[m - 3] = z[m - 2] - 1;
                p3[m - 2] = B - 2;
            }
            else if (y[m - 2] == B - 1 and not(0 <= y[m - 1] and y[m - 1] <= 1))
            {
                // cout << "IV.5.iii.b" << "\n";
                p1[m] = p1[m - 1] = 2;
                p2[m] = p2[m - 3] = B - 2;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 2] == B - 1 and y[m - 1] == 0)
            {
                // cout << "IV.5.iii.c" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 2;
                p2[m - 1] = p2[m - 2] = B - 2;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 2] == B - 1 and y[m - 1] == 1)
            {
                // cout << "IV.5.iii.d" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 2;
                p2[m - 1] = p2[m - 2] = B - 1;
                p3[m - 1] = p3[m - 3] = z[m - 2] + 1;
                p3[m - 2] = 1;
            }
        }
        else if (z[m - 1] == B - 1 and z[m - 2] == 0 and y[m - 2] != 0)
        {
            // cout << "IV.5.iv" << "\n";
            if (not(0 <= y[m - 1] and y[m - 1] <= 1))
            {
                // cout << "IV.5.iv.a" << "\n";
                p1[m] = p1[m - 1] = 2;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 1] == 0)
            {
                // cout << "IV.5.iv.b" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = B - 2;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 1] == 1)
            {
                // cout << "IV.5.iv.c" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = y[m - 2] - 1;
                p2[m - 1] = p2[m - 2] = B - 1;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
        }
        else if (z[m - 1] == B - 1 and z[m - 2] == 0 and y[m - 2] == 0)
        {
            // cout << "IV.5.v" << "\n";
            if (not(0 <= y[m - 1] and y[m - 1] <= 1))
            {
                // cout << "IV.5.v.a" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 2;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = y[m - 1] - 2;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 1] == 0)
            {
                // cout << "IV.5.v.b" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = B - 2;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
            else if (y[m - 1] == 1)
            {
                // cout << "IV.5.v.c" << "\n";
                p1[m + 1] = p1[m - 2] = x[m - 2] - 1;
                p1[m] = p1[m - 1] = 1;
                p2[m] = p2[m - 3] = B - 1;
                p2[m - 1] = p2[m - 2] = B - 1;
                p3[m - 1] = p3[m - 3] = 1;
                p3[m - 2] = 1;
            }
        }
    }
    else if (x[m - 1] + c[m - 1] == 3)
    {
        // cout << "IV.6" << "\n";
        p2[m - 1] = p2[m - 2] = y[m - 1] - 1;
        p3[m - 2] = 0;
    }
}

void algorithm61(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    p1.resize(1);
    p2.resize(1);
    p3.resize(1);
    p1[0] = K[0];
    p2[0] = 0;
    p3[0] = 0;
}

void algorithm62(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (K[1] >= 1 and K[1] <= K[0])
    {
        p1 = {K[1], K[1]};
        p2 = {K[0] - K[1]};
        p3 = {0};
    }
    else if (K[1] > K[0] + 1)
    {
        p1 = {K[1] - 1, K[1] - 1};
        p2 = {B + K[0] - (K[1] - 1)};
        p3 = {0};
    }
    else if (K[0] >= 1 and K[1] == K[0] + 1)
    {
        p1 = {K[0], K[0]};
        p2 = {B - 1};
        p3 = {1};
    }
    else if (K[0] == 0 and K[1] == 1)
    {
        p1 = {B - 1};
        p2 = {1};
        p3 = {0};
    }
}

void algorithm63(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (K[2] <= K[0])
    {
        p1 = {K[2], K[1], K[2]};
        p2 = {K[0] - K[2]};
        p3 = {0};
    }
    else if (K[2] >= K[0] + 1 and K[1] != 0)
    {
        p1 = {K[2], K[1] - 1, K[2]};
        p2 = {B + K[0] - K[2]};
        p3 = {0};
    }
    else if (K[2] >= K[0] + 1 and K[1] == 0 and D(K[2] - K[0] - 1, B) != 0)
    {
        p1 = {K[2] - 1, B - 1, K[2] - 1};
        p2 = {B + K[0] - K[2] + 1};
        p3 = {0};
    }
    else if (K[2] >= K[0] + 1 and K[1] == 0 and D(K[2] - K[0] - 1, B) == 0)
    {
        if (K[2] >= 3)
        {
            p1 = {K[2] - 2, B - 1, K[2] - 2};
            p2 = {1, 1, 1};
            p3 = {0};
        }
        else if (K[2] == 2)
        {
            p1 = {1, 0, 1};
            p2 = {B - 1, B - 1};
            p3 = {1};
        }
        else if (K[2] == 1)
        {
            p1 = {B - 1, B - 1};
            p2 = {1};
            p3 = {0};
        }
    }
}

void algorithm64(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    vector<int32_t> p4;
    vector<int32_t> K_rev(K.rbegin(), K.rend());
    vector<int32_t> compare = {K[3], 0, 0, K[3]};
    if (K[0] == 0 and K[1] == 0 and K[2] == 0 and K[3] == 1)
    {
        // cout << "v\n";
        p1 = {B - 1, B - 1, B - 1};
        p2 = {1};
        p3 = {0};
    }
    else if (K_rev >= compare)
    {
        vector<int32_t> K2 = big_sub(K, compare, B);
        if (K2.size() == 3 and K2[0] == 1 and K2[1] == 0 and K2[2] == 2)
        {
            // cout << "ii\n";
            if (K[3] != 1 and K[3] != B - 1)
            {
                // cout << "ii.a\n";
                p1 = {K[3] - 1, B - 1, B - 1, K[3] - 1};
                p2 = {2, 1, 2};
                p3 = {0};
            }
            else if (K[3] == 1)
            {
                // cout << "ii.b\n";
                p1 = {1, 1, 1, 1};
                p2 = {B - 2, B - 2};
                p3 = {3};
            }
            else if (K[3] == B - 1)
            {
                // cout << "ii.c\n";
                p1 = {B - 1, 1, 1, B - 1};
                p2 = {B - 2, B - 2};
                p3 = {3};
            }
        }
        else if (K2.size() == 2 and K2[0] >= 1 and K2[0] + 1 == K2[1])
        {
            // cout << "iii\n";
            int32_t i = K2[0];
            if (K[3] + i == K[0])
            {
                // cout << "iii.a\n";
                if (K[3] != 1)
                {
                    // cout << "iii.a.1\n";
                    p1 = {K[3] - 1, B - 2, B - 2, K[3] - 1};
                    p2 = {1, 3, 1};
                    p3 = {i, i};
                }
                else if (K[3] == 1)
                {
                    // cout << "iii.a.2\n";
                    p1 = {B - 1, B - 1, B - 1};
                    p2 = {i + 1, i + 1};
                    p3 = {1};
                }
            }
            else if (K[3] + i == B + K[0])
            {
                // cout << "iii.b\n";
                p1 = {K[3] - 1, B - 2, B - 2, K[3] - 1};
                p2 = {1, 3, 1};
                p3 = {i, i};
            }
        }
        else if (K2.size() == 1)
        {
            // cout << "i\n";
            p1 = compare;
            p2 = K2;
            p3 = {0};
        }
        else if (K2.size() == 2)
        {
            // cout << "i\n";
            p1 = compare;
            algorithm62(K2, B, 2, p2, p3, p4);
        }
        else if (K2.size() == 3)
        {
            // cout << "i\n";
            p1 = compare;
            algorithm63(K2, B, 3, p2, p3, p4);
        }
    }
    else if (K[1] == 0 and K[2] == 0 and K[0] < K[3] and K[3] != 1)
    {
        // cout << "iv\n";
        p1 = {K[3] - 1, B - 1, B - 1, K[3] - 1};
        p2 = {B + K[0] - K[3]};
        p3 = {1};
    }
}

void algorithm65(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (K[4] != 1)
    {
        // cout << "x\n";
        determine_number_type_and_make_initial_configuration(K, B, l, p1, p2, p3, false);
        algorithm1(K, B, l, p1, p2, p3);
    }
    else if (K[4] == 1)
    {
        vector<int32_t> compare = {1, K[3], 0, K[3], 1};
        vector<int32_t> K_rev(K.rbegin(), K.rend());
        vector<int32_t> p4;
        if (K_rev >= compare)
        {
            vector<int32_t> K2 = big_sub(K, compare, B);
            // cout << K2 << "\n";
            if (K2.size() == 3 and K2[0] == 1 and K2[1] == 0 and K2[2] == 2)
            {
                // cout << "ii\n";
                p1 = {1, K[3], 1, K[3], 1};
                p2 = {1, 0, 1};
                p3 = {0};
            }
            else if (K2.size() == 2 and K2[0] + 1 == K2[1] and K[3] != 0)
            {
                // cout << "iii\n";
                int32_t d = K2[0];
                if (d + 1 + K[3] <= B - 1)
                {
                    // cout << "iii.a\n";
                    p1 = {1, K[3] - 1, 1, K[3] - 1, 1};
                    p2 = {B - 1, d + 1, B - 1};
                    p3 = {d + 1};
                }
                else if (d + 1 + K[3] == B + K[1])
                {
                    // cout << "iii.b\n";
                    p1 = {1, K[3] - 1, 1, K[3] - 1, 1};
                    p2 = {B - 1, d + 1, B - 1};
                    p3 = {d + 1};
                }
            }
            else if (K2.size() == 2 and K2[0] + 1 == K2[1] and K[3] == 0)
            {
                // cout << "iv\n";
                int32_t d = K2[0];
                p1 = {B - 1, B - 1, B - 1, B - 1};
                p2 = {d + 1, d + 1};
                p3 = {1};
            }
            else
            {
                p1 = compare;
                if (K2.size() == 1)
                {
                    // cout << "i\n";
                    algorithm61(K2, B, 1, p2, p3, p4);
                }
                else if (K2.size() == 2)
                {
                    // cout << "i\n";
                    algorithm62(K2, B, 2, p2, p3, p4);
                }
                else if (K2.size() == 3)
                {
                    // cout << "i\n";
                    algorithm63(K2, B, 3, p2, p3, p4);
                }
            }
        }
        else if (K[3] == 0)
        {
            // cout << "v\n";
            p1 = {B - 1, B - 1, B - 1, B - 1};
            p2 = {1};
            p3 = {0};
        }
        else if (K[3] != 0)
        {
            compare = {1, K[3] - 1, B - 1, K[3] - 1, 1};
            vector<int32_t> K2 = big_sub(K, compare, B);
            if (K2.size() == 2 and K2[0] + 1 == K2[1])
            {
                // cout << "vii\n";
                int32_t d = K2[0];
                p1 = {1, K[3] - 1, B - 2, K[3] - 1, 1};
                p2 = {1, d + 1, 1};
                p3 = {d - 1};
            }
            else
            {
                p1 = compare;
                if (K2.size() == 1)
                {
                    // cout << "vi\n";
                    algorithm61(K2, B, 1, p2, p3, p4);
                }
                else if (K2.size() == 2)
                {
                    // cout << "vi\n";
                    algorithm62(K2, B, 2, p2, p3, p4);
                }
                else if (K2.size() == 3)
                {
                    // cout << "vi\n";
                    algorithm63(K2, B, 3, p2, p3, p4);
                }
            }
        }
    }
}

void algorithm66(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (K[5] != 1)
    {
        determine_number_type_and_make_initial_configuration(K, B, l, p1, p2, p3, false);
        // cout << p1 << " " << p2 << " " << p3 << "\n";
        int32_t m = 3;
        vector<int32_t> x(m + 2, 0), y(m + 2, 0), z(m + 2, 0), c(m + 2, 0);
        for (int32_t i = 1; i < m; ++i)
        {
            if (i == 1)
            {
                x[1] = p1[0];
                y[1] = p2[0];
                z[1] = p3[0];
                c[1] = (x[1] + y[1] + z[1]) / B;
            }
            else if (i == 2)
            {
                x[2] = z[1] < K[2 * m - 3] ? D(K[2 * m - 2] - y[1], B) : D(K[2 * m - 2] - y[1] - 1, B);
                y[2] = D(K[2 * m - 3] - z[1] - 1, B);
                z[2] = D(K[1] - x[2] - y[2] - c[1], B);
                c[2] = (x[2] + y[2] + z[2] + c[1] - K[1]) / B;
            }
            else
            {
                x[i] = z[i - 1] < K[2 * m - i - 1] ? 1 : 0;
                y[i] = D(K[2 * m - i - 1] - z[i - 1] - 1, B);
                z[i] = D(K[i - 1] - x[i] - y[i] - c[i - 1], B);
                c[i] = (x[i] + y[i] + z[i] + c[i - 1] - K[i - 1]) / B;
            }
        }
        x[m] = 0;
        y[m] = D(K[m - 1] - z[m - 1] - c[m - 1], B);
        c[m] = (x[m] + y[m] + z[m - 1] + c[m - 1] - K[m - 1]) / B;
        // cout << x << " " << y << " " << z << " " << m << "\n";
        for (int32_t i = 1; i <= m; ++i)
        {
            p1[i - 1] = p1[p1.size() - i] = x[i];
            p2[i - 1] = p2[p2.size() - i] = y[i];
            if (i == m)
            {
                continue;
            }
            p3[i - 1] = p3[p3.size() - i] = z[i];
        }
        if (c[m] == 1)
        {
            // cout << "II.1" << "\n";
            // No further action needed
        }
        else if (c[m] == 0)
        {
            // cout << "II.2" << "\n";
            if (y[m] != 0)
            {
                // cout << "II.2.i" << "\n";
                p1[m] = p1[m - 1] = 1;
                p2[m - 1] = y[m] - 1;
            }
            else if (y[m] == 0)
            {
                // cout << "II.2.ii" << "\n";
                if (y[m - 1] != 0)
                {
                    // cout << "II.2.ii.a" << "\n";
                    p1[m] = p1[m - 1] = 1;
                    p2[m] = p2[m - 2] = y[m - 1] - 1;
                    p2[m - 1] = B - 2;
                    p3[m - 1] = p3[m - 2] = z[m - 1] + 1;
                }
                else if (y[m - 1] == 0 and z[m - 1] != 0)
                {
                    // cout << "II.2.ii.b" << "\n";
                    p2[m] = p2[m - 1] = p2[m - 2] = 1;
                    p3[m - 1] = p3[m - 2] = z[m - 1] - 1;
                }
                else if (y[m - 1] == 0 and z[m - 1] == 0)
                {
                    // cout << "II.2.ii.c" << "\n";
                    if (x[2] != 0)
                    {
                        // cout << "II.2.ii.c.1" << "\n";
                        p1 = {p1[5], p1[4] - 1, B - 1, B - 1, p1[1] - 1, p1[0]};
                        p2 = {p2[4], 1, 1, 1, p2[0]};
                    }
                    else if (x[2] == 0)
                    {
                        // cout << "II.2.ii.c.2" << "\n";
                        if (x[1] == 1)
                        {
                            // cout << "II.2.ii.c.2.i" << "\n";
                            p1 = {2, 0, 0, 0, 0, 2};
                            p2 = {1, 1};
                            p3 = {B - 4};
                        }
                        else if (x[1] != 1 and y[1] != B-1)
                        {
                            // cout << "II.2.ii.c.2.ii" << "\n";
                                p1 = {p1[5] - 1, B - 1, 0, 0, B - 1, p1[5] - 1};
                                p2 = {p2[4] + 1, 0, B - 2, 0, p2[0] + 1};
                                p3 = {p3[3], 1, 1, p3[0]};
                        } else if (x[1] != B-1 and y[1] == B-1 and z[1] == B-1){
                            // cout << "II.2.ii.c.2.iii" << "\n";
                                p1 = {p1[5] + 1, 0, 0, 0, 0, p1[0] + 1};
                                p2 = {1, 1};
                                p3 = {B - 4};
                        }
                    }
                    else
                    {
                        // cout << "II.2.ii.c.2\n";
                        p1[m + 1] = p1[m - 2] = x[m - 1] - 1;
                        p1[m] = p1[m - 1] = 1;
                        p2[m] = p2[m - 2] = B - 1;
                        p2[m - 1] = B - 4;
                        p3[m - 1] = p3[m - 2] = 2;
                    }
                }
            }
        }
        else if (c[m] == 2)
        {
            // cout << "II.3" << "\n";
            p1[m] = p1[m - 1] = 1;
            p2[m] = p2[m - 2] = y[m - 1] - 1;
            p2[m - 1] = B - 2;
            p3[m - 1] = p3[m - 2] = 0;
        }
    }
    else if (K[5] == 1)
    {
        int32_t z1 = D(K[0] - K[4] + 1, B);
        int32_t compare = D(K[0] - K[4] + 2, B);
        if (D(K[0] - K[4] + 1, B) != 0 and compare != 0)
        {
            // cout << "i\n";
            int32_t x1 = (B + K[4] - 1) >> 1;
            int32_t y1 = (B + K[4] - 1) - x1;
            int32_t x2 = (B + K[3] - 1) >> 1;
            int32_t y2 = (B + K[3] - 1) - x2;
            int32_t c1 = (x1 + y1 + z1 - K[0]) / B;
            int32_t z2 = D(K[1] - x2 - y2 - c1, B);
            int32_t c2 = (x2 + y2 + z2 + c1 - K[1]) / B;
            int32_t x3 = (B + K[2] - c2 - z1) >> 1;
            int32_t y3 = (B + K[2] - c2 - z1) - x3;
            p1 = {x1, x2, x3, x2, x1};
            p2 = {y1, y2, y3, y2, y1};
            p3 = {z1, z2, z1};
        }
        else if (compare == 0 and K[2] != 0)
        {
            // cout << "ii\n";
            int32_t x1 = (B + K[4] - 1) >> 1;
            int32_t y1 = (B + K[4] - 1) - x1;
            z1 = B - 1;
            int32_t x2 = (B + K[3] - 1) >> 1;
            int32_t y2 = (B + K[3] - 1) - x2;
            int32_t c1 = (x1 + y1 + z1 - K[0]) / B;
            int32_t z2 = D(K[1] - x2 - y2 - c1, B);
            int32_t c2 = (x2 + y2 + z2 + c1 - K[1]) / B;
            int32_t x3 = (B + K[2] - c2 - z1) >> 1;
            int32_t y3 = (B + K[2] - c2 - z1) - x3;
            p1 = {x1, x2, x3, x2, x1};
            p2 = {y1, y2, y3, y2, y1};
            p3 = {z1, z2, z1};
        }
        else if (compare == 0 and K[2] == 0)
        {
            // cout << "iii\n";
            if (K[4] == 0)
            {
                // cout << "iii.a\n";
                int32_t x1 = B - 2;
                int32_t y1 = 1;
                z1 = B - 1;
                int32_t x2 = (K[3]) >> 1;
                int32_t y2 = (K[3]) - x2;
                int32_t z2 = D(K[1] - x2 - y2 - 1, B);
                int32_t c2 = (x2 + y2 + z2 + 1 - K[1]) / B;
                int32_t x3 = (B - c2 - z2) >> 1;
                int32_t y3 = (B - c2 - z2) - x3;
                p1 = {x1, x2, x3, x2, x1};
                p2 = {y1, y2, y3, y2, y1};
                p3 = {z1, z2, z2, z1};
            }
            else if (K[4] == 1)
            {
                // cout << "iii.b\n";
                int32_t x1 = B - 1;
                int32_t y1 = 1;
                z1 = B - 1;
                int32_t x2 = (K[3]) >> 1;
                int32_t y2 = (K[3]) - x2;
                int32_t z2 = D(K[1] - x2 - y2 - 1, B);
                int32_t c2 = (x2 + y2 + z2 + 1 - K[1]) / B;
                int32_t x3 = (B - c2 - z2) >> 1;
                int32_t y3 = (B - c2 - z2) - x3;
                p1 = {x1, x2, x3, x2, x1};
                p2 = {y1, y2, y3, y2, y1};
                p3 = {z1, z2, z2, z1};
            }
            else if (K[4] == 2)
            {
                // cout << "iii.c\n";
                int32_t x1 = B - 1;
                int32_t y1 = 2;
                z1 = B - 1;
                int32_t x2 = (K[3]) >> 1;
                int32_t y2 = (K[3]) - x2;
                int32_t z2 = D(K[1] - x2 - y2 - 2, B);
                int32_t c2 = (x2 + y2 + z2 + 2 - K[1]) / B;
                int32_t x3 = (B - c2 - z2) >> 1;
                int32_t y3 = (B - c2 - z2) - x3;
                if (c2 != 2)
                {
                    // cout << "iii.c.1\n";
                    p1 = {x1, x2, x3, x2, x1};
                    p2 = {y1, y2, y3, y2, y1};
                    p3 = {z1, z2, z2, z1};
                }
                else if (c2 == 2)
                {
                    // cout << "iii.c.2\n";
                    p1 = {1, 2, B - 2, B - 2, 2, 1};
                    p2 = {1, B - 3, 1};
                    p3 = {B - 2};
                }
            }
            else if (K[4] >= 3)
            {
                // cout << "iii.d\n";
                int32_t c4 = (D(K[3] - 1, B) + 1 - K[3]) / B;
                int32_t z = D(K[1] - K[3] - 1 + c4, B);
                int32_t c2 = (2 - c4 + D(K[3] - 1, B) + z - K[1]) / B;
                p1 = {1, 1 - c4, 0, 0, 1 - c4, 1};
                p2 = {K[4] - 1, D(K[3] - 1, B), 2 - c2, D(K[3] - 1, B), K[4] - 1};
                p3 = {B - 2, z, B - 2};
            }
        }
        else if (D(K[0] - K[4] + 1, B) == 0 and K[3] != 0)
        {
            // cout << "iv\n";
            if (K[4] != B - 1)
            {
                // cout << "iv.a\n";
                int32_t x1 = (B + K[4]) >> 1;
                int32_t y1 = (B + K[4]) - x1;
                z1 = B - 1;
                int32_t c1 = (x1 + y1 + z1 - K[0]) / B;
                int32_t x2 = (K[3] - 1) >> 1;
                int32_t y2 = (K[3] - 1) - x2;
                int32_t z2 = D(K[1] - x2 - y2 - c1, B);
                int32_t c2 = (x2 + y2 + z2 + c1 - K[1]) / B;
                int32_t x3 = (1 + K[2] - c2) >> 1;
                int32_t y3 = (1 + K[2] - c2) - x3;
                p1 = {x1, x2, x3, x2, x1};
                p2 = {y1, y2, y3, y2, y1};
                p3 = {z1, z2, z1};
            }
            else if (K[4] == B - 1)
            {
                // cout << "iv.b\n";
                int32_t y2 = D(K[1] - 4, B) == B - 1 ? 3 : (D(K[1] - 4, B) == B - 2 ? 2 : 1);
                int32_t x2 = K[3] < y2 ? K[3] + B - y2 : K[3] - y2;
                int32_t c1 = (3 + y2 + D(K[1] - 3 - y2, B) - K[1]) / B;
                int32_t mu = 0;
                int32_t c2 = (x2 + D(K[2] - x2 - 1 - c1 - +mu, B) + c1 + 1 - K[2]) / B;
                if (c2 > 1)
                {
                    c2 = 1;
                    mu = 1;
                }
                int32_t c3 = (x2 + y2 - K[3]) / B;
                p1 = {1, 3 - c3, x2 - mu, x2 - mu, 3 - c3, 1};
                p2 = {B - 4, y2 - c2 + mu, D(K[2] - x2 - 1 - c1 + mu, B), y2 - c2 + mu, B - 4};
                p3 = {1, D(K[1] - 3 - y2, B) + c2 - mu + c3, 1};
            }
        }
        else if (D(K[0] - K[4] + 1, B) == 0 and K[3] == 0)
        {
            // cout << "v\n";
            if (K[4] == 0)
            {
                // cout << "v.a\n";
                if (K[2] != 0)
                {
                    // cout << "v.a.1\n";
                    vector<int32_t> compare2 = {1, 0, 0, 0, 0, 1};
                    vector<int32_t> K2 = big_sub(K, compare2, B);
                    vector<int32_t> p4;
                    p1 = compare2;
                    if (K2.size() == 1)
                    {
                        algorithm61(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 2)
                    {
                        algorithm62(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 3)
                    {
                        algorithm63(K2, B, l, p2, p3, p4);
                    }
                }
                else if (K[2] == 0 and K[1] != 0 and K[1] != B - 1)
                {
                    // cout << "v.a.2\n";
                    vector<int32_t> compare2 = {1, 0, 0, 0, 0, 1};
                    vector<int32_t> K2 = big_sub(K, compare2, B);
                    vector<int32_t> p4;
                    p1 = compare2;
                    if (K2.size() == 1)
                    {
                        algorithm61(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 2)
                    {
                        algorithm62(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 3)
                    {
                        algorithm63(K2, B, l, p2, p3, p4);
                    }
                }
                else if (K[2] == 0 and K[1] == 0)
                {
                    // cout << "v.a.3\n";
                    p1 = {1, 0, 0, 0, 0, 1};
                    p2 = {B - 2};
                    p3 = {0};
                }
                else if (K[2] == 0 and K[1] == B - 1)
                {
                    // cout << "v.a.4\n";
                    p1 = {B - 1, 0, 1, 0, B - 1};
                    p2 = {B - 1, B - 2, B - 2, B - 1};
                    p3 = {1, 0, 1};
                }
            }
            else if (K[4] == 1)
            {
                // cout << "v.b\n";
                if (K[2] >= 2 or (K[2] == 1 and K[1] != 0))
                {
                    // cout << "v.b.1\n";
                    vector<int32_t> compare2 = {1, 1, 0, 0, 1, 1};
                    vector<int32_t> K2 = big_sub(K, compare2, B);
                    vector<int32_t> p4;
                    p1 = compare2;
                    if (K2.size() == 1)
                    {
                        algorithm61(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 2)
                    {
                        algorithm62(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 3)
                    {
                        algorithm63(K2, B, l, p2, p3, p4);
                    }
                }
                else if (K[2] == 1 and K[1] == 0)
                {
                    // cout << "v.b.2\n";
                    p1 = {1, 0, B - 1, B - 1, 0, 1};
                    p2 = {1, B - 1, 1};
                    p3 = {B - 2};
                }
                else if (K[2] == 1 and K[1] == 1)
                {
                    // cout << "v.b.3\n";
                    p1 = {1, 1, 0, 0, 1, 1};
                    p2 = {B - 1, B - 1};
                    p3 = {0};
                }
                else if (K[2] == 0 and K[1] >= 2)
                {
                    // cout << "v.b.4\n";
                    if (K[1] == 2)
                    {
                        p1 = {1, 1, 0, 0, 1, 1};
                        p2 = {B - 1};
                        p3 = {0};
                    }
                    else
                    {
                        p1 = {1, 1, 0, 0, 1, 1};
                        p2 = {K[1] - 2, K[1] - 2};
                        p3 = {B - K[1] + 1};
                    }
                }
                else if (K[2] == 0 and K[1] == 1)
                {
                    // cout << "v.b.5\n";
                    p1 = {1, 0, 0, 0, 0, 1};
                    p2 = {1, 0, 0, 0, 1};
                    p3 = {B - 2};
                }
                else if (K[2] == 0 and K[1] == 0)
                {
                    // cout << "v.b.6\n";
                    p1 = {1, 0, 0, 0, 0, 1};
                    p2 = {B - 1, B - 1, B - 1, B - 1};
                    p3 = {0};
                }
            }
            else if (K[4] == 2)
            {
                // cout << "v.c\n";
                if (K[2] >= 2 or (K[2] == 1 and K[1] != 0))
                {
                    // cout << "v.c.1\n";
                    vector<int32_t> compare2 = {1, 2, 0, 0, 2, 1};
                    vector<int32_t> K2 = big_sub(K, compare2, B);
                    vector<int32_t> p4;
                    p1 = compare2;
                    if (K2.size() == 1)
                    {
                        algorithm61(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 2)
                    {
                        algorithm62(K2, B, l, p2, p3, p4);
                    }
                    else if (K2.size() == 3)
                    {
                        algorithm63(K2, B, l, p2, p3, p4);
                    }
                }
                else if (K[2] == 1 and K[1] == 0)
                {
                    // cout << "v.c.2\n";
                    p1 = {1, 1, B - 1, B - 1, 1, 1};
                    p2 = {1, B - 2, 1};
                    p3 = {B - 1};
                }
                else if (K[2] == 1 and K[1] == 1)
                {
                    // cout << "v.c.3\n";
                    p1 = {1, 1, B - 1, B - 1, 1, 1};
                    p2 = {1, B - 1, 1};
                    p3 = {B - 1};
                }
                else if (K[2] == 0 and K[1] >= 3)
                {
                    // cout << "v.c.4\n";
                    if (K[1] == 3)
                    {
                        // cout << "v.c.4.a\n";
                        p1 = {1, 2, 0, 0, 2, 1};
                        p2 = {B - 1};
                        p3 = {1};
                    }
                    else
                    {
                        // cout << "v.c.4.b\n";
                        p1 = {1, 2, 0, 0, 2, 1};
                        p2 = {K[1] - 3, K[1] - 3};
                        p3 = {B - K[1] + 3};
                    }
                }
                else if (K[2] == 0 and K[1] == 2)
                {
                    // cout << "v.c.5\n";
                    p1 = {1, 1, B - 1, B - 1, 1, 1};
                    p2 = {1, 0, 1};
                    p3 = {B - 1};
                }
                else if (K[2] == 0 and K[1] == 1)
                {
                    // cout << "v.c.6\n";
                    p1 = {1, 0, 0, 0, 0, 1};
                    p2 = {2, 0, 0, 0, 2};
                    p3 = {B - 2};
                }
                else if (K[2] == 0 and K[1] == 0)
                {
                    // cout << "v.c.7\n";
                    p1 = {1, 1, B - 1, B - 1, 1, 1};
                    p2 = {B - 2, B - 2};
                    p3 = {2};
                }
            }
            else if (K[4] == 3)
            {
                // cout << "v.d\n";
                int32_t y = 0;
                for (int32_t i = 1; i <= 3; i++)
                {
                    if (D(K[1] - 1 - i, B) != 0 and D(K[1] - 1 - i, B) != B - 1)
                    {
                        y = i;
                        break;
                    }
                }
                int32_t c1 = (2 + y + D(K[1] - 1 - y, B) - K[1]) / B;
                int32_t c2 = (B - y - 1 + D(K[2] + y + 2, B) + B - 1 - K[2]) / B;
                p1 = {1, 0, B - y - 1 - c1, B - y - 1 - c1, 0, 1};
                p2 = {2, y - c2 + 1 + c1, D(K[2] + y + 2, B), y - c2 + 1 + c1, 2};
                p3 = {B - 1, D(K[1] - 1 - y, B) + c2 - 1 - c1, B - 1};
            }
            else if (K[4] >= 4)
            {
                // cout << "v.e\n";
                int32_t y = 0;
                for (int32_t i = 1; i <= 3; i++)
                {
                    if (D(K[1] - 1 - i, B) != 0 and D(K[1] - 1 - i, B) != B - 1)
                    {
                        y = i;
                        break;
                    }
                }
                int32_t c1 = (1 + y + D(K[1] - 1 - y, B) - K[1]) / B;
                int32_t c2 = (B - y - 1 + D(K[2] + y - 1, B) + B - 1 - K[2]) / B;
                p1 = {1, 2, B - y - c1, B - y - c1, 2, 1};
                p2 = {K[4] - 3, y - c2 + c1, D(K[2] + y - 1, B), y - c2 + c1, K[4] - 3};
                p3 = {1, D(K[1] - 2 - y, B) + c2 - c1, 1};
            }
        }
    }
}

void algorithm6(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (K.size() == 1)
    {
        algorithm61(K, B, l, p1, p2, p3);
    }
    if (K.size() == 2)
    {
        algorithm62(K, B, l, p1, p2, p3);
    }
    if (K.size() == 3)
    {
        algorithm63(K, B, l, p1, p2, p3);
    }
    if (K.size() == 4)
    {
        algorithm64(K, B, l, p1, p2, p3);
    }
    if (K.size() == 5)
    {
        algorithm65(K, B, l, p1, p2, p3);
    }
    if (K.size() == 6)
    {
        algorithm66(K, B, l, p1, p2, p3);
    }
}

void big_sub_for_algorithm5(vector<int32_t> &K, int32_t B, int32_t l)
{
    int32_t m = l / 2;
    K[m - 1] -= 1;
    K[m] -= 1;
    for (int32_t i = m - 1; i < l - 1; i++)
    {
        if (K[i] < 0)
        {
            K[i + 1] -= 1;
            K[i] += B;
        }
    }
    if (!K.empty() and K.back() == 0)
    {
        K.pop_back();
    }
    if (K.empty())
    {
        K.push_back(0);
    }
}

void algorithm5(vector<int32_t> &K, int32_t B, int32_t l, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    int32_t m = l / 2;
    int32_t k = 0;
    vector<int32_t> K2(K.begin(), K.end());

    for (int32_t i = 1; i < 3; i++)
    {
        big_sub_for_algorithm5(K2, B, l);
        if (K2[m - 1] != 0 and K2[m] != 0)
        {
            k = i;
            break;
        }
    }
    // cout << K2 << "\n";
    l = K2.size();
    m = l >> 1;
    int32_t number_type = determine_number_type_and_make_initial_configuration(K2, B, (int32_t)K2.size(), p1, p2, p3);
    if (number_type == 20)
    {
        algorithm66(K2, B, l, p1, p2, p3);
    }
    if (p1.size() == 2 * m)
    {
        if (1 <= number_type and number_type <= 6)
        {
            algorithm2(K2, B, l, p1, p2, p3);
        }
        else if (11 <= number_type and number_type <= 16)
        {
            algorithm4(K2, B, l, p1, p2, p3);
        }
    }
    else if (p1.size() == 2 * m - 1)
    {
        p1.resize(l);
        p2.resize(l - 2);
        p3.resize(l - 3);
        if (K2[l - 1] == 1 and K2[l - 2] <= 2 and D(K2[0] - K2[l - 3], B) != 0)
        {
            int32_t z1 = D(K2[0] - K2[l - 3], B);
            p1[0] = p1[p1.size() - 1] = 1;
            p1[1] = p1[p1.size() - 2] = K2[l - 2];
            p2[0] = p2[p2.size() - 1] = K2[l - 3] - 1;
            p3[0] = p3[p3.size() - 1] = z1;
        }
        if (K2[l - 1] == 1 and K2[l - 2] <= 2 and D(K2[0] - K2[l - 3], B) == 0)
        {
            p1[0] = p1[p1.size() - 1] = 1;
            p1[1] = p1[p1.size() - 2] = K2[l - 2];
            p2[0] = p2[p2.size() - 1] = K2[l - 3] - 2;
            p3[0] = p3[p3.size() - 1] = 1;
        }
        algorithm4(K2, B, l, p1, p2, p3);
    }
    p1[m - 1] += k;
    p1[m] += k;
}

void execute_algorithm(int32_t algorithm_type, int32_t B, int32_t l, vector<int32_t> &K, vector<int32_t> &p1, vector<int32_t> &p2, vector<int32_t> &p3)
{
    if (algorithm_type == 1)
    {
        algorithm1(K, B, l, p1, p2, p3);
    }
    if (algorithm_type == 2)
    {
        algorithm2(K, B, l, p1, p2, p3);
    }
    if (algorithm_type == 3)
    {
        algorithm3(K, B, l, p1, p2, p3);
    }
    if (algorithm_type == 4)
    {
        algorithm4(K, B, l, p1, p2, p3);
    }
    if (algorithm_type == 5)
    {
        algorithm5(K, B, l, p1, p2, p3);
    }
    if (algorithm_type == 6)
    {
        algorithm6(K, B, l, p1, p2, p3);
    }
}

bool has_trailing_zeroes(vector<int32_t> &p1)
{
    return p1.size() == 0 or (p1.size() > 1 and p1[p1.size() - 1] == 0);
}

bool valid_coefficient(vector<int32_t> &p1, int32_t B)
{
    return all_of(p1.begin(), p1.end(), [B](int32_t i)
                  { return 0 <= i and i < B; });
}

bool is_palindrome(vector<int32_t> &p1)
{
    int32_t start = 0;
    int32_t end = p1.size() - 1;
    while (start <= end)
    {
        if (p1[start] != p1[end])
        {
            return false;
        }
        start += 1;
        end -= 1;
    }
    return true;
}

int32_t main()
{
    fastIO();
    int32_t T;
    cin >> T;
    for (int32_t i = 0; i < T; i++)
    {
        vector<int32_t> K, p1, p2, p3;
        int32_t l, B;
        string K2;
        cin >> B >> K2;
        // cout << B << " " << K2 << " " << K2.length() << "\n";
        for (auto it = K2.rbegin(); it != K2.rend(); ++it)
        {
            K.push_back(letter_to_number(*it));
        }
        // cout << B << "\n";
        // cout << K << "\n";
        l = (int32_t)K.size();
        // cout << l << "\n";
        int32_t number_type = determine_number_type_and_make_initial_configuration(K, B, l, p1, p2, p3);
        // cout << number_type << "\n";
        int32_t algorithm_type = determine_algorithm_type(l, number_type, K);
        // cout << algorithm_type << "\n";
        execute_algorithm(algorithm_type, B, l, K, p1, p2, p3);
        vector<int32_t> result = big_three_sum(p1, p2, p3, B);
        cout << p1 << " " << p2 << " " << p3 << "\n";
        //  if (result != K)
        //  {
        //  cout << "BREAK\n";
        //  break;
        // }
        // cout << result << " " << (result == K) << "\n";
    }
}
