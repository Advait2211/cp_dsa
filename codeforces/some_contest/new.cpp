#include<bits/stdc++.h>
using namespace std;
 
#define ll long long
 
int main(){
    ll n;
    cin >> n;
 
    vector<ll> dp(n+1, 0);
    dp[1] = 1;
    // dp[2] = 2;
    
 
    for(ll i = 2; i <= n; i++){
        ll count = 0;
        for (ll j = 1; j <= 6; j++){
            if (i - j >= 0){
                count += 1;
                dp[i] += 1 + dp[i-j];
            }
        }
        dp[i] -= count - 1;
        dp[i] %= (ll)(1e9+7);
    }
 
 
 
    cout << dp[n] << endl;
    // for(ll i = 0; i <= n; i++) cout << dp[i] << " ";
}


/*

# if colors[-1] >= remaining[2]:
        #     colors[-1] -= remaining[2]
        #     remaining[2] = 0
        #     cost += 1
        #     continue
        
        # if colors[-1] >= remaining[1]:
        #     colors[-1] -= remaining[1]
        #     remaining[1] = 0
        #     cost += 1
        #     continue
                
        # if colors[-1] >= remaining[0]:
        #     colors[-1] -= remaining[0]
        #     remaining[0] = 0
        #     cost += 1
        #     continue*/