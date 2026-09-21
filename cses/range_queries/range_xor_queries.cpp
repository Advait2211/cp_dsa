#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n, q; cin >> n >> q;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    vector<ll> pre(n+1);

    pre[0] = 0;

    for(ll i = 0 ; i < n; i++){
        pre[i+1] = pre[i] ^ v[i];
    }

    while(q--){
        ll l, r; cin >> l >> r;
        cout << (pre[l-1] ^ pre[r]) << '\n';
    }

    return 0;
}

// how chip verification is done, and what is being done to automate that part. 