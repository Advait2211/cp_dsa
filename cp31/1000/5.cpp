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
    ll n, k; cin >> n >> k;

    ll temp; 
    vector<ll> v(n);
    for(ll i = 0; i < n; i++){
        cin >> temp;
        if (temp % k == 0) v[i] = k;
        else v[i] = temp % k;
    }

    vector<pair<ll, ll>> vp;

    for(ll i = 0; i < n; i++){
        vp.push_back({v[i], i});
    }

    sort(vp.begin(), vp.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
    if (a.first != b.first) return a.first > b.first;  
        return a.second < b.second;
    });

    // print(vp);

    for(auto itr: vp){
        cout << itr.second+1 << " ";
    }

    cout << endl;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        solve();
    }

}  