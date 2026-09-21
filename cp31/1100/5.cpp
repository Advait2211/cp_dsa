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

vector<ll> factors(ll n){
    vector<ll> facts;
    facts.push_back(1);

    for(ll i = 2; i * i <= n; i++){
        if (n % i == 0) {
            facts.push_back(i);
            if(n/i != i) facts.push_back(n/i);
        }
    }

    // facts.push_back(n);

    return facts;
}

ll solve(){
    // take prefix sum
    // compute factors
    // for each factor, take the max - min 
    // maximum max - min is returned

    ll n; cin >> n;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    if(n==1)return 0;

    vector<ll> facts = factors(n);
    vector<ll>presum(n);
    presum[0] = v[0];

    for(ll i = 1; i < n; i++){
        presum[i] = presum[i-1] + v[i];
    }

    // print(facts);
    // print(presum);

    ll mx_diff = 0;


    for(auto itr: facts){
        ll mn = LLONG_MAX;
        ll mx = LLONG_MIN;

        ll prev = 0;

        for(ll i = itr-1; i < n; i+=itr){
            ll cur = presum[i] - prev;
            prev = presum[i];
            // cout << cur << endl;
            mn = min(mn, cur);
            mx = max(mx, cur);
            // cout << i << " ";
        }

        mx_diff = max(mx_diff, mx-mn);
        // cout << "itr " << itr << endl;
        // cout << "mx_diff " << mx_diff << endl;
    }

    return mx_diff;



}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}