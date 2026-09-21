#include<bits/stdc++.h>

using namespace std;
#define ll long long

int main(){
    ll n, q; cin >> n >> q;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];
    vector<ll> queries(n); for(ll i = 0; i < q; i++) cin >> queries[i];

    set<pair<ll, ll>> vp;
    for(ll i = 0; i < n; i++){
        vp.insert({v[i], i});
    }

    // sort(vp.begin(), vp.end());

    // for(auto itr: vp){
    //     cout << itr.first << " " << itr.second << endl;
    // }

    for(ll i = 0; i < q; i++){
        ll query = queries[i];
        auto it = vp.lower_bound({query, 0});

        if(it == vp.end()){
            cout << 0 << " ";
        } else {
            auto temp = *it;
            cout << temp.second+1 << " ";
            // cout << temp.first << " " << temp.second << endl;
            vp.erase(it);

            temp.first -= query;
            vp.insert(temp);
        }

    }



}