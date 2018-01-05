#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    cin >> n;
    if(n&1==1 or (n>=6 and n<=20)){
        cout<<"Weird\n";
    }
    else{
        cout<<"Not Weird\n";
    }
    return 0;
}
