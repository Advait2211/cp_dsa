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
    ll n, l, r; cin >> n >> l >> r;
    vector<ll> v(n);

    for(ll i = 1; i <= n; i++){
        ll temp = (l + i - 1) / i;

        if(temp * i > r){
            cout << "NO" << endl;
            return;
        }

        v[i-1] = temp * i;
    }

    cout << "YES" << endl;
    for(ll i = 0; i < n; i++) cout << v[i] << " ";
    cout << endl;
    return;

    /* 
    
    observation 1: all n should have a element they divide in l - r, else the answer is no
    
    proved - we need at least n/2 + 1 elements in the range
    disproved, we could have just one number that is the multiplication of all and it would work


    */

    ll pivot = -1;

    for(ll i = l; i <= r; i++){
        if(i % n == 0){
            pivot = i;
            break;
        }
    }

    if(pivot == -1){
        cout << "NO" << endl;
        return;
    }

    ll base = 0;

    // vector<ll> v(n+1);

    base = pivot / n;
    v[n] = pivot;

    for(ll i = n-1; i >= 1; i--){
        if(pivot % i == 0){
            v[i] = pivot;
            base = pivot / i;
            continue;
        }

        ll diff = i - base;
        pivot += diff;

        if(pivot > r or pivot < l){
            if (pivot > r){
                pivot -= i;
            } else {
                pivot += i;
            }
            

            if(pivot > r or pivot < l){
                cout << "NO" << endl;
                return;
            }
        }

        // if(pivot > r or pivot < l){
        //     pivot -= (2 * diff);


        //     if(pivot > r or pivot < l){
        //         cout << "NO" << endl;
        //         return;
        //     }
        // }

        

        v[i] = pivot;
        base = pivot / i;
    }

    cout << "YES" << endl;
    for(ll i = 1; i <= n; i++) cout << v[i] << " ";

    cout << endl;


}

int main() {
    ll t;
    cin >> t;

    while (t--){
        solve();
    }

}  