// #include<bits/stdc++.h>
// using namespace std;
// #define ll long long
// #define vecin(v) for(auto &x : (v)) cin >> x
// #define vecout(v) for(auto &x : (v)) cout << x << ' '; cout << '\n'

// static ll vis[200005];
// static ll timer = 1;

// ll mex(vector<ll> &a) {
//     for (ll x : a)
//         if (x >= 1 && x <= (ll)a.size())
//             vis[x] = timer;

//     for (ll i = 1; i <= (ll)a.size(); i++)
//         if (vis[i] != timer)
//             return i;

//     timer++;
//     return a.size() + 1;
// }


// int main(){
//     ll n, k;
//     cin >> n >> k;

//     vector<ll> v(k);
//     vecin(v);

//     vecout(v);

//     ll m = mex(v);
//     cout << m;

//     vector<ll> dp (n+1, false);

//     dp[0] = false;

//     for (auto val : v){
//         dp[val] = true;
//     }

//     vecout(dp);

//     /*
//     mex (1 idx)
//     dp[i] = !dp[i-mex]
//     */

//     for(ll i = m+1; i < n; i++){
//         dp[i] = !dp[i-m];
//     }

//     vecout(dp);
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> p(k);
    for (int i = 0; i < k; i++) cin >> p[i];

    vector<bool> win(n + 1, false);
    win[0] = false;

    for (int i = 1; i <= n; i++) {
        for (int move : p) {
            if (i - move >= 0 && !win[i - move]) {
                win[i] = true;
                break;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << (win[i] ? 'W' : 'L');
    }
    cout << '\n';
}
