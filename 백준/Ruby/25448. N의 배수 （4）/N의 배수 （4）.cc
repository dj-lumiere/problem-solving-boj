#include <cstdint>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int32_t> egz_composite(int32_t p, int32_t q, const vector<int32_t> &a);
vector<int32_t> egz_prime(int32_t p, const vector<int32_t> &a);
vector<int32_t> egz(int32_t n, const vector<int32_t> &a);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int32_t n;
	cin >> n;
	vector<int32_t> a(2 * n - 1);
	for (auto &x : a) {
        cin >> x;
    }
	vector<int32_t> egz_list = egz(n, a);
	for (int32_t i = 0; i < 2 * n - 1; i++) {
		if (not egz_list[i]) {
			continue;
		}
		cout << a[i] << " ";
	}
}

int32_t powmod(int32_t base, int32_t exp, int32_t mod) {
	int32_t res = 1;
	base %= mod;
	while (exp > 0) {
		if (exp & 1) { 
			res = (int64_t(res) * base) % mod;
		}
		base = (int64_t(base) * base) % mod;
		exp >>= 1;
	}
	return res;
}

int32_t mod_inverse(int32_t a, int32_t p) {
	return powmod(a, p - 2, p);
}

int32_t find_t(int32_t p, const vector<bool> &t, int32_t d, int32_t u, int32_t v) {
	int32_t inv_d = mod_inverse(d, p);
	int32_t l = (int32_t)(((int64_t(u) * inv_d) % p + p) % p);
	int32_t h = p + (int32_t)(((int64_t(v) * inv_d) % p + p) % p) % p;

	while (l + 1 != h) {
		int32_t m = (l + h) / 2;
		int32_t idx = (int32_t)(((int64_t(m) * d) % p + p) % p);
		if (t[idx])
			l = m;
		else
			h = m;
	}
	return (int32_t)(((int64_t(h) * d) % p + p) % p);
}

vector<int32_t> egz_composite(int32_t p, int32_t q, const vector<int32_t> &a) {
	vector<int32_t> S;
	for (int32_t i = 0; i < p - 1; i++) S.push_back(i);
	vector<vector<int32_t>> T(2 * q - 1, vector<int32_t>());
	for (int32_t i = 0; i < 2 * q - 1; i++) {
		for (int32_t j = 0; j < p; j++) {
			S.push_back((i + 1) * p + j - 1);
		}
		vector<int32_t > a_subset(2 * p - 1);
		for (int32_t j = 0; j < 2 * p - 1; j++) {
			a_subset[j] = a[S[j]];
		}
		vector<int32_t> ret = egz(p, a_subset);
		for (int32_t j = 0; j < 2 * p - 1; j++) {
			if (ret[j])
				T[i].push_back(S[j]);
		}
		vector<int32_t> new_S;
		for (int32_t j = 0; j < 2 * p - 1; j++) {
			if (not ret[j])
				new_S.push_back(S[j]);
		}
		S = new_S;
	}
	vector<int32_t> L(2 * p * q - 1, 0);
	vector<int32_t> a_final(2 * q - 1, 0);
	for (int32_t i = 0; i < 2 * q - 1; i++) {
		int32_t sum_val = 0;
		for (auto &t_val : T[i]) {
			sum_val += a[t_val];
		}
		a_final[i] = sum_val / p;
	}
	vector<int32_t> ret_final = egz(q, a_final);
	for (int32_t i = 0; i < 2 * q - 1; i++) {
		if (ret_final[i]) {
			for (auto &j : T[i]) {
				L[j] = 1;
			}
		}
	}
	return L;
}

vector<int32_t> egz(int32_t n, const vector<int> &a) {
	if (n == 1) return { 1 };
	for (int32_t i = 2; i < n; i++) {
		if (n % i == 0) { 
			return egz_composite(i, n / i, a); 
		}
	}
	return egz_prime(n, a);
}

vector<int32_t> egz_prime(int32_t p, const vector<int32_t> &a) {
	vector<int32_t> k(2 * p - 1);
	for (int32_t i = 0; i < 2 * p - 1; i++) k[i] = i;

	sort(k.begin(), k.end(), [&](int32_t x, int32_t y) -> bool {
		return (a[x] % p) < (a[y] % p);
	});
	vector<int32_t> L(2 * p - 1, 0);

	for (int32_t i = 1; i < p; i++) {
		if ((a[k[i]] % p) == (a[k[i + p - 1]] % p)) {
			for (int32_t j = i; j < i + p; j++) {
				L[k[j]] = 1;
			}
			return L;
		}
	}
	int32_t s = 0;
	for (int32_t i = 0; i < p; i++) {
		s = (s + a[k[i]]) % p;
	}

	vector<bool> T(p, false);
	vector<int32_t> P(p, -1);
	T[s] = true;
	for (int32_t i = 1; i < p; i++) {
		if (T[0])
			break;
		int32_t temp = (a[k[p + i - 1]] - a[k[i]]) % p;
		if (temp < 0) {
			temp += p;
			temp %= p;
		}
		int32_t t_i = find_t(p, T, temp, s, 0);
		T[t_i] = true;
		P[t_i] = i;
	}
	for (int32_t i = 0; i < p; i++) {
		L[k[i]] = 1;
	}
	int32_t c = 0;
	while (s != c) {
		int32_t i = P[c];
		L[k[i + p - 1]] = 1;
		L[k[i]] = 0;
		c = (c - (a[k[i + p - 1]] - a[k[i]])) % p;
		if (c < 0) {
			c += p;
			c %= p;
		}
	}
	return L;
}
