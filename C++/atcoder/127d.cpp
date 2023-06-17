#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
  int n,m;cin>>n>>m;
  vector<pair<ll,ll>>pa;
  for(ll i=0;i<n;i++){
      ll a; cin>>a;
      pa.push_back({a,1});

  }
  for(ll i=0;i<m;i++){
      ll b,c; cin>>b>>c;
      pa.push_back({c,b});
  }
  sort(pa.rbegin(),pa.rend());
  ll ans=0;
  ll cnt=0;
  for(ll i=0;i<pa.size();i++){
      if(cnt+pa[i].second<=n){
          ans+=pa[i].second*pa[i].first;
          cnt+=pa[i].second;
      }
      else{
          if(cnt<=n){
              ans+=(n-cnt)*pa[i].first;
              cnt=n;
          }
      }
  }
  cout<<ans<<endl;
  return 0;
}