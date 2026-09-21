#include<bits/stdc++.h>
using namespace std;
#define ll long long

string solve(){
    ll a, b; cin >> a >> b;

    if((a + b) % 3 != 0) return "NO";

    if(a >= (a + b) / 3 and b >= (a + b) / 3) return "YES";

    return "NO";
}

int main(){
    ll t; 
    cin >> t;
    while(t--) cout << solve() << '\n';
}