#include <bits/stdc++.h>
#define all(s) s.begin(), s.end()
using namespace std;
using ll=long long;
#define vecin(vec) for(auto &x : (vec)) cin >> x;

int main() {
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	ll n;
    cin >> n;

    vector<ll> v(n);
    vecin(v);
    ll soln = 0;

    for(ll i = 1; i < n; i++){
        if (v[i-1]>v[i]){
            // cout << "entered here" << endl;
            soln += v[i-1] - v[i];
            v[i] = v[i-1];
        }
    }

    cout << soln << endl;
	return 0;
}