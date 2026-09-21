#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n; cin >> n;
    ll MOD = 1e9;

    ll sol = 0;

    // ll fact = 1;

    // for(ll i = 1; i <= n; i++){
    //     fact = (fact * i);
    //     while(fact%10 == 0) {
    //         sol += 1;
    //         fact /= 10;
    //     }
    //     fact %= MOD;
    // }

    while(n){
        n /= 5;
        sol += n;
    }

    cout << sol << '\n';
}