#define ll long long
#define MAX 15840000
#include <iostream>
#include <unordered_map>
#include <cmath>

std::unordered_map<int, int> large_mu;
int mu[MAX + 1] = { 0, 1 };

ll mertens(int n) {
	if (n <= MAX) return mu[n];
	if (large_mu.find(n) != large_mu.end()) {
		return large_mu[n];
	}
	ll ans = 1;
	int i, j;
	for (i = 2; i <= n; i = j + 1) {
		j = n / (n / i);
		ans -= mertens(n / i) * (j - i + 1);
	}
	return large_mu[n] = ans;
}

ll small_squareFree(ll n) {
	ll d = sqrt(n);
	ll ans = 0;
	for (ll i = 1; i <= d; i++) {
		ans += ((ll)mu[i] - (ll)mu[i - 1]) * (n / (i * i));
	}
	return ans;
}

ll squareFree(ll n) {
	int d = sqrt(n);
    if ((ll)d * d < n){ d += 1;}
	int i, j;
	ll ans = 0;
	for (i = 1; i < d; i = j + 1) {
		j = sqrt(n / (n / ((ll)i * i)));
		ans += (mertens(j) - mertens(i - 1)) * (n / ((ll)i * i));
		i = j + 1;
	}
	return ans;
}

ll inline multiple(ll n, ll m, ll k) {
	return (ll)((__int128)n * m / k);
}

ll solve(ll n) {
    if (n == 4) {
        return 5;
    }
    if (n == 1) {
        return 1;
    }
	ll left;
	ll right;

	if (n < 1e12) {
		left = 1;
		right = n << 1;
	}
	else if (n < 10000000000000000) { // 1e16
		left = multiple(n,  164493406, 100000000);
		right = multiple(n, 164493407, 100000000);
	}
	else if (n < 100000000000000000) { // 1e17
		left = multiple(n,  164493406684, 100000000000);
		right = multiple(n, 164493406685, 100000000000);
	}
	else {
		left = multiple(n,  1644934066848000, 1000000000000000);
		right = multiple(n, 1644934066848400, 1000000000000000);
	}


	while (left < right) {
		ll mid = (left + right) >> 1;
		ll count = squareFree(mid);
        if (count < n) {
			left = mid + 1;
		}
		else {
			right = mid;
		}
	}
	return left;
}

int main() {
	for (int i = 1; i <= MAX; i++) {
		for (int j = 2; i * j <= MAX; j++) {
			mu[i * j] -= mu[i];
		}
		mu[i] += mu[i - 1];
	}
	ll n;
    std::cin >> n;
	std::cout << solve(n) << "\n";
	return 0;
}
