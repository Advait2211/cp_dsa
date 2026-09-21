#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll MOD = 1e9 + 7;

int main(){
    ll n; cin >> n;
    // if(n == 1) cout << 2 << '\n';

    ll ans = 2;

    for(ll i = 1; i < n; i++){
        ans = (ans * 2) % MOD;
    }

    cout << ans << '\n';
}