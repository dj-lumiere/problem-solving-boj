#include <bits/stdc++.h>
using namespace std;

vector<int32_t> lcs_length(const string& A, const string& B, int32_t start_a, int32_t end_a, int32_t start_b,
    int32_t end_b)
{
    int32_t n = end_a - start_a;
    int32_t m = end_b - start_b;
    vector<int32_t> previous(m + 1, 0), current(m + 1, 0);

    for (int32_t i = 1; i <= n; ++i)
    {
        for (int32_t j = 1; j <= m; ++j)
        {
            if (A[start_a + i - 1] == B[start_b + j - 1])
            {
                current[j] = previous[j - 1] + 1;
            }
            else
            {
                current[j] = max(previous[j], current[j - 1]);
            }
        }
        previous = current;
    }
    return previous;
}

vector<int32_t> lcs_length_reverse(const string& A, const string& B, int32_t start_a, int32_t end_a, int32_t start_b,
    int32_t end_b)
{
    int32_t n = end_a - start_a;
    int32_t m = end_b - start_b;
    vector<int32_t> previous(m + 1, 0), current(m + 1, 0);

    for (int i = n - 1; i >= 0; --i)
    {
        for (int j = m - 1; j >= 0; --j)
        {
            if (A[start_a + i] == B[start_b + j])
            {
                current[j] = previous[j + 1] + 1;
            }
            else
            {
                current[j] = max(previous[j], current[j + 1]);
            }
        }
        previous = current;
    }
    return previous;
}

string hirschberg(const string& A, const string& B, int32_t start_a, int32_t end_a, int32_t start_b, int32_t end_b)
{
    int32_t n = end_a - start_a;
    int32_t m = end_b - start_b;

    if (n == 0)
    {
        return "";
    }
    if (n == 1)
    {
        for (int32_t j = start_b; j < end_b; ++j)
        {
            if (A[start_a] == B[j])
            {
                return string(1, A[start_a]);
            }
        }
        return "";
    }

    int32_t mid_a = start_a + n / 2;
    vector<int32_t> L1 = lcs_length(A, B, start_a, mid_a, start_b, end_b);
    vector<int32_t> L2 = lcs_length_reverse(A, B, mid_a, end_a, start_b, end_b);
    int32_t max_j = 0;
    int32_t max_val = 0;
    for (int j = 0; j <= m; ++j)
    {
        if (L1[j] + L2[j] > max_val)
        {
            max_val = L1[j] + L2[j];
            max_j = j;
        }
    }
    int split_b = start_b + max_j;
    string lcs_left = hirschberg(A, B, start_a, mid_a, start_b, split_b);
    string lcs_right = hirschberg(A, B, mid_a, end_a, split_b, end_b);
    return lcs_left + lcs_right;
}

int main()
{
    int32_t a, b;
    cin >> a >> b;
    string A, B;
    cin >> A >> B;
    string lcs = hirschberg(A, B, 0, a, 0, b);
    cout << lcs.length() << "\n" << lcs;
}
