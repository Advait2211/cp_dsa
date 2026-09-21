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
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    // map<ll, vector<ll>> mp;

    // for(ll i = 0; i < n; i++){
    //     mp[v[i]].push_back(i);
    // }

    // for (auto itr : mp) {
    //     cout << itr.first << ": ";

    //     for (auto idx : itr.second) {
    //         cout << idx << " ";
    //     }

    //     cout << endl;
    // }

    unordered_map<ll, ll> mp;

    for(ll i = 0; i < n; i++){
        mp[v[i]] = i+1;
    }

    // print(mp);

    ll mx = 0;

    if (mp[1] > 0) mx = max(mx, 2 * mp[1]);

    for(ll i = 1; i <= 1000; i++){
        for(ll j = i+1; j <= 1000; j++){
            if(gcd(i, j) == 1 and mp[i] > 0 and mp[j] > 0) mx = max(mx, mp[i]+mp[j]);
        }
    }

    if (mx == 0) return -1;

    return mx;




}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  