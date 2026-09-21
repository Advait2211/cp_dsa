#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll solve(){
    ll n; cin >> n;
    vector<ll>a(n); for(ll i = 0; i < n; i++) cin >> a[i];

    vector<ll>a2 = a; sort(a2.begin(), a2.end());

    vector<ll>presum(n); presum[0] = a2[0];
    for(ll i = 1; i < n; i++) presum[i] = presum[i-1] + a2[i];

    vector<ll> reach(n);
    reach[n-1] = n-1;

    for(ll i=n-2; i >= 0; i--){
        if (presum[i] >= a2[i+1]){
            reach[i] = reach[i+1];        
        } else {
            reach[i] = i;
        }
    }

    for(ll i = 0; i < n; i++){
        ll idx = lower_bound(a2.begin(), a2.end(), a[i]) - a2.begin();
        cout << reach[idx] << " ";
    }

    cout << endl;
    return 0;





}

int main() {
    ll t=1;
    cin >> t;

    while (t--){
        solve();
    }

} 