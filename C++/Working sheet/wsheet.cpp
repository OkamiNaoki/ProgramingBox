#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
using namespace std;
using ll=long long;
using P =pair<int,int>;
 
 
 //勤務者プロフィール
struct prof {   
    char name[30];   // 名前
    int teem;        // ０チーム　1チーム
    int seibetu;     //性別　０男　1女
    bool keiken;     //0 3年以下　1 4年以上
    bool can;        //師長休み時　１　日勤可能
    bool sityo;      //師長か？

    bool restInter;  //休み間隔正解
    bool restNum;    //休み日数
    bool restCon;    //連休日数
    bool junsin;     //準夜足す深夜
} person;

//勤務表シャッフル関数
void shuffle(int ary[],int size)
{
    for(int i=0;i<size;i++)
    {
        int j = rand()%size;
        int t = ary[i];
        ary[i] = ary[j];
        ary[j] = t;
    }
}

int main(){
int MAX_NUM;cin>>MAX_NUM;
int HITOTUKI=28;
int YOUBI;//最初の曜日０月ー６日
cin>>YOUBI;
struct prof person[MAX_NUM];
int kinmuhyou[MAX_NUM][HITOTUKI];
//1日勤,2深夜,3はやで,4おそで,5準夜,6休み
int heijitu[MAX_NUM]={1,1,1,1,3,3,4,4,2,2,2,5,5,6,6};
int kyuujitu[MAX_NUM]={1,1,3,3,4,4,2,2,2,5,5,6,6,6,6};
rep(i,HITOTUKI){
    if((i+YOUBI)%7==5||(i+YOUBI)%7==6){
        shuffle(kyuujitu,MAX_NUM);
        rep(j,MAX_NUM){
            kinmuhyou[j][i]=kyuujitu[j];
        }
    }else{
        shuffle(heijitu,MAX_NUM);
         rep(k,MAX_NUM){
            kinmuhyou[k][i]=heijitu[k];
        }
    }

}
   rep(i,MAX_NUM){
       rep(j,HITOTUKI){
           cout<<kinmuhyou[i][j];
       }
       cout<<endl;

   }
}