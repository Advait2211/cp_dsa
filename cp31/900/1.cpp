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
    ll a, b; cin >> a >> b;
    ll k1, k2; cin >> k1 >> k2;
    ll q1, q2; cin >> q1 >> q2;

    set<pair<ll, ll>> k, q;

    k = {{k1 + a, k2 + b}, {k1 + a, k2 - b}, {k1 - a, k2 + b}, {k1 - a, k2 - b}, {k1 + b, k2 + a}, {k1 + b, k2 - a}, {k1 - b, k2 + a}, {k1 - b, k2 - a}};
    q = {{q1 + a, q2 + b}, {q1 + a, q2 - b}, {q1 - a, q2 + b}, {q1 - a, q2 - b}, {q1 + b, q2 + a}, {q1 + b, q2 - a}, {q1 - b, q2 + a}, {q1 - b, q2 - a}};


    ll cnt = 0;

    for (auto itr : k) {
        if (q.count(itr))
            cnt++;
    }

    return cnt;

}   

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  