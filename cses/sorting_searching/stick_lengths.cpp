#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n;
    cin >> n;

    vector<ll> v(n); 

    for(ll i = 0; i < n; i++) cin >> v[i];


    sort(v.begin(), v.end());
    ll median = v[v.size() / 2];


    ll cost = 0;
    for(ll i = 0; i < n; i++){
        cost += abs(v[i] - median);
    }   
    cout << cost;

    
}