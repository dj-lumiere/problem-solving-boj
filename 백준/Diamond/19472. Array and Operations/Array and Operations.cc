#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <cassert>
#include <functional>
#include <list>
#include <set>
#include <cmath>
#include <algorithm>
#include <cassert>

using namespace std;

#define int long long
#define var auto
#define in :
typedef pair<int, int> p;
typedef vector<int> iv;
template<typename T, typename C = less<T>>
using pq = priority_queue<T, vector<T>, C>;
#define endl '\n'
#define blank ' '
#define inf 0x7fffffffll

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    int q;
    cin >> q;
    var dt = iv(n);
    for (var &x in dt) cin >> x;

    typedef struct {
        int mx, mi, sum;
    } ST;
    var st = vector<ST>(n << 2);

    var lazy_add = iv(n << 2, 0);
    var lazy_set = iv(n << 2, 0);

    var merge = [&](ST a, ST b) {
        return ST{max(a.mx, b.mx), min(a.mi, b.mi), a.sum + b.sum};
    };

    function<void(int, int, int)> init_st = [&](int l, int r, int lev) {
        if (l == r) {
            st[lev] = ST{dt[l], dt[l], dt[l]};
            return;
        }
        var mid = (l + r) >> 1;
        init_st(l, mid, lev << 1);
        init_st(mid + 1, r, lev << 1 | 1);
        st[lev] = merge(st[lev << 1], st[lev << 1 | 1]);
    };

    var spread = [&](int s, int e, int lev) {
        if (lazy_set[lev]) {
            st[lev].mx = st[lev].mi = lazy_set[lev];
            st[lev].sum = (e - s + 1) * st[lev].mx;
        }

        st[lev].mx += lazy_add[lev];
        st[lev].mi += lazy_add[lev];
        st[lev].sum += (e - s + 1) * lazy_add[lev];

        if (s != e)
            for (var nx in {lev << 1, lev << 1 | 1}) {
                if(lazy_set[lev]) {
                    lazy_set[nx] = lazy_set[lev];
                    lazy_add[nx] = 0;
                }
                lazy_add[nx] += lazy_add[lev];
            }
        lazy_set[lev] = 0;
        lazy_add[lev] = 0;
    };

    function<void(int, int, int, int, int, int)> update_sum = [&](int begin, int end, int d, int l, int r, int lev) {
        spread(l, r, lev);
        if (end < l || r < begin) return;
        if (begin <= l && r <= end) {
            lazy_add[lev] += d;
            spread(l, r, lev);
            return;
        }
        var mid = (l + r) >> 1;
        update_sum(begin, end, d, l, mid, lev << 1);
        update_sum(begin, end, d, mid + 1, r, lev << 1 | 1);
        st[lev] = merge(st[lev << 1], st[lev << 1 | 1]);
    };

    function<void(int, int, int, int, int)> update_sqrt = [&](int begin, int end, int l, int r, int lev) {
        spread(l, r, lev);
        if (end < l || r < begin) return;
        if (begin <= l && r <= end && st[lev].mx <= 1) return;
        if (begin <= l && r <= end && (int) sqrt(st[lev].mx) == (int) sqrt(st[lev].mi)) {
            lazy_set[lev] = (int)sqrt(st[lev].mx);
            spread(l, r, lev);
            return;
        }
        if(begin <= l && r <= end && (int) sqrt(st[lev].mx) == (int) sqrt(st[lev].mi)+1 && st[lev].mx == st[lev].mi + 1) {
            lazy_add[lev] = (int)sqrt(st[lev].mi) - st[lev].mi;
            spread(l, r, lev);
            return;
        }
        var mid = (l + r) >> 1;
        update_sqrt(begin, end, l, mid, lev << 1);
        update_sqrt(begin, end, mid + 1, r, lev << 1 | 1);
        st[lev] = merge(st[lev << 1], st[lev << 1 | 1]);
    };

    function<int(int, int, int, int, int)> get_sum = [&](int begin, int end, int l, int r, int lev) {
        spread(l, r, lev);
        if (r < begin || end < l) return 0ll;
        if (begin <= l && r <= end) return st[lev].sum;
        var mid = (l + r) >> 1;
        return get_sum(begin, end, l, mid, lev << 1) + get_sum(begin, end, mid + 1, r, lev << 1 | 1);
    };

    init_st(0, n - 1, 1);

    while (q--) {
        int com;
        cin >> com;
        switch (com) {
            case 1: {
                int l, r, d;
                cin >> l >> r >> d;
                l--;
                r--;
                update_sum(l, r, d, 0, n - 1, 1);
            }
                break;
            case 2: {
                int l, r;
                cin >> l >> r;
                l--;
                r--;
                update_sqrt(l, r, 0, n - 1, 1);
            }
                break;
            case 3: {
                int l, r;
                cin >> l >> r;
                l--;
                r--;
                cout << get_sum(l, r, 0, n - 1, 1) << endl;
            }
                break;
        }
    }
    return 0;
}