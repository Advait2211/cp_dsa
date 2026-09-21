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

ll solve(){
    ll n; cin >> n;
    vector<ll> v(n); for (ll i = 0; i < n; i++) cin >> v[i];

    ll neg = 0;
    ll mn = LLONG_MAX;
    bool zero = false;

    for(ll i = 0; i < n; i++){
        if(v[i] < 0) neg += 1;
        if(v[i] == 0) zero = true;

        mn = min(mn, abs(v[i]));
    }

    ll sm = 0;

    for (ll i = 0; i < n; i++){
        sm += abs(v[i]);
    }

    if (zero) return sm;

    if(neg % 2 == 0) return sm;

    return sm - 2 * abs(mn);


}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  