
#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;


int main(){

    int a,b,k;
    int count=0;
    cin>>a>>b>>k;
    for(int i=min(a,b);i>0;i--){
        if(a%i==0&&b%i==0){
            count++;
            if(count==k){
                cout<<i<<endl;
                return 0;

            }
        }

    }


}