#include<iostream>
#include <vector>
using namespace std;

int main(){
    long long t;
    cin >> t;

    vector<int> arr(t);  // create vector of size t

    for (int i = 0; i < t; i++) {
        cin >> arr[i];  // take input for each element
    }

    arr = sort

    // (Optional) print to verify
    for (int x : arr) cout << x << " ";
    cout << endl;

    return 0;
}