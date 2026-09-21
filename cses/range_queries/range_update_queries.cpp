#include<bits/stdc++.h>
using namespace std;
#define ll long long

vector<ll> fenwick;

void update(ll idx, ll val){ 
    ll n = fenwick.size();
    while (idx <= n){
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
    ll n, q; cin >> n >> q;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    vector<ll> diff(n);
    diff[0] = v[0];

    for(ll i = 1; i < n; i++){
        diff[i] = v[i] - v[i-1];
    }

    fenwick.resize(n+1);

    for(ll i = 0; i < n; i++){
        update(i+1, diff[i]);
    }

    // for(ll i = 0; i <= n; i++) cout << fenwick[i] << " ";

    while(q--){
        ll type;
        cin >> type;

        if(type == 1){
            ll l, r, val;
            cin >> l >> r >> val;

            update(l, val);

            if(r < n) update(r+1, -val);

        } else {
            ll idx;
            cin >> idx;

            cout << query(idx) << "\n";
        }
    }

    return 0;


}