#include<bits/stdc++.h>
using namespace std;
using ll = long long;

string solve(){
    ll n;
    cin >> n;

    vector<ll>v(n);
    bool pos = true;

    for(ll i = 0; i < n; i++){
        cin >> v[i];
        if (v[i] < 0) pos = false;
    }

    if (pos) return "YES";

    vector<ll> prefix(n+1, 0);

    for(ll i = 0; i < n; i++){
        prefix[i+1] = prefix[i] + v[i];
    }

    vector<ll> pmin(n+1);
    pmin[0] = prefix[0];

    for(ll i = 0; i < n; i++){
        pmin[i+1] = min(pmin[i], prefix[i+1]);
    }

    ll val = 0;

    for(ll i = 0; i < n; i++)
    {
        if (v[i] - pmin[i+1] >= prefix[n]) return "NO";
    }


    // for(ll i = 0; i <= n; i++) cout << prefix[i] << " ";
    // cout << endl;
    // for(ll i = 0; i <= n; i++) cout << pmin[i] << " ";
    // cout << endl;
    // for(ll i = 0; i <= n; i++) cout << smax[i] << " ";
    // cout << endl;
    return "YES";




}

int main(){
    ll t = 0;
    cin >> t;

    while(t--){
        cout << solve() << endl;
    }
}