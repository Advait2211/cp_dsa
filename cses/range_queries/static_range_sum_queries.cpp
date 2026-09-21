#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    int n, q; cin >> n >> q;

    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    vector<ll>presum(n+1);
    presum[0] = 0;

    for(ll i = 0; i < n; i++){
        presum[i+1] = presum[i] + v[i];
    }

    while(q--){
        ll l, r;
        cin >> l >> r;

        cout << presum[r] - presum[l-1] << "\n";
    }


}

