#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool possible(vector<ll> &v, ll height, ll w){

    ll sm = 0;

    for(auto itr: v){
        sm += max(0LL, height - itr);
    }

    if(sm > w) return false;
    return true;

}

ll solve(){
    ll n, w; cin >> n >> w;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    ll l = 0;
    ll h = *max_element(v.begin(), v.end());
    h = h + w;

    // cout << possible(v, 4, w) << endl;

    // cout << l << " " << h << endl;

    while(l < h){
        ll mid = (l+h+1) / 2;

        if (possible(v, mid, w)) l = mid;
        else h = mid - 1;

        // cerr << l << " " << h << '\n';

         

    }

    return l;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

} 