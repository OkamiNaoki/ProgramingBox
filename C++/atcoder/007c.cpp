#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
int n;
cin>>n;
vector<vector<int>>v(n);
rep(i,n)cin>>v[i];
v[1].push_back(10);
rep(i,n+1){
    rep(j,2){
    cout<<v[i][j]<<endl;
    }
}


}