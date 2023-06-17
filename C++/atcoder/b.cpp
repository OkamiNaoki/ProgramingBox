#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;
const ll mod =1000000007;

int main(){
    int n,x,y;
    int t=0;
      cin>>n>>x;
    vector<int>a(n);
    cin>>n>>x;
    rep(i,n){
        cin>>y;
        if(y==x)continue;
        a[t]=y;
        t++;
       
    }
    if(t==0){
        cout<<" ";
        return;
    }
    rep(i,t){
        cout<<a[i];
    }
}