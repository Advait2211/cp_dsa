#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#define ll long long
#define fast_io ios::sync_with_stdio(false); cin.tie(NULL);

void solve(){
    int n; cin >> n;
    vector<ll> a(n);
    int zero = 0;

    for(int i = 0; i<n; i++) {
        cin >> a[i];
        if(a[i] == 0) zero ++;
    }

    // vector<ll> temp = a;
    // sort(temp.begin(), temp.end());

    if(zero == 0){
        cout << "YES" << "\n";
        for(int i = 0; i<n; i++) cout <<"A";
        cout << "\n";
        return;
    }

    if(zero == 1){
        cout << "NO" << "\n";
        return;
    }

    bool A = false, B = true;
    string ans (n, 'C');

    if(true){
        for(int i = 0; i<n; i++){
            if(a[i] == 0){
                if (!A){
                    A = true;
                    ans[i] = 'A';
                }
                else if(B){
                    B = true;
                    ans[i] = 'B';
                }
                else ans[i] = 'C';
            }
        }
    }
    else{ 
        int flag = 0;

        for (int i = 0; i < n; i++) {
            if (a[i] == 0) {
                if (flag == 0)
                    ans[i] = 'A';
                else if (flag == 1)
                    ans[i] = 'B';
                else if (flag == 2)
                    ans[i] = 'C';
                else
                    ans[i] = 'B';

                flag++;
            }
            else {
                ans[i] = 'B';
            }
        }
    }

    cout << "YES" << "\n" << ans << "\n";
}

int main() {
    fast_io;

    int t;
    cin >> t;
    while(t--) {
        solve();
    }

    return 0;
}