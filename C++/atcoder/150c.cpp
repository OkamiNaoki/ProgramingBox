#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int n;cin>>n;
    vector<int>p(n);
    vector<int>q(n);
    rep(i,n)cin>>p[i];
    rep(i,n)cin>>q[i];
 int ans1=0;
 int ans2=0;
     do{
   ans1++;
 
  }while(next_permutation(p.begin(),p.end()));

  do{

  }while(next_permutation(q.begin(),q.end()));
cout<<abs(ans1-ans2);
}