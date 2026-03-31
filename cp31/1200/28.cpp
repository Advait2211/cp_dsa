#include<bits/stdc++.h>
#define ll long long
#define vecin(name, n) vector<ll> name(n); for(ll i = 0; i < n; i++) cin >> name[i];
#define vecout(name) for(auto x : name) cout << x << " "; cout << '\n';
using namespace std;

void solve(){
    ll n, k;
    cin >> n >> k;
    vecin(v, n);

    /*
    very simple question.
    just requires a pure two-sum. 

    only catch is we check if this exists in the map:
    k - ai % k
    */

    map<ll, ll> need;

    unordered_set<ll> st;

    for(ll i = 0; i < n; i++){
        ll temp = (k - v[i] % k) % k; 
        need[temp] += 1;
    }

    ll soln1 = 0;
    ll soln2 = 0;

    for(auto &tmp: need){

        
        ll a = tmp.first;
        ll b = tmp.second;
        ll x = k - tmp.first;
        ll y = need[x];

        if (st.count(x) || st.count(a)) continue;
        st.insert(a);
        st.insert(x);

        // cout << a << " " << b << endl;
        // cout << x << " " << y << endl << endl;

        if(a == 0){
            if(b > 0 or y > 0){
                soln1 += 1;
                continue;
            }
        }

        if(a == x){
            if(b > 0) soln1 += 1;
            continue;
        }

        if(b == 0 && y == 0) continue;

        if(b == 0 || y == 0){
            soln1 += b + y;
        } else {
            soln1 += 1 + max(0LL, abs(b - y) - 1);
        }

        // if(b > y){
        //     soln1 += y + y + 1;
        //     b -= (y+1);
        //     soln1 += b;
        // } else if (y > b){
        //     soln1 += 1;
        //     y -= (b+1);
        //     soln1 += y;
        // } else {
        //     if(b > 0 && y > 0){
        //         soln1 += 1;
        //     }
        // }
    }

    cout << soln1 << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    ll t = 0;

    cin >> t;

    while(t--){
        solve();
    }
    
    return 0;
}