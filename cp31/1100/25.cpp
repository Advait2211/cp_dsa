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

string solve(){
    string s; cin >> s;

    vector<ll> order;
    set<ll> st;

    ll idx = 0;

    bool invalid = false;

    for(auto itr: s){

        if (!invalid && st.find(itr) == st.end()){
            st.insert(itr);
            order.push_back(itr);
        } else {
            invalid = true;
            if(order[idx] != itr) return "NO";
            idx += 1;
            idx %= order.size();
        }
    }

    return "YES";

    

    for(auto itr: s){
        if(order[idx] != itr) return "NO";

        idx += 1;
        idx %= order.size();
    }

    return "YES";
}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  