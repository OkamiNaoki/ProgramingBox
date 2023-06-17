#include<stdio.h>
#include <stdlib.h>
#include<math.h>
#include<string.h>

double p(double** arr,int c,int a){
        double nmax=0;
        int imax;
        double* n = NULL;
        n = (double*)malloc(sizeof(double) * c*2);
        for(int i=a;i<c;i++){
        if(labs(arr[i][a])>abs(nmax)){
            nmax=arr[i][a];
            imax=i;
        }
    }
    for(int i=0;i<c*2;i++){
        n[i]=arr[a][i];
        arr[a][i]=arr[imax][i];
        arr[imax][i]=n[i];
    }
}

int main(){

	FILE *fp; // FILE型構造体
	int N=256;
    char fname[N];
    double** num = NULL;
    int counter=0;
    char str[N];
    double reader=1;
    double y=0;
    printf("file名を教えてください");
    scanf("%s",fname);

	fp = fopen(fname, "r"); // ファイルを開く。失敗するとNULLを返す。
	if(fp == NULL) {
		printf("%s file not open!\n", fname);
		return -1;
	}
	while(fgets(str, N, fp) != NULL) {
        counter++;

    }


    num = (double**)malloc(sizeof(double*) * counter);
     if(num == NULL){
        return -1;
    }
    for(int i = 0; i < counter; i++){
        num[i] = (double*)malloc(sizeof(double) * counter*2);
        if(num[i] == NULL){
            return -1;
        }
    }  
    rewind(fp);  

for (int i = 0; i < counter; i++){
        for (int j = 0; j < counter*2; j++){
            num[i][j]=0;
        }
            num[i][i+counter]=1;
}
double strdouble=-1;
for (int i = 0; i < counter; i++){
        for (int j = 0; j < counter; j++){
            if (fscanf(fp, "%s", str) != EOF){
                strdouble=atof(str);
                if(strcmp(str,"K")==0){
                        printf("Kに入れる数字を教えて");
                        scanf("%lf",&reader);
                    num[i][j]=reader;
                }else{
                     num[i][j]=strdouble;
                }
            }else{
                break;
            }
        }
}

	fclose(fp); // ファイルを閉じる
int e=0.00005;

for(int l=0;l<counter;l++){
    if(num[l][l]==0||labs(num[l][l])<e){
p(num,counter,l);

}

    for(int j=l+1;j<counter;j++){
            y=num[j][l]/num[l][l];
        for(int k=l;k<counter*2;k++){

            num[j][k]=num[j][k]-num[l][k]*y;
        }

    }
    int c=0;
    for(int j=0;j<counter;j++){
        if(num[l][j]==0)c++;
    }
    if(c==4){
     printf("No inverse Matrix");
        return 0;
    }
}
for(int i=0;i<counter;i++){
    for(int j=0;j<counter*2;j++){
        printf("%f,",num[i][j]);
    }
    printf("\n");
}
    printf("\n");

for(int i=counter-1;i>0;i--){
    for(int j=i-1;j>=0;j--){
        y=num[j][i]/num[i][i];
        for(int k=counter*2-1;k>=0;k--){
            num[j][k]=num[j][k]-y*num[i][k];
        }
    }
}
for(int i=0;i<counter;i++){
    for(int j=0;j<counter*2;j++){
        printf("%lf,",num[i][j]);
    }
    printf("\n");
}
for(int i=0;i<counter;i++){
    for(int j=counter;j<counter*2;j++){
        num[i][j]=num[i][j]/num[i][i];
    }
       num[i][i]=num[i][i]/num[i][i];
}
for(int i=0;i<counter;i++){
    for(int j=0;j<counter*2;j++){
        printf("%f,",num[i][j]);
    }
    printf("\n");
}
return 0;
}


