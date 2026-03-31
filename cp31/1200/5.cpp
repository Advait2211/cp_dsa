#include<bits/stdc++.h>
#define ll long long
using namespace std;

void solve(){
    ll n, k;
    cin >> n >> k;
    vector<ll> v(n);
    for(ll i = 0; i < n; i++) cin >> v[i];

    struct Node{
        ll prev = -1;
        ll maxi = 0;
        ll smaxi = 0;
    };

    map<ll, Node> mp;


    for(ll i = 0; i < n; i++){
        Node &temp = mp[v[i]];
        
        ll diff = i - temp.prev;
        if (diff >= temp.maxi){
            temp.smaxi = temp.maxi;
            temp.maxi = diff;
        } else if (diff > temp.smaxi){
            temp.smaxi = diff;
        }

        temp.prev = i;
    }

    for(auto &it: mp){
        Node &temp = it.second;

        ll diff = n - temp.prev;
        if (diff >= temp.maxi){
            temp.smaxi = temp.maxi;
            temp.maxi = diff;
        } else if (diff > temp.smaxi){
            temp.smaxi = diff;
        }
    }

    ll soln = INT_MAX;

    for(auto &it: mp){
        soln = min(soln, max((it.second.maxi + 1) / 2, it.second.smaxi));
    }

    cout << soln-1;
}

int main(){
    ll t = 0;

    cin >> t;

    while(t--){
        solve();
        cout << endl;
    }
    
    return 0;
}