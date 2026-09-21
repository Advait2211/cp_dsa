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
    string s; cin >> s;

    // char prev_char = s[0];
    // ll streak = 1, mx;
    // ll idx = -1;
    // bool flag = false;

    // for(ll i = 1; i < n-1; i++){
    //     if(s[i] == prev_char){
    //         streak += 1;
    //     } else if (!flag){
    //         flag = true;
    //     } else {
    //         if (prev_char == s[i]){
    //             streak += 1;
    //             if streak > 
    //         } else {
    //             streak = 1;
    //             prev_char = s[i-1];
    //         }
    //     }
    // }

    vector<ll>freq;
    string s2 = "";
    ll streak = 1;
    char prev = s[0];

    for(ll i = 1; i < n; i++){
        if (prev == s[i]){
            streak+=1;
        } else {
            s2 += prev;
            freq.push_back(streak);
            prev = s[i];
            streak = 1;
        }
    }

    s2 += prev;
    freq.push_back(streak);

    // print(freq);
    // print(s2);

    ll mxlen = 0;
    ll del = -1;

    ll flag = false;

    for(ll i = 1; i < freq.size()-1; i++){
        if(freq[i] != 1) continue;

        if (s2[i-1] == s2[i+1]){
            return freq.size() - 2;
        } else {
            flag = true;
        }
    }
    if(flag) return freq.size()-1;
    return freq.size();

}

int main() {
    ll t;
    cin >> t;

    while (t--){
        cout << solve() << endl;
    }

}  