#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int n,m;cin>>n>>m;
    int ans=0;
    vector<int>l(m);
    vector<int>r(m);
    rep(i,m)cin>>l[i]>>r[i];
    sort(l.begin(),l.end());
    sort(r.begin(),r.end());

    for(int i=l[m-1];i<=r[0];i++){
        ans++;
    }
   
    cout<<ans;

}