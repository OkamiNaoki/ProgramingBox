#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
int n;
int count=0;
int ans=0;
cin>>n;
for(int i=1;i<=n;i++){
    count=0;
if(i%2==0)continue;
for(int  j=1;j<=i;j++){
    if(j%2==0)continue;
    if(i%j==0)count++;
}
if(count==8)ans++;
}
cout<<ans;

}