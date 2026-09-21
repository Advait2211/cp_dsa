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
    string s; cin >> s;
    ll n = s.size();

    bool flag = false;
    ll first_zero = -1;

    for(ll i = 0; i < n; i++){
        if(!flag and s[i] == '0'){
            first_zero = i;
            flag = true;
        }
    }

    if(!flag) return n * n;

    flag = false;

    for(ll i = 0; i < n; i++){
        if(s[i] == '1') flag = true;
    }

    if(!flag) return 0;


    vector<ll> closest(n);

    ll cnt = -1;
    for(ll i = first_zero; i >= 0; i--){
        if(s[i] == '0') cnt = 0;
        else cnt++;

        closest[i] = cnt;
    }

    for(ll i = n-1; i > first_zero; i--){
        if(s[i] == '0') cnt = 0;
        else cnt++;

        closest[i] = cnt;
    }

    vector<ll> col(n);

    cnt = -1;
    for(ll i = first_zero; i < n; i++){
        if(s[i] == '0') cnt = 0;
        else cnt++;

        col[i] = cnt;
    }

    for(ll i = 0; i < first_zero; i++){
        if(s[i] == '0') cnt = 0;
        else cnt++;

        col[i] = cnt;
    }

    // print(closest);
    // print(col);


    ll maxans = 1;
    ll horiz = 0;
    ll vert = 0;

    for(ll i = 0; i < n; i++){
        if(s[i] == '1'){
            horiz = closest[i];
            vert = col[i] ;

            maxans = max(maxans, horiz*vert);
        } else {
            horiz = 0;
        }
    }

    return maxans;
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  