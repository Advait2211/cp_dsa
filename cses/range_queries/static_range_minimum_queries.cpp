#include <bits/stdc++.h>
#define all(s) s.begin(), s.end()
using namespace std;
using ll=long long;
#define vecin(vec) for(auto &x : (vec)) cin >> x;

int main() {
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	ll n, q;
    cin >> n >> q;

    vector<ll> a(n);
    vector<vector <ll>> sparse;
    vecin(a);

    vector<ll> prefix_sum(n+1, 0);
    for(ll i = 1; i <= n; i++){
        prefix_sum[i] = prefix_sum[i-1] + a[i-1];
    }

    for(ll i = 0; i < q; i++){
        ll a, b;
        cin >> a >> b;
        cout << max(prefix_sum[b], prefix_sum[a-1]) - min(prefix_sum[b], prefix_sum[a-1]) << endl;
    }

	return 0;
}