#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll solve(ll n){

    /*
    // 2 ways to reach max
    // alternate placement in rows
    // 2 row at a time placement

    if(n==1) return 1;
    if(n==2) return 4;
    
    if (n%2 == 0){
        // even logic
        return n * (n/2);
    } else {
        // odd logic
        ll c = ceil(n/2) * ceil(n/2);
        ll f = n/2 * n/2;

        return c + f;
    }
    */


    if(n==0)return 0;
    // (corner + edge + center) * 2
    /*
    2 - corners
    3 - after corner - side pixels
    4 - rest of the middle side pixels + 2, 2 (inner square corner)
    6 - 
    8 - 
    */


}

int main() {
    ll t;
    cin >> t;

    ll temp = t;

    while (t--){
        cout << solve(temp-t) << endl;
    }

} 