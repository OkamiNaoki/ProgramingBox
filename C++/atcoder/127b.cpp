#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    ll r,d,x;cin>>r>>d>>x;
    for(int i=1;i<=10;i++){
        ll ans;
        ans=r*x-d;
        cout<<ans<<endl;
        x=ans;

    }
}