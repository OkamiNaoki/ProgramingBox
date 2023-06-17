#include<stdio.h>
#include<time.h>

int abc(int n){
int t=0;
int a=1;
int b=1;
int c=1;
for(int i=1;i<n+1;i++){
a=i*i*i;
for(int j=1;j<a/3+1;j++){
c=j*3;
for(int k=1;k<c+1;k++){
b=k*k*k;
if(a==b+c){
t++;
}
}
}

}
return t;
}
void main(){
clock_t start,end;
int n=20;
int s=0;
for(int i=0;i<10;i++){
for(int j=0;j<5;j++){
start=clock();
s=abc(n+i);
end=clock();
printf("%f sec",(double)(end-start)/CLOCKS_PER_SEC);
printf("%d",s);
}
printf("\n");

}
}

