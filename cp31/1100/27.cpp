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
    /*
    what is the goal here? we have to remove all elements but one
    effectively we have to choose which element we want to keep last
    and in what sequence we want to order the elements

    both the order and the chosen element matter
    so effectively we can convert this into a single sorting problem

    
    */

    ll n, k; cin >> n >> k;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    set<ll> want;

    for(ll i = 0; i < n; i++){
        if(want.count(v[i])) return "YES";

        want.insert(v[i] - k);
        want.insert(v[i] + k);
    }

    for(ll i = 0; i < n; i++){
        if(want.count(v[i])) return "YES";
    }

    return "NO";
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  