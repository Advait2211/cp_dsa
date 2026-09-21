#include<bits/stdc++.h>
using namespace std;
using ll = long long;

vector<ll> factors(ll n){
    ll i = 2; 
    vector<ll> v (3);
    int cnt = 0;

    while(i * i < n){
        if(n % i == 0){
            v[cnt] = i;
            n /= i;
            cnt++;
            if(cnt==2){
                // if(n == i) return {-1, -1, -1};
                v[cnt] = n;
                return v;
            }
        }
        i++;
    }

    return {-1, -1, -1};
}

void solve(){
    ll n;
    cin >> n;
    vector<ll> vec = factors(n);

    if (vec[0] == -1) {
        cout << "NO" << endl;
        return;
    }

    cout << "YES" << endl;
    cout << vec[0] << " " << vec[1] << " " << vec[2] << endl;
}

int main(){
    ll t = 0;

    cin >> t;

    while (t--){
        solve();
    }

    return 0;
}