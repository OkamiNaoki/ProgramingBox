#include <stdio.h>
#define epsiron 0.00005
#define ROW 3 /* 制約条件の数(基底変数の数) */
#define SLACK 3 /* SLACK変数の数 */
#define COLUMN 2 /* 列数(目的関数の変数の数) */
#define M 3 /* 基底変数の数 */
#define N 5 /* 全ての変数の数 MとNを使ってプログラムを組んでも構いません */

int main(void)
{
	int i, j, k, end_flag;
	int pivot_column,pivot_row; /* ピボット変換の基準となる値を入れるための変数 */
	double temp; /* 値の保持のための変数 */
	double min_val; /* 値の比較のために使用する変数 */
	int min_num; /* 値の比較のために使用する変数 */

    double A[ROW][COLUMN+SLACK],B[ROW],C[COLUMN+SLACK]; /* 各係数を入れるための配列の準備 */
    double d[COLUMN+SLACK]; /* 残差を入れるための配列 */
    int Cbx[ROW]; /* 基底変数となる番号を入れた配列 */
    double Cb[ROW]; /* 基底変数となる目的関数の係数を入れた配列 */
    FILE *fp; /* ファイル読み込みのための変数 */
    char fname[30]; /* ファイル名の入力用変数　*/

	double ob; /* 目的関数の値の計算用の変数 */

    /* 係数情報ファイルからの情報取得 */
    printf("Input file name =");
    scanf("%s",fname);

    fp = fopen(fname, "r");
    if (fp == NULL)
    {
        printf("cannot open file");
        return 0;
    }
    else{
        for(i=0;i<COLUMN;i++){ /* 目的関数の入力 */
            fscanf(fp,"%lf",&C[i]);
        }
        for(i=0;i<ROW;i++){ /* 各係数の入力 */
            for(j=0;j<COLUMN+SLACK;j++){
                fscanf(fp,"%lf ",&A[i][j]);
            }
            fscanf(fp,"%lf",&B[i]);
        }
        for(i=COLUMN+SLACK-ROW;i<COLUMN+SLACK;i++){ /* スラック変数部分の目的関数の係数を0にするための処理 */
            C[i]=0.00;
        } 
        for(i=0;i<ROW;i++){ /* 基底変数の番号の入力 */
            fscanf(fp,"%d",&Cbx[i]);
        }
    }

    /* 初期設定 */
    for(i=0;i<COLUMN+SLACK;i++){ /* 残差の初期設定 */
        d[i]=C[i];
    }
    for(i=0;i<ROW;i++){ /* 基底変数の目的関数の係数の入力 */
        Cb[i]=C[Cbx[i]];
    }

	end_flag = 0; /* 全てのdが0以上になったかを判断するためのフラグ */
int count=0;
	while(1){
		i =0;
count++;
		/* 全てのd（残差）が0以上になったかどうかを調べ，なっていれば結果を出力させるためにend_flagの値を変更する */
		/* 丸め誤差を考慮してepsironを使用する */
		for(int j=0;j<COLUMN+SLACK;j++)if(d[j]<-epsiron)i=1;
		if(i!=1)end_flag=1;

	
		if (end_flag ==0){ /* 負の残差がある場合，シンプレックス法を解く */
			min_num = 0;
			min_val = 0;

			/* ピボットする列を決定するため，最も小さいdの値を探索し，ピボット変換する列を決定 */
			for(int j=0;j<COLUMN+SLACK;j++){
				if(min_val>=d[j]){
					min_val=d[j];
					min_num=j;
				}
			}
			pivot_column=min_num;
			
			min_num=0;
			min_val=1000;

            /* ピボット変換するための行を決定 */
			/* ピボットする行は，Aの値が0でなく，B[j]/A[j][pivot_column]が正の値のうち，最も小さい値 */
			for(int j=0;j<ROW;j++){
				if(min_val>B[j]/A[j][pivot_column]&&(B[j]/A[j][pivot_column])>0){
					min_val=B[j]/A[j][pivot_column];
					min_num=j;
				}
			}
			pivot_row=min_num;



            /* ガウス・ジョルダン法（掃き出し法）による変換 */
			/* ピボットする行に対する演算 */
			double save=A[pivot_row][pivot_column];
			for(int j=0;j<COLUMN+SLACK;j++) A[pivot_row][j]/=save;
			B[pivot_row]/=save;

			/* それ以外の行に対する演算 */
			/* ピボット変換を行った行以外で演算を行う */
			
			for(int j=0;j<ROW;j++){
				if(j==pivot_row)continue;
				save=A[j][pivot_column];
			
				for(int k=0;k<COLUMN+SLACK;k++){
					A[j][k]=A[j][k]-(save*A[pivot_row][k]);
				}
				B[j]=B[j]-save*B[pivot_row];
			}



			/* 残差のところまで忘れずに演算を行うことに注意 */
			save=d[pivot_column];
			
			for(int j=0;j<COLUMN+SLACK;j++){
			d[j]=d[j]-save*A[pivot_row][j];

			}



			/* 基底変数の入れ替え */
			double changeNum;
			changeNum=Cb[pivot_row];
			Cb[pivot_row]=C[pivot_column];
			C[pivot_column]=changeNum;
			Cbx[pivot_row]=pivot_column;

			for(k=0;k<ROW;k++){ /* 途中の変換の様子を出力 */
				for(j=0;j<COLUMN+SLACK;j++){
					printf("%lf ",A[k][j]);
				}
				printf("%lf\n",B[k]);
			}

		}
		else{ /* 全ての残差が0以上になったら結果を出力 */
			ob = 0.000;

			for(k=0;k<ROW;k++){ /* 目的関数値の計算 */
				ob+= Cb[k] * B[k];
			}
			int x0,x1;
			printf("Objective Function = %d\n",(int)ob);
			for(k=0;k<ROW;k++){ /* 基底変数の番号とその値の出力 */
				if(Cbx[k] < COLUMN+SLACK-ROW){
					printf("Basic variable: x%d = %lf\n",Cbx[k],B[k]);
					if(Cbx[k]==0)x0=k;
					if(Cbx[k]==1)x1=k;
				}else{
					printf("Basic variable: Lambda%d = %lf\n",Cbx[k]-(COLUMN+SLACK-ROW),B[k]);
				}
			}

			/* これ以下で総販売金額，総利益など求められている値を出力させる */
			printf("Total Sales =%lf yen\n",-1*(B[x0]*Cb[x0]+B[x1]*Cb[x1]));
			printf("Profits = %lf yen\n",-1*(Cb[x0]*B[x0]+Cb[x1]*B[x1])-(200*B[x0]+150*B[x1]));
			printf("Production volume: %lf liter\n",B[x0]*1.5+B[x1]*1.0);
			printf("Used material volume: M = %lf gram\n",B[x0]*100+B[x1]*180);



			break;
		}

	}

	return 0;

}