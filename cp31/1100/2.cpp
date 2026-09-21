#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll solve(){
    ll n, k;
    cin >> n >> k;

    vector<ll>a(n); for(ll i = 0; i < n; i++) cin >> a[i];
    vector<ll>b(n); for(ll i = 0; i < n; i++) cin >> b[i];

    ll mx = 0, base_mx = 0, cur = 0, temp = 0;

    ll val = min(n, k);

    for(ll i = 0; i < val; i++){

        base_mx = max(base_mx, b[i]);
        cur += a[i];
        temp = cur + (k-i-1) * base_mx;
        mx = max(mx, temp);

    }

    return mx;


}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

} 