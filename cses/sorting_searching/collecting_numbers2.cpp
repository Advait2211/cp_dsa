#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n, q;
    cin >> n >> q;

    map<ll, ll> mpp;
    vector<ll> v(n);

    for(ll i =0 ; i < n; i++) {
        cin >> v[i];
        mpp.insert({v[i], i});
    }

    // for(auto itr:mpp) cout << itr.first << " " << itr.second << endl;
    // cout << endl;

    for(ll qs = 0; qs < q; qs++){
        ll a, b;
        cin >> a >> b;

        swap(mpp[v[a-1]], mpp[v[b-1]]);

        // for(auto itr:mpp) cout << itr.first << " " << itr.second << endl;
        // cout << endl;

        ll prev = -1;
        ll count = 1;

        for (auto itr: mpp){
            if(prev > itr.second){
                count += 1;
                prev = itr.second;
            }
            else prev = itr.second;
        }

        cout << count << endl;
    }
}