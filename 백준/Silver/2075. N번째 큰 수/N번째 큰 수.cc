#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int32_t n, num;
	cin >> n;
	vector<int32_t> q(n * n);
	for (int32_t i = 0; i < n; i += 1)
	{
		for (int32_t j = 0; j < n; j += 1)
		{
			cin >> num;
			q[i * n + j] = num;
		}
	}
	sort(q.begin(), q.end());
	cout << q[n * n - n];
	return 0;
}