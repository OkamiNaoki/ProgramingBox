#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;

int main(){
    int count=0;
    int max=0; 
    int l;   
    string s;
    cin>>s;
    l=s.size();
    rep(i,l){
        count=0;
          
            for(int j=i;j<l;j++){
            if(!(s[j]=='A'||s[j]=='G'||s[j]=='C'||s[j]=='T')){
            break;
            }
            count++;
            }
        
        if(max<=count)max=count;
    }

    cout<<max;
}