#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
int n,m;
int ans=0;
cin>>n>>m;
vector<vector<bool>>root(n);//boolで通れる道とそうでない道を分ける
rep(i,n){root[i].resize(n);}//これは必要っぽい
rep(i,m){
    int a,b;
    cin>>a>>b;
    
    root[a-1][b-1]=root[b-1][a-1]=true;//無向グラフなので
}
vector<int>v(n);
rep(i,n)v[i]=i;

do{
    bool ok =true;//boolで判別はじめtrueで消去法
    rep(i,n){   
       
        if(!v[0]==0){
    
        ok=false;
        }
        if(i==n-1){
            break;
            ok=false;
        }
        
        if(!((root[v[i]][v[i+1]])||(root[v[i+1]][v[i]])))ok=false;
        //とおれないみちのときにtrue 
    }
    
    if(ok)ans++;
}while(next_permutation(v.begin(),v.end()));
cout<<ans<<endl;

}
