#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vecin(v) for(auto &x : (v)) cin >> x
#define vecout(v) for(auto &x : (v)) cout << x << ' '; cout << '\n'

bool dfs(ll row, ll col, vector<vector<char>> &mat, vector<vector<int>>& vis, vector<int>& delrow, vector<int>& delcol, int n, int m){

    vis[row][col] = 1;

    for(int i = 0; i < 4; i++)
    {
        int nrow = row + delrow[i];
        int ncol = col + delcol[i];

        if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && !vis[nrow][ncol])
        {
            if(mat[nrow][ncol] == '.')
            {
                if(dfs(nrow, ncol, mat, vis, delrow, delcol, n, m))
                {
                    vis[nrow][ncol] = 1;
                    continue;
                }
            }

            else if(mat[nrow][ncol] == '#')
            {
                return true;
            }
        }
    }
    return false;
}

int main(){
    ll n, m;
    cin >> n >> m;

    vector<vector<char>> mat(n, vector<char>(m));

    for(ll i = 0; i < n; i++){
        for(ll j = 0; j < m; j++){
            cin >> mat[i][j];
        }
    }

    ll count = 0;

    vector<vector<int>> vis(n, vector<int>(m, 0));

    vector<int> delrow = {-1, 0, 1, 0};
    vector<int> delcol = {0, 1, 0, -1};

    for(ll i = 0; i < n; i++){
        for(ll j = 0; j < m; j++){
            if(mat[i][j] == '.'){
                if (dfs(i, j, mat, vis, delrow, delcol, n, m)){
                    count++;
                    
                }
            }
        }
    }

    cout << count << endl;
}