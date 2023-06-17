#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int a,b;cin>>a>>b;
    if(a>=13){
        cout<<b;
        return 0;
    }
    if(a>=6&&a<=12){
        cout<<b/2;
        return 0;
    }
    if(a<=5){
        cout<<0;
        return 0;
    }
}