#include<bits/stdc++.h>
using namespace std;
#define ll long long

/*
0 0 1 0 1 1
0 0 1 1 2 3

- 2 6 1 4 2

- 0 1 2 3 4



*/

vector<ll>fenwick;

void update(ll idx, ll val){
    ll n = fenwick.size();
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
    ll n; cin >> n;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];
    vector<ll> queries(n); for(ll i = 0; i < n; i++) cin >> queries[i];


    fenwick.resize(n+1);

    for(ll i = 0; i < n; i++){
        update(i+1, 1);
    }

    for(ll i = 0; i < n; i++){
        ll q = queries[i];

        ll l = 0, r = n;
        while (l < r){
            ll mid = (l + r)/2;

            ll val = query(mid);

            if (val < q){
                l = mid+1;
            } else {
                r = mid;
            }
        }

        cout << v[r-1] << " ";
        // cout << query(r) << "\n";
        update(r, -1);

    }
}

