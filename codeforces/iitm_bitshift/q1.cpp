#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll t;
    cin >> t;

    while(t--){

        ll n;
        cin >> n;
        vector<ll> v(n);
        map<ll, ll> mp;

        for(ll i = 0; i < n; i++){
            cin>>v[i];
            mp[v[i]] = i;
        }

        stack<pair<ll,ll>> st;
        vector<ll> prev(n, 0);
        set<ll> fc;

        for(ll i = 0; i < n; i++){
            if(!fc.count(v[i])){
                fc.insert(v[i]);
                if (st.empty()){
                    st.push({mp[v[i]], i});
                } else {
                    pair<ll, ll> tp = st.top();
                    if(tp.first > mp[v[i]]){
                        st.push({mp[v[i]], i});
                    } else {
                        st.pop();
                        st.push({mp[v[i]], tp.second});
                    }
                }
            }

            pair<ll, ll> tp = st.top();

            if(i == tp.first){
                prev[i] = ((tp.second==0)? 0: prev[tp.second-1])+1;
                st.pop();
            } 
        }

        ll sm = accumulate(prev.begin(), prev.end(), 0LL);

        cout << sm << endl;

    }
}