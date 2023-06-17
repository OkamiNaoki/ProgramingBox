
#include<bits/stdc++.h>
#define rep(i,n) for(int i=1;i<=(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
int n;
int count=0;
cin>>n;
rep(i,n){
string s=to_string(i);
if(s.size()%2==1)count++;
}
cout<<count;
}