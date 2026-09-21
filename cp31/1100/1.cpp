#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll solve(){
    ll n; cin >> n;
    string s; cin >> s;    

    set<string>st;
    ll sm = 0;

    for(ll i = 0; i < n; i++){
        if (st.contains(s[i])){
            cout << "lessgo";
        }
    }

    return sm;

}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

} 