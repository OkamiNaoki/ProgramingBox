#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int n,m;cin>>n>>m;
    vector<vector<int>>v(m);
    rep(i,m){
        int k;cin>>k;
        v[i].resize(k);
        rep(j,k){
            cin>>v[i][j];
            --v[i][j];
        }
    }
    vector<int>p(m);
    rep(i,m)cin>>p[i];
    int ans=0;
    rep(i,1<<n){ //00 01 10 11が入っている

        bool ok=true;
        rep(j,m){ //電球の個数
           
            int c=0;
            for(int id:v[j]){ // v[]に入っている数字によって２桁目か一桁目か
            
                if((i>>id)&1){
                    ++c;
                }
            }
            c%=2;
            if(c!=p[j]){
                ok=false;
            }
        }
        if(ok){
            ++ans;
        }
    }

    cout<<ans<<endl;
    return 0;

}
