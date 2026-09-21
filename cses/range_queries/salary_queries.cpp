#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n, q; cin >> n >> q;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    multiset<pair<ll, ll>> ms;

    for(ll i = 0; i < n; i++){
        ms.insert({v[i], i});
    }



    while(q--){
        char opr; cin >> opr;
        if(opr == '?'){
            ll l, r; cin >> l >> r;

            cout << distance(
                ms.lower_bound({l, 0}),
                ms.upper_bound({r, LLONG_MAX})
            ) << '\n';


        } else {
            ll idx, new_sal; cin >> idx >> new_sal;
            idx -= 1;
            ll old_val = v[idx];

            ms.erase(ms.find({old_val, idx}));
            ms.insert({new_sal, idx});
            v[idx] = new_sal;
        }

        // for (auto itr : ms) {
        //     cout << itr.first << " " << itr.second << endl;
        // }
        // cout << endl;
    }
}