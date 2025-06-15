#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;

const ll INF = 1e18; // Changed to match the range of `ll`
const ll LINF = 1e18;
const ll MOD = 1e9 + 7;

#define fast_io() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define vll vector<ll>
#define vvll vector<vector<ll>>
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz(v) ((ll)(v).size())

#define min_heap priority_queue<ll, vector<ll>, greater<ll>>
#define max_heap priority_queue<ll>
#define dq deque<ll>
#define stk stack<ll>
#define q queue<ll>
#define pq priority_queue<ll>
#define uset unordered_set<ll>
#define umap unordered_map<ll, ll>

template <typename T>
inline void prtv(const vector<T>& v) {
    for (const auto& x : v) cout << x << " ";
    cout << endl;
}

template <typename T>
inline void prtl(initializer_list<T> v) {
    for (const auto& x : v) cout << x << " ";
    cout << endl;
}

inline vector<ll> stv(const string& s) {
    vector<ll> v;
    for (char c : s) {
        v.push_back(c - '0');
    }
    return v;
}

template <typename T>
inline vector<T> rv(ll n) {
    vector<T> v(n);
    for (ll i = 0; i < n; ++i) cin >> v[i];
    return v;
}

template <typename T>
inline void srtpl(vector<T>& v) {
    sort(v.begin(), v.end());
}

template <typename T>
inline void srtmn(vector<T>& v) {
    sort(v.rbegin(), v.rend());
}

struct DSU {
    vector<int> parent, rank, size;

    DSU(int n) {
        parent.resize(n);
        rank.assign(n, 0);
        size.assign(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int v) {
        if (parent[v] == v) return v;
        return parent[v] = find(parent[v]);  // Path compression
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            if (rank[a] < rank[b]) swap(a, b);
            parent[b] = a;
            size[a] += size[b];
            if (rank[a] == rank[b]) rank[a]++;
        }
    }

    bool same_set(int a, int b) {
        return find(a) == find(b);
    }

    int set_size(int v) {
        return size[find(v)];
    }
};


void solve() {
    // Add your problem logic here.
    ll n;
    cin>>n;
    string s;
    vector<ll> v;
    cin>>s;
    for(ll i=0; i<n; i++){
        v.push_back(s[i]-'0');
    }
    // prtv(v);
    ll cnt=0,  j=n-1;
    bool chk1=false;
    bool chk2=false;
    while(j>=0){
        if(chk1==false){
            if(v[j]==0){
                chk2=true;
            }else{
                chk1=true;
            }
        }else{
            if(v[j]==0){
                if(chk2){
                    cnt+=1;
                }
                chk2=false;
                chk1=false;
                j+=1;
                cnt+=1;
            }
        }
        j--;
    }
    if (chk1){
        if(chk2){
            cnt+=1;
        }
        cnt+=1;
    }
    cout<<cnt<<endl;
}

int main() {
    fast_io();
    ll t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}