#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;


ll n;
vector<ll>h(n),s(n);

bool jadge(ll x){
    vector<ll>v(n);
    rep(i,n){
        if(x<h[i])return false;
        ll tlimit=(x-h[i])/s[i]; //xに二部探査の値を代入することで求めている
        v[i]=tlimit;
    }
    sort(v.begin(),v.end());
    rep(i,n){
        if(v[i]<i)return false;
    }
    return true;
}

int main(){
    cin>>n;
     h.resize(n),s.resize(n);
    rep(i,n){
        cin>>h[i]>>s[i];

    }

    ll lb=0,ub=25;;
    while(ub-lb>1){
        ll half=(lb+ub)/2;
        if(jadge(half)){
            ub=half;
        }else lb=half;
    }
cout<<ub<<endl;
}