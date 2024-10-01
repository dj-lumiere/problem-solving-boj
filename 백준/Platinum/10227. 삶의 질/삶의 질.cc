#include <iostream>
#include <vector>
#include <cstdint>
#include <set>

using namespace std;

class MedianSet
{
    set<int32_t> lower_half; // Should contain floor(total_size / 2) elements
    set<int32_t> upper_half; // Should contain ceil(total_size / 2) elements
    void balance();

public:
    void insert(int32_t value);
    void erase(int32_t value);
    size_t size();
    int32_t find_median();
};

void MedianSet::balance()
{
    while (lower_half.size() > upper_half.size())
    {
        upper_half.insert(*prev(lower_half.end()));
        lower_half.erase(prev(lower_half.end()));
    }
    while (upper_half.size() > lower_half.size() + 1)
    {
        lower_half.insert(*upper_half.begin());
        upper_half.erase(upper_half.begin());
    }
}

void MedianSet::insert(int32_t value)
{
    if (upper_half.empty() || value >= *upper_half.begin())
    {
        upper_half.insert(value);
    }
    else
    {
        lower_half.insert(value);
    }
    balance();
}

void MedianSet::erase(int32_t value)
{
    if (lower_half.find(value) != lower_half.end())
    {
        lower_half.erase(value);
    }
    else if (upper_half.find(value) != upper_half.end())
    {
        upper_half.erase(value);
    }
    balance();
}

size_t MedianSet::size()
{
    return lower_half.size() + upper_half.size();
}

int32_t MedianSet::find_median()
{
    if (upper_half.empty())
    {
        throw std::runtime_error("MedianSet is empty");
    }
    return *upper_half.begin();
}

void fastIO()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int main()
{
    fastIO();
    int32_t r, c, h, w;
    cin >> r >> c >> h >> w;
    vector<vector<int32_t> > v(r, vector<int32_t>(c, 0));
    for (int32_t i = 0; i < r; i++)
    {
        for (int32_t j = 0; j < c; j++)
        {
            cin >> v[i][j];
        }
    }
    MedianSet median;
    for (int32_t i = 0; i < h; i++)
    {
        for (int32_t j = 0; j < w; j++)
        {
            median.insert(v[i][j]);
        }
    }
    int32_t highest_quality_rank = median.find_median();
    for (int32_t i = 0; i < r - h + 1; i++)
    {
        if (i & 1)
        {
            for (int32_t j = c - w - 1; j >= 0; j--)
            {
                for (int32_t k = 0; k < h; k++)
                {
                    median.erase(v[i + k][j + w]);
                    median.insert(v[i + k][j]);
                }
                highest_quality_rank = min(highest_quality_rank, median.find_median());
            }
            if (i != r - h)
            {
                for (int32_t k = 0; k < w; k++)
                {
                    median.erase(v[i][k]);
                    median.insert(v[i + h][k]);
                }
                highest_quality_rank = min(highest_quality_rank, median.find_median());
            }
        }
        else
        {
            for (int32_t j = 0; j < c - w; j++)
            {
                for (int32_t k = 0; k < h; k++)
                {
                    median.erase(v[i + k][j]);
                    median.insert(v[i + k][j + w]);
                }
                highest_quality_rank = min(highest_quality_rank, median.find_median());
            }
            if (i != r - h)
            {
                for (int32_t k = c - 1; k >= c - w; k--)
                {
                    median.erase(v[i][k]);
                    median.insert(v[i + h][k]);
                }
                highest_quality_rank = min(highest_quality_rank, median.find_median());
            }
        }
    }
    cout << highest_quality_rank << "\n";
}
