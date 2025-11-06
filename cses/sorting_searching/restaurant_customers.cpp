#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll n;
    cin >> n;

    map<ll, ll> mpp;

    for(ll i = 0; i < n; i++){
        ll a, b;
        cin >> a >> b;

        mpp.insert({a, 1});
        mpp.insert({b, -1});
    }

    ll max_ans = 0;
    ll cur_ans = 0;

    for(auto it: mpp){
        // cout << it.first << " " << it.second << endl;
        cur_ans += it.second;
        max_ans = max(cur_ans, max_ans);
    }

    cout << max_ans;

    return 0;

}