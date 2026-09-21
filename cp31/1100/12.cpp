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
    vector<ll>a(n); for(ll i = 0; i < n; i++) cin >> a[i];
    vector<ll>b(n); for(ll i = 0; i < n; i++) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    vector<ll> gt(n);

    for(ll i = 0; i < n; i++){
        auto temp = upper_bound(a.begin(), a.end(), b[i]);

        if (temp != a.end()){
            gt[i] = a.end()-temp;
        } else{
            return 0;
        }
    }

    ll ans = 1;
    const ll MOD = 1000000007;

    for (ll i = n-1; i >= 0; i--){
        ll mux = gt[i] - (n - i - 1);

        if (mux <= 0) return 0;

        ans = (ans * (mux % MOD)) % MOD;
    }

    return ans;

}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  