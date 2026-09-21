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
    ll n, k; cin >> n >> k;

    vector<ll>a(n); for(ll i = 0; i < n; i++) cin >> a[i];
    vector<ll>b(n); for(ll i = 0; i < n; i++) cin >> b[i];
    vector<ll>c(n); for(ll i = 0; i < n; i++) cin >> c[i];

    vector<ll> soln;

    for(auto it: a){
        if((k & it) == it) soln.push_back(it);
        else break;
    }

    for(auto it: b){
        if((k & it) == it) soln.push_back(it);
        else break;
    }

    for(auto it: c){
        if((k & it) == it) soln.push_back(it);
        else break;
    }

    ll sol = 0;
    for (auto it : soln){
        sol = sol | it;
    }

    // print(soln);
    // print(sol);

    if (sol == k) return "Yes";
    return "No";

}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  