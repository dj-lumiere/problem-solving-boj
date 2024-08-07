#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// print std::vector with std::cout's operator<<
template<typename element>
std::ostream& operator<<(std::ostream& os, const std::vector<element>& target)
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

class SegmentTree
{
public:
    std::vector<long> tree;
    int n;
    int height;
    int max_size;
    int index_offset;
    SegmentTree(const std::vector<long>& data)
    {
        n = data.size();
        height = static_cast<int>(std::ceil(std::log2(n)));
        max_size = 2 << height;
        index_offset = max_size >> 1;
        tree.resize(max_size);
        build(data);
    }

    SegmentTree(int size)
    {
        n = size;
        height = static_cast<int>(std::ceil(std::log2(n)));
        max_size = 2 << height;
        index_offset = max_size >> 1;
        tree.resize(max_size);
    }

    void build(const std::vector<long>& data)
    {
        for (int i = 0; i < n; i++)
        {
            tree[i + this->index_offset] = data[i];
        }
        for (int i = this->index_offset - 1; i > 0; i--)
        {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    void update(int index, long value)
    {
        index += index_offset;
        while (index > 0)
        {
            tree[index] += value;
            index >>= 1;
        }
    }

    long query(int left, int right)
    {
        left += index_offset;
        right += index_offset;
        long result = 0;
        while (left <= right)
        {
            if (left % 2 == 1)
            {
                result += tree[left];
                left += 1;
            }
            if (right % 2 == 0)
            {
                result += tree[right];
                right -= 1;
            }
            left >>= 1;
            right >>= 1;
        }
        return result;
    }

    long total_sum()
    {
        return tree[1];
    }
};

int main(){
	long n, m, k;
	cin >> n >> m >> k;
	vector<long> members(n + 1, 0);
	for (int i = 1; i <= n; i++){
		cin >> members[i];
	}
	SegmentTree a(members);
	for (int i = 0; i < m+k; i++){
		long q, x, y;
		cin >> q >> x >> y;
		if (q==1){
			long current = a.query(x, x);
			long delta = y - current;
			a.update(x, delta);
		}
		if (q==2){
			long result = a.query(x, y);
			cout << result << "\n";
		}
	}
}