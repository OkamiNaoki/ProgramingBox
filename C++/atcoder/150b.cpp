#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int n;cin>>n;
    string s;cin>>s;
    int ans=0;
    rep(i,n-2){
        if(s[i]=='A'){
            if(s[i+1]=='B'){
                if(s[i+2]=='C'){
                    ans++;
                }
            }
        }
    }
    cout<<ans;
}