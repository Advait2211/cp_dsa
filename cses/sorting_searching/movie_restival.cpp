#include<bits/stdc++.h>
using namespace std;
#define ll long long

/*
logic would to be check by ending time
and pick the one which is shortest 
keep doing this
*/

int main(){
    ll n;
    cin >> n;

    map<ll, ll> mpp;

    for (ll i = 0; i < n; i++){
        ll a, b;
        cin >> a >> b;

        if (mpp.find(b) != mpp.end())
            mpp[b] = max(mpp[b], a);
        else
            mpp[b] = a;
    }
    ll soln = 0;
    ll ending_time = 0;


    for(auto itr: mpp){
        if (itr.second >= ending_time){
            soln += 1;
            ending_time = itr.first;
        }

        // cout << itr.first << " " << itr.second << endl;
    }

    cout << soln;
}