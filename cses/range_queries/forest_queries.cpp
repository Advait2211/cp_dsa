#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll r, q; cin >> r >> q;
    vector<string> grid(r);

    for(ll i = 0; i < r; i++) cin >> grid[i];

    vector<vector<ll>> presum(r+1, vector<ll>(r+1));

    for(ll i = 0; i < r; i++){
        ll cnt = 0;
        for(auto itr: grid[i]){
            if(itr == '.'){
                presum[i+1][cnt+1] = presum[i+1][cnt];
            } else {
                presum[i+1][cnt+1] = presum[i+1][cnt] + 1;
            }
            cnt += 1;
        }
    }

    for(ll i = 1; i <= r; i++){
        for(ll j = 1; j <= r; j++){
            presum[i][j] += presum[i-1][j];
        }
    }

    // for(ll i = 0; i <= r; i++){
    //     for(ll j = 0; j <= r; j++){
    //         cout << presum[i][j] << " ";
    //     }

    //     cout << "\n";
    // }

    while(q--){
        ll y1, x1, y2, x2; cin >> y1 >> x1 >> y2 >> x2;

        cout << presum[y2][x2] - presum[y1-1][x2] - presum[y2][x1-1] + presum[y1-1][x1-1] << "\n";

        // ll sm = 0;

        // while(y1 <= y2){
        //     sm += (presum[y1-1][x2] - presum[y1-1][x1-1]);
        //     y1 += 1;
        // }

        // cout << sm << "\n";
    }

    return 0;
}