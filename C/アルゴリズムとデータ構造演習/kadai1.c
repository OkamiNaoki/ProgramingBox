#include<stdio.h>
#include<time.h>

long long int total(long int n){
long long int t=0;
for(long long int i=1;i<n+1;i++){
if(i%3==0||i%5==0){
continue;

}
t+=i;

}
return t;
}
void main(){
clock_t start,end;
long long int n=1000000;
long long int s=0;
for(int j=1;j<11;j++){
for(int i=0;i<5;i++){
start=clock();
s=total(n*j);
end=clock();
printf("%f sec",(double)(end-start)/CLOCKS_PER_SEC);
printf("%lld",s);
}
printf("\n");
}
}

