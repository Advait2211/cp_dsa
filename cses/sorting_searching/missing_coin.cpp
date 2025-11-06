#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n;
    cin >> n;

    vector<ll> v(n);
    for(ll i = 0; i < n; i ++) cin >> v[i];

    sort(v.begin(), v.end());

    ll reachable = 0;
    ll k = 0;
    for(ll i = 0; i < n; i++){
        if (v[i] <= reachable+1){
            reachable += v[i];
        } else {
            k = i;
            break;
        }
    }

    cout << reachable + 1;
    return 0;
}

/*
1 1
1 2 - 1 2 3
1 2 3 - 1 2 3 5 6
1 2 3 4 - 1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


okay what could be the logic of solving this question

we find the smallest coin that is missing
after that
how do you compute which would be the smallest value which is unachievable by not having that coin

oh simple
find the smallest missing number
if 1, 1; 2, 2; 4, 4;
else output sum of all numbers + 1

that would work, only if there can be 1 count of the same coin. 
since you have have multiple of the same coins, this will not work

so what to do

*/