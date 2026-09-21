#include <bits/stdc++.h>
using namespace std;
#define ll long long
#include <algorithm>

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
    ll a, b, c; cin >> a >> b >> c;

    ll sm = (a + b + c) / 3;

    set<ll> st;

    st.insert(a);
    st.insert(b);
    st.insert(c);

    if (st.size() <= 2) return 0;

    ll mx = max({a, b, c});
    ll mn = min({a, b, c});

    ll none;
    if(a != mx and a != mn) none = a;
    if(b != mx and b != mn) none = b;
    if(c != mx and c != mn) none = c;

    return min({
        (mx - mn + 1) / 2,
        abs(mx - none),
        abs(mn - none)
    });

    // ll ans = 0;

    // ans += abs(sm - a);
    // ans += abs(sm - b);
    // ans += abs(sm - c);
    // ans /= 2;

    // return ans;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  