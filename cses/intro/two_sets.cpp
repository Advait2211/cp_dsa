#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
int main(){
    ll n; cin >> n;

    if(n == 3){
        cout << "YES\n";
        cout << "1\n3\n";
        cout << "2\n1 2\n";
        return 0;
    }
 
    ll sm = (n * (n+1)) / 2;
 
 
    if(sm % 2 == 1){
        cout << "NO" << "\n";
        return 0;
    }
 
    cout << "YES\n";
 
    ll sm2 = 0;
    ll br = -1;
 
    for(ll i = n; i >= 0; i--){
        // cout << sm2 << endl;
        sm2 += i;
        if(sm2 > sm/2){
            sm2 -= i;
            br = i;
            break;
        }
    }
 
    cout << n - br + 1 << '\n';
 
    ll other = sm/2 - sm2;
 
 
    for(ll i = n; i > br; i--){
        cout << i << " ";
    }
 
    cout << other << "\n";
 
    cout << n - (n - br + 1) << '\n';
 
    for(ll i = 1; i <= br; i++){
        if(i != other) cout << i << " ";
    }
 
    cout << "\n";
 
 
    return 0;
 
}