#include<bits/stdc++.h>
using namespace std;
#define ll long long

// solved in 5 minutes after previous question after thinking whether i should go out to eat. crazy.

int main(){
    ll n;
    cin >> n;

    map<ll, ll> mpp;
    vector<ll> v(n);

    for(ll i =0 ; i < n; i++) {
        cin >> v[i];
        mpp.insert({v[i], i});
    }
    ll prev = -1;
    ll count = 1;

    for (auto itr: mpp){
        if(prev > itr.second){
            count += 1;
            prev = itr.second;
        }
        else prev = itr.second;
        // cout << itr.first << " " << itr.second << endl;
    }

    cout << count;


}