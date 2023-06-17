#include<stdio.h>
#include <stdlib.h>

int main(){

	FILE *fp; // FILE型構造体
	char fname[] = "gauss_data.txt";
    double** num = NULL;
    double* n = NULL;

    int N=256;
    char str[N];
	fp = fopen(fname, "r"); // ファイルを開く。失敗するとNULLを返す。
	if(fp == NULL) {
		printf("%s file not open!\n", fname);
		return -1;
	}
    int counter=0;
    
	while(fgets(str, N, fp) != NULL) {
        counter++;
    }

    n = (double*)malloc(sizeof(double) * counter+1);
    num = (double**)malloc(sizeof(double*) * counter);
     if(num == NULL){
        return -1;
    }
    for(int i = 0; i < counter; i++){
        num[i] = (double*)malloc(sizeof(double) * counter+1);
        if(num[i] == NULL){
            return -1;
        }
    }  
    fclose(fp);  
    	fp = fopen(fname, "r"); // ファイルを開く。失敗するとNULLを返す。
	if(fp == NULL) {
		printf("%s file not open!\n", fname);
		return -1;
	}

    int s=0;
for (int i = 0; i < counter; i++){
        for (int j = 0; j < counter+1; j++){
            if (fscanf(fp, "%lf", &num[i][j]) == EOF)break;
        }
}
	fclose(fp); // ファイルを閉じる
int e=0.00005;
double nmax=0;
int imax;
double y=0;
for(int l=0;l<counter-1;l++){
    if(num[l][l]==0||labs(num[l][l])<e){

    for(int i=l;i<counter;i++){
        if(labs(num[i][l])>abs(nmax)){
            nmax=num[i][l];
            imax=i;
        }
    }
    for(int i=0;i<counter+1;i++){
        n[i]=num[l][i];
        num[l][i]=num[imax][i];
        num[imax][i]=n[i];
    }
}

    for(int j=l+1;j<counter;j++){
            y=num[j][l]/num[l][l];
        for(int k=l;k<counter+1;k++){

            num[j][k]=num[j][k]-num[l][k]*y;
        }
    }

}
for(int i=0;i<counter;i++){
    for(int j=0;j<counter+1;j++){
        printf("%f,",num[i][j]);
    }
    printf("\n");
}
    printf("\n");

for(int i=counter-1;i>0;i--){
    for(int j=i-1;j>=0;j--){
        y=num[j][i]/num[i][i];
        for(int k=counter;k>=0;k--){
            num[j][k]=num[j][k]-y*num[i][k];
        }
    }
}
for(int i=0;i<counter;i++){
    num[i][counter]=num[i][counter]/num[i][i];
    num[i][i]=num[i][i]/num[i][i];
}
for(int i=0;i<counter;i++){
    for(int j=0;j<counter+1;j++){
        printf("%f,",num[i][j]);
    }
    printf("\n");
}
return 0;
}
