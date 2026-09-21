#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define printarr(arr, n) \
for(ll i = 0; i < n; i++) cout << arr[i] << " "; \
cout << endl;

#define printmat(mat, r, c) \
for(ll i = 0; i < r; i++){ \
    for(ll j = 0; j < c; j++) \
        cout << mat[i][j] << " "; \
    cout << endl; \
}

string solve(){
    ll n;
    cin >> n;

    vector<ll>v(n);
    
    for(ll i = 0; i < n; i++) cin >> v[i];

    vector<ll>postmin(n);
    vector<ll>premax(n);

    premax[0] = v[0];

    for(ll i = 1; i < n; i++){
        premax[i] = max(premax[i-1], v[i]);
    }

    postmin[n-1] = v[n-1];

    for(ll i = n-2; i >= 0; i--){
        postmin[i] = min(postmin[i+1], v[i]);
    }

    // printarr(postmin, n);
    // printarr(premax, n);

    for(ll i = 0; i < n; i++){
        if (postmin[i] < v[i] and premax[i] > v[i]){
            return "NO";
        }
    }

    return "YES";


}


int main(){
    ll t = 1; 
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }
}

