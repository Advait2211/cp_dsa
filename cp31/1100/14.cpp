#include <bits/stdc++.h>
using namespace std;
#define ll long long

// ---------- Check if something is iterable ----------

template<typename T, typename = void>
struct is_iterable : false_type {};

template<typename T>
struct is_iterable<T, void_t<
    decltype(begin(declval<T>())),
    decltype(end(declval<T>()))
>> : true_type {};


// ---------- Generic ----------

template<typename T>
typename enable_if<!is_iterable<T>::value>::type
print_one(const T& x) {
    cout << x;
}


// ---------- Pair ----------

template<typename A, typename B>
void print_one(const pair<A, B>& p) {
    cout << '(';
    print_one(p.first);
    cout << ", ";
    print_one(p.second);
    cout << ')';
}


// ---------- Containers ----------

template<typename T>
typename enable_if<is_iterable<T>::value>::type
print_one(const T& container) {
    cout << '[';

    bool first = true;

    for (const auto& x : container) {
        if (!first) cout << ", ";
        first = false;

        print_one(x);
    }

    cout << ']';
}


// ---------- Python-like print ----------

template<typename... Args>
void print(const Args&... args) {
    ((print_one(args), cout << ' '), ...);
    cout << '\n';
}

void solve(){
    ll n; cin >> n;
    vector<ll>a(n); for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll>a2(n); for (ll i = 0; i < n; i++) cin >> a2[i];

    ll firstdiff = n, lastdiff = 0;

    for(ll i = 0; i < n; i++){
        if(a[i] != a2[i]){
            firstdiff = i;
            break;
        }
    }

    /* 
        4
        1 2 3 4
        1 2 3 4
    */

    for(ll i = n-1; i >= 0; i--){
        if(a[i] != a2[i]){
            lastdiff = i;
            break;
        }
    }

    if (firstdiff == n) {
        ll ln = 1, mxln = 1;
        ll start = 0, ansStart = 0, ansEnd = 0;

        for (ll i = 0; i < n - 1; i++) {

            if (a2[i] <= a2[i + 1]) {
                ln++;

                if (ln > mxln) {
                    mxln = ln;
                    ansStart = start;
                    ansEnd = i + 1;
                }

            } else {
                ln = 1;
                start = i + 1;
            }
        }
        cout << ansStart+1 << " " << ansEnd+1 << endl;
        return;
    }

    while(true){
        if(firstdiff > 0 and a2[firstdiff] >= a2[firstdiff-1])firstdiff--;
        else break;
    }

    while(true){
        if(lastdiff < (n-1) and a2[lastdiff] <= a2[lastdiff+1]) lastdiff++;
        else break;
    }

    cout << firstdiff+1 << " " << lastdiff+1 << endl;

}

int main() {
    ll t;
    cin >> t;

    while (t--){
        solve();
    }

}  