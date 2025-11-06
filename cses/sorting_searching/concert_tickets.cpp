#include<bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
    ll n, m;
    cin >> n >> m;

    vector <ll> h(n);
    vector <ll> t(m);

    for(ll i = 0; i < n; i++) cin >> h[i];
    for(ll i = 0; i < m; i++) cin >> t[i];

    // for(ll i = 0; i < n; i++) cout << h[i] << " ";

    sort(h.begin(), h.end());

    multiset<ll> ms(h.begin(), h.end());

    for(ll i = 0; i < m; i++){
        if (ms.size() == 0){
            cout << -1 << endl;
            continue;
        }
        ll target = t[i];

        auto k = ms.upper_bound(target);

        // if (target < h[0]){
        //     cout << -1 << endl;
        //     continue;
        // }

        if (k == ms.begin() && *k > target){
            cout << -1 << endl;
            continue;
        }
        
        if (k == ms.end() || *k > target) k--;
        cout << *k << endl;

        ms.erase(k);
    }
    return 0;

}