#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n;
    cin >> n;

    vector<ll> v(n);

    for(ll i = 0; i < n; i++) cin >> v[i];

    map<ll, ll>mpp;

    ll consec = 0, max_consec = 0, l = 0;

    for(ll r = 0; r<n; r++){
        mpp[v[r]]++;
        while(mpp[v[r]] > 1){
            mpp[v[l]]--;
            l++;
        }
        max_consec = max(max_consec, (r-l+1));
        // cout << consec << " ";
    }

    cout << max_consec << endl;

    // for(auto itr: mpp) cout << itr.first << " " << itr.second << endl;
}