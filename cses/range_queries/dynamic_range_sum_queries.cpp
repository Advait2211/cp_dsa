#include<bits/stdc++.h>
using namespace std;
#define ll long long

vector<ll> fenwick;

void update(ll idx, ll n, ll val){
    while(idx <= n){
        fenwick[idx] += val;
        idx = idx + (idx & (-idx));
    }
}

ll query(ll idx){
    ll sm = 0;
    while(idx > 0){
        sm += fenwick[idx];
        idx = idx - (idx & (-idx));
    }

    return sm;
}


int main(){
    int n, q; cin >> n >> q;

    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    fenwick.resize(n+1);

    for(ll i = 0; i < n; i++){
        update(i+1, n, v[i]);
    }

    // for(ll i = 0; i <= n; i++) cout << fenwick[i] << " ";

    while(q--){
        ll o, idx, val; cin >> o >> idx >> val;

        if(o == 1){
            idx -= 1;
            ll change = val - v[idx];
            v[idx] = val;
            update(idx+1, n, change);
        } else {
            ll l = idx, r = val;
            cout << query(r) - query(l-1) << "\n";
        }
    }

}

