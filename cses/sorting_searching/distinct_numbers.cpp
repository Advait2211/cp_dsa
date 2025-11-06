#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <cassert>
#include <unordered_set>
#include <chrono>
#include <iomanip>
#include <type_traits>
#include <utility>
#include <iterator>
#include <functional>
#include<vector>
using namespace std;

#define ll long long
#define endl '\n'
#define forn(start, end, var) for(ll var = start; var < end; var++)
#define forrn(start, end, var) for(ll var = start; var > end; var--)
#define fora(v, var) for(const auto& var: v)
#define rt return
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define _sort(v) sort(all(v))
#define sum(v) accumulate(all(v), 0ll)
#define str(s) to_string(s)
#define len(x) x.size()
#define pb push_back
#define get_bit(x,r) (x&(1<<r))
#define M 1000000007
#define precision(x, p) std::cout << std::fixed << std::setprecision(p) << x << endl;

template <typename T>
class MyVector : public vector<T> {
private:
    int adjustIndex(int idx) const {
        if (idx < 0) idx += this->size();
        assert(idx >= 0 && idx < this->size() && "Invalid Index");
        rt idx;
    }
public: 
    using vector<T>::vector;
    MyVector(size_t n, const T& value) : vector<T>(n, value) {}

    T& operator[](int idx) {
        rt vector<T>::operator[](adjustIndex(idx));
    }
    const T& operator[](int idx) const {
        rt vector<T>::operator[](adjustIndex(idx));
    }
};
template<typename T> using vc = MyVector<T>;
template<typename T> using vcc = vc<vc<T>>;

#define pi pair<int, int>
#define pl pair<ll,ll>
#define vi vc<int>
#define vl vc<ll>
#define vpi vc<pi>
#define vpl vc<pl>
#define vs vc<string>
#define vvi vcc<int>
#define vvl vcc<ll>
#define vvs vcc<string>

struct custom_hash {
static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
}
size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
}
};
#ifdef ONLINE_JUDGE
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
#define um gp_hash_table
#else
#define um unordered_map
#endif
template<typename Key, typename Value, typename Hash = custom_hash>
using hashmap = um<Key, Value, Hash>;

ll binExp(ll a, ll b, ll mod = M,ll ans=1) {
    for (; b; b >>= 1, a = a * a % mod)
        if (b & 1) ans = a * ans % mod;
    rt ans;
}

vs split(const string& str, const char& sep = ',') {
    vs rs;string tk;stringstream ss(str);
    while (getline(ss, tk, sep)) {
        tk.erase(0, tk.find_first_not_of(' '));tk.erase(tk.find_last_not_of(' ') + 1);
        rs.push_back(tk);}
    rt rs;
}

template<typename T>
typename std::enable_if<std::is_arithmetic<T>::value||std::is_same<T,char>::value>::type
inline pim(const T& in,string s=""){cout<<in<<s;}
inline void pim(const string& in,string s=""){cout<<in<<s;}
template<typename T1,typename T2>
inline void pim(const std::pair<T1,T2>& p,string s=""){cout<<'(';pim(p.first,", ");pim(p.second,")");cout<<s;}
template<typename T>
typename std::enable_if<std::is_same<decltype(std::begin(std::declval<T>())),decltype(std::end(std::declval<T>()))>::value>::type
inline pim(const T& c,string s=""){cout<<'[';ll n=c.size();fora(c,x){n--;pim(x,n?", ":"");}cout<<"]";cout<<s;}
template<typename Fs,typename... R>
void print(const Fs& f,const R&... r){if constexpr(sizeof...(r)>0){pim(f, " ");print(r...);}else{pim(f);cout<<endl;}}

vs debugVarName(0);
ll debugVarNameIdx;
template<typename T>
inline void dbgi(T& x){print(debugVarName[debugVarNameIdx], "=", x);};
template<typename Fs, typename ...R>
inline void dbgi(Fs& f, R&... r){dbgi(f);debugVarNameIdx++;dbgi(r...);}
#define dbg(...) do { \
    debugVarName = split(#__VA_ARGS__); \
    debugVarNameIdx = 0;\
    dbgi(__VA_ARGS__);\lear
    cout << endl; \
} while(0)

// template<typename T>
// inline auto vec(int n, T in){return MyVector(n, in);}
// template<typename... Args>
// inline auto vec(int n, Args... args) {return MyVector(n, vec(args...));}

template<typename T>
inline void fill(T& x){cin >> x;}
template<typename T, typename L>
inline void fill(pair<T, L>& p){fill(p.F);fill(p.S);}
template<typename T>
inline void fill(vc<T>& v){forn(0, v.size(),i)fill(v[i]);}
template<typename... Args, typename T>
inline void fill(T& first, Args&... args) {fill(first);fill(args...);}

template<typename T>
inline T min(const vc<T>& v) {rt *min_element(all(v));}
template<typename T>
inline T max(const vc<T>& v) {rt *max_element(all(v));}

template<typename T>
inline int min_idx(const vc<T>& v){rt min_element(all(v))-v.begin();}
template<typename T>
inline int max_idx(const vc<T>& v){rt max_element(all(v))-v.begin();}

template<typename... Args, typename T>
inline T max(T fs, T sn, Args... a){rt max({fs, sn, a...});}
template<typename... Args, typename T>
inline T min(T fs, T sn, Args... a){rt min({fs, sn, a...});}

void prc(bool con, string yes, string no){
    if (con) print(yes);
    else print(no);
}

template<typename T>
void pra(vc<T>& ve){
    forn(0, len(ve), i) cout << ve[i] << " ";
    cout << endl;
}

#define INT(...) ll int __VA_ARGS__; fill(__VA_ARGS__)
#define STR(...) string __VA_ARGS__; fill(__VA_ARGS__)
#define VEC(x, ...) auto x = vec(__VA_ARGS__); fill(x); 

inline ll ModAdd(ll a, ll b, ll m = M) { rt ((a % m) + (b % m)) % m; }
inline ll ModSub(ll a, ll b, ll m = M) { rt ((a % m) - (b % m) + m) % m; }
inline ll ModMul(ll a, ll b, ll m = M) { rt ((a % m) * (b % m)) % m; }
inline ll ModInv(ll a, ll m = M) { rt binExp(a, M - 2, M); }
inline ll ModDiv(ll a, ll b, ll m = M) { rt ModMul(a, ModInv(b, m), m); }

void precalc(){

}

void solve() {
    ll n;
    cin >> n;
    unordered_set<ll> s;
    forn(0, n, i){
        ll x; cin >> x;
        s.insert(x);
    }
    cout << s.size() << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t=1;
    // cin>>t;
    precalc();
    while(t--){
        solve();
    }
    rt 0;
}