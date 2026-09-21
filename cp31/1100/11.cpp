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

ll check(){

}

ll solve(){
    ll n, k; cin >> n >> k;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    sort(v.begin(), v.end());
    ll l = 0, r = n-1;

    // print(v);

    vector<ll> presum(n+1); presum[0] = 0;

    for(ll i = 0; i < n; i++) presum[i+1] = presum[i] + v[i];

    // print(presum);

    

    l = 0;
    r = n - k;

    ll mx = presum[r] - presum[l];

    for(ll i = n-k-1; i < n; i++){
        // cout << l << " " << r << endl;
        // cout << mx << endl;
        mx = max(mx, presum[r] - presum[l]);
        l += 2;
        r += 1;
    }

    return mx;


    // for(ll i = 0; i < k; i++){
    //     if(v[l]+v[l+1] > v[r])r -= 1;
    //     else l += 2;
    // }

    // ll sm = 0;
    // for (ll i = l; i <= r; i++) sm += v[i];

    // return sm;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  