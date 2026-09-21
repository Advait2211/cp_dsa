#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll solve(){
    ll n, k;
    cin >> n >> k;

    if (n > k){
        if (n % 2 == 0) return n * n - k + 1;
        return (n-1) * (n-1) + k;
    } else{
        if (k % 2 == 1) return k * k - n + 1;
        return (k-1) * (k-1) + n;
    }
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}