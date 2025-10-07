#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define VEC(name, n, init) vector<ll> name(n, init)

void solve() {
    ll n;
    cin >> n;
    VEC(a, n, 0ll);
    for (int i = 0; i < n; i++) cin >> a[i];

    multimap<ll, ll> mpp;

    for (int i = 0; i < n; i++) {
        auto it = mpp.upper_bound(a[i]);  // first key > a[i]
        if (it != mpp.end()) {
            mpp.erase(it);               // erase strictly larger key
        }
        mpp.insert({a[i], i});           // insert current element
    }

    cout << mpp.size() << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
