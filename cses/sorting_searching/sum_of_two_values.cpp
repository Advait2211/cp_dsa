#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n, k;
    cin >> n >> k;

    vector<ll> v(n);
    map<ll, ll>mpp;

    for(ll i = 0; i < n; i++) cin >> v[i];

    for(ll i = 0; i < n; i++){
        ll need = k - v[i];

        if (mpp.find(need) != mpp.end()){
            cout << i+1 << " " << mpp[need]+1 << endl;
            return 0;
        }
        else{
            mpp.insert({v[i], i});
        }
    }

    cout << "IMPOSSIBLE";

    return 0;
}