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

    for(ll i = 2; i <= n/i; i++){
        if(n % i == 0){
            facts.push_back(i);
            if(i != n/i) facts.push_back(n/i);
        }
    }

    return facts;

}

ll solve(){
    ll n; cin >> n;
    vector<ll> v(n); for(ll i = 0; i < n; i++) cin >> v[i];

    ll sm = accumulate(v.begin(), v.end(), 0LL);

    // cout << sm << endl;

    // vector<ll> facts = factors(sm);

    // sort(facts.rbegin(), facts.rend());
    // print(facts);

    // for(auto itr: facts){
    //     ll temp_sm = 0;
    //     for(ll i = 0; i < n; i++){
    //         temp_sm += v[i];
    //         if (temp_sm == itr) return itr;
    //         else if(temp_sm > itr) break;
    //     }
    //     // if(temp_sm == itr) 
    // }

    ll temp_sm = 0;

    ll soln = 1;

    for(ll i = 0; i < n-1; i++){
        temp_sm += v[i];
        soln = max(soln, gcd(temp_sm, sm - temp_sm));
    }

    return soln;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  