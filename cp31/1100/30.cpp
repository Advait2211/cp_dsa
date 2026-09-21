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

string solve(){
    ll n; cin >> n;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    ll ele1 = -1, ele2 = -1;

    for(ll i = 0; i < n; i++){
        if(v[i] != v[n - i - 1]){
            ele1 = v[i];
            ele2 = v[n - i - 1];
        }
    }

    if(ele1 == -1){
        return "YES";
    }

    // check if array is palindrome without ele1
    ll fc = 0, bc = 0;
    bool flag = true;
    for(ll i = 0; (i+fc) < n; i++){
        if(i+fc >= n - i - 1 - bc) break;

        while(v[i + fc] == ele1) fc += 1;
        while(v[n - i - 1 - bc] == ele1) bc += 1;

        if(v[i + fc] != v[n - i - 1 - bc]) flag = false;
    }

    if(flag) return "YES";

    // check if array is palindrome without ele2
    fc = 0, bc = 0;
    flag = true;
    for(ll i = 0; (i+fc) < n; i++){
        if(i+fc >= n - i - 1 - bc) break;

        while(v[i + fc] == ele2) fc += 1;
        while(v[n - i - 1 - bc] == ele2) bc += 1;

        if(v[i + fc] != v[n - i - 1 - bc]) flag = false;
    }

    if(flag) return "YES";

    return "NO";
    
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  