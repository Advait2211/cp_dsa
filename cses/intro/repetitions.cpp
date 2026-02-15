#include <bits/stdc++.h>
//#define all(s) s.begin(), s.end()
using namespace std;
using ll=long long;
using ull=unsigned long long;

const int _N=1e5+5;

int main() {
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	// int T = 1;
	// cin>>T;
	// while (T--) {
        // cout << "inside here";
	    string s;
        cin >> s;
        int yadu_ka_long = 0;
        int shaurya = 0;
        int i = 0;
        while (i < s.size()){
            if (s[i] == s[i+1]){
                while (s[i] == s[i+1]){
                    i++;
                    yadu_ka_long++;
                }
            }

            shaurya = max(yadu_ka_long+1, shaurya);
            yadu_ka_long = 0;
            i++;
        }

        cout << shaurya;
	// }
	return 0;
}