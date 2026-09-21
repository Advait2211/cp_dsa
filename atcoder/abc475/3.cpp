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
    ll n, s, k; cin >> n >> s >> k;
    vector<ll>v(n-1); for(ll i = 0; i < n-1; i++) cin >> v[i];
    /* 
    6 3 10
    5 2 4 1 6
    */

    vector<ll> presum(n);

    presum[0] = 0;

    for(ll i = 0; i < n-1; i++){
        presum[i+1] = presum[i] + v[i];
    }

    ll m = s - 1;
    ll r = n - 1;
    ll l = m;

    ll mx = 1;

    for(ll i = m; i < n; i++){
        if(presum[i] - presum[m] > k){
            r = i-1;
            break;
        }
    }

    // how far left can we go for each right
    while (r >= m){

        ll cost = presum[r] - presum[m];

        while(l > 0){
            ll extra = presum[m] - presum[l-1];

            if (2 * min(extra, cost) + max(extra, cost) > k) break;
            l -= 1;
        }

        mx = max(mx, r - l + 1);

        r -= 1;
    }

    return mx;

}

int main() {
    ll t = 1;
    // cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  