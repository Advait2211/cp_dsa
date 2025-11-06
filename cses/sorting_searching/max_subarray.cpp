#include<bits/stdc++.h>
using namespace std;
#define ll long long 

int main(){
    ll n;
    cin >> n;

    vector<ll> v(n);
    for(ll i = 0; i < n; i++) cin >> v[i];

    ll max_sum = v[0];
    ll cur_sum = v[0];

    for (ll i = 1; i < n; i++){
        if (cur_sum < 0){
            cur_sum = 0;
        }
        cur_sum += v[i];
        max_sum = max(cur_sum, max_sum);
    }

    cout << max_sum;

    return 0;
    
}