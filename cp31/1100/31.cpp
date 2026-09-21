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
    ll n, q; cin >> n >> q;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];
    vector<ll> qr(q); for(ll i = 0; i < q; i++) cin >> qr[i];


    map<ll, ll> where;

    for(ll i = n-1; i >= 0; i--){
        where[v[i]] = i+1;
    }

    // print(where);

    for(ll z = 0; z < q; z++){
        ll query = qr[z];   

        cout << where[query] << " ";

        for (auto &[key, value] : where){
            if(value < where[query]) value += 1;
        }

        where[query] = 1;
    }
}

int main() {
    ll t = 1;
    // cin >> t;

    while (t--){
        solve();
    }

}  