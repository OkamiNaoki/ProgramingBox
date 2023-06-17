#include <stdio.h>
#include <math.h> /* ターミナルでコンパイルする際にエラー・警告が出た場合 gcc -lm newton.c -o newtonというように"-lm"オプションを付けてください．*/
#define EPSIRON1 0.00001 /* 収束・発散判定に用いる値は適宜決めてください */
#define EPSIRON2 0.00001
#define K_MAX 100 /* 反復回数は適宜決めてください */ 

double nonlinear_func(double x) /* 非線形関数の計算用関数 */
{
	double ff;

	ff=0.03*x*x*x-3*x*sin(0.6*x)-0.3*x+3.0;
	return ff;
}

double nonlinear_func_diff(double x) /* 微分した関数の計算用関数 */
{
	double ff;

/* 計算した微分した関数を書き込んでいいです */

	ff=(9*x*x-180*x*cos(0.6*x)-300*sin(0.6*x)-30)/100;
	return ff;
}

int main (void)
{
	double init_x, x[K_MAX+1];
	int k; /* カウント用 */
	int flag_step1=1; /* フラグ用の変数(必要ならば使ってください) */

	printf("Inital value = ");
    /* 初期値の入力部分を書いてください */ 
	scanf("%lf",&init_x);
	x[0]=init_x;

    k=0;
	while(k<K_MAX){ /* ニュートン法の処理を書いてください．For文でも作れます */
      /* この中でステップ2～4の操作と，ステップ1に戻る場合を記載することになります */
      /* 例えば，ステップ1に戻るかどうかをフラグ用変数を使う場合(flag_step1 = 0のときステップ1の作業（初期解を設定）を行う) */
		if(flag_step1 == 0){
	      /* 初期解の再設定 */
			printf("Initial value=");
			scanf("%lf",&init_x);
			x[0]=init_x;
            k=0;
			flag_step1=1;
		}
		else{
         /* ステップ2～4の操作 */
         /* この中で非線形関数・微分した関数の計算用関数を呼び出す */
		 if(fabs(nonlinear_func_diff(x[k]))<EPSIRON1){
			 flag_step1=0;
			 continue;
		 }
			x[k+1]=x[k]-nonlinear_func(x[k])/nonlinear_func_diff(x[k]);
			if(fabs(nonlinear_func(x[k+1]))<EPSIRON2)break;
			if(k>=1){
				if(fabs(x[k+1]-x[k])>=fabs(x[k]-x[k-1])){
					flag_step1=0;
				}
			}
			printf("x[%d]=%lf\n",k+1,x[k+1]);
	     	k++;
		}
	}

 /* 解の出力部分を書いてください */
printf("result: x[%d]=%lf",k,x[k]);

	return 0;
}