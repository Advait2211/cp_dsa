#include <bits/stdc++.h>
#define all(s) s.begin(), s.end()
using namespace std;
using ll=long long;
#define vecin(vec) for(auto &x : (vec)) cin >> x;

int main() {
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	ll n;
    cin >> n;

    if(n == 1){
        cout << 1 << endl;
        return 0;
    }

    if(n < 4){
        cout << "NO SOLUTION" << endl;
        return 0;
    }

    for(ll i = n-1; i > 0; i -= 2){
        cout << i << " ";
    }

    for(ll i = n; i > 0; i -= 2){
        cout << i << " ";
    }

    
	return 0;

    // 2 4 1 3
}