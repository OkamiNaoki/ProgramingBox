#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;


int main(){
int n;
int d;
int ans=0;
cin>>n>>d;
vector<double>x(n);
vector<double>y(n);
rep(i,n)cin>>x[i]>>y[i];
rep(i,n){
    if(sqrt(x[i]*x[i]+y[i]*y[i])<=d){
        ans++;
    }


}
cout<<ans;
    
}