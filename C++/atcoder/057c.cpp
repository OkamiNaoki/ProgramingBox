#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    ll n,a;
    cin>>n;
    ll ans=100;
    string s;
    for(ll i=1;i<=sqrt(n);i++){
        if(n%2==1&&i%2==0)continue;
        if(n%i==0){
        s=to_string(max(i,n/i));
        a=s.size();
        ans=min(ans,a);
        }

    }
    cout<<ans<<endl;
}