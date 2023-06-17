#include<stdio.h>
#include<math.h>


#define DEN 998
#define DN 2.0 /*ノズル径*/
#define NH 3.0 /*噴孔数*/
#define DL 8.9 /*噴孔長さ*/
#define Patm 0.1e6

#define Pinj 2.6e7

#define ZD 0.8 /*Z/D*/
#define DS 10.2 /*サック径*/

#define NUM1 36 /*周方向に何等分して考えるか*/
#define NUM 10 /*管摩擦損失の部分を何等分にするか*/


int main(void){

        /*FILE *fp;
    char *fname="a1.csv";
    fp = fopen(fname,"w");
    if(fp == NULL){
        printf("file can't open\n");
        return 0;
    }*/

/*面積の単位は㎜、㎟とする*/
double b;
int NU=4;
for(b=1; b<NU+1; b++){
    double liftper = b/NU;
    /*printf("b/NU %e ", liftpercent);*/
    /*printf("%lf \n", VNfirst);*/
    
    double VN = 10;/*初期値代入のための適当な値*/
    double VN2 = 1.5;/*Zが小さいほど値は小さく！！！*/
    double Fusums;
    while(VN2 > 1.005*VN ||  VN2 < 0.995*VN){
            VN = VN2;
            printf("continue %e\n", VN);
        
/*printf("%e\n", VN);*/
double Z = ZD*DN*liftper;
double ADN =M_PI*pow(DN/2.0, 2.0);
double NUE =0.893*pow(10, -6.0); /*動粘性係数ν*/
double rs = 0.0355; /*計算できるようになるまでは面積比手入力(小さい方の面積)*/
double rl = 0.0881; /*計算できるようになるまでは面積比手入力(大きい方の面積)*/
double ral = M_PI*Z*(DS+Z*pow(3.0, 2.0)/2.0);/*全体の面積*/
        int l;
        double YA[NUM], YAs[NUM], uys[NUM], Res[NUM], LAMs[NUM], Yss[NUM], Ys; /*LAM：λ*/
        for(l=0; l<NUM; l++){
                YA[l] =M_PI*Z*(DS+4.0*l+Z*pow(3.0, 2.0)/2.0);
                YAs[l] = YA[l]*rs/ral;
                uys[l] = 3*VN*ADN/YA[l];/*一旦1周等しいとしたときの流速にする！！！*/
                Res[l] = uys[l]*Z*rs/(ral*NUE);
                LAMs[l] = 0.3164*pow(Res[l], -0.25); 
                Yss[l] = DEN*LAMs[l]/(Z*pow(rs,0.5)/pow(ral, 0.5))*pow(uys[l], 2.0)/2.0;/*線比は面積比の1/2乗にした*/
                Ys += Yss[l]; /*確認済*/
                /*printf("%e %e %e %e %e \n", YAs[l], uys[l], Res[l], LAMs[l], Yss[l]);*/
        }

/*縮小損失Xの計算*/
        double Xa = 2*3*24;
        double Xas = Xa/NUM1;
        double Xrcs = 0.582+0.0148/(1.1-pow((YAs[0]/Xas), 2.0)); /*A2/Ac*/
        double XCs = 0.04+pow((1.0/Xrcs)-1.0, 2.0); /*ξ*/
        double Xs = XCs*DEN*pow(uys[9], 2.0)/2.0;/*縮小損失*/ /*丸め込むのがおかしい気がするちょっと誤差ある*/
        /*printf("Xs %e\n", Xs);*/ 

/*拡大損失Zの計算*/

        double YAe = M_PI*pow((DS/2), 2.0) ;
        double Aes = YAe/NUM1;
        double Zes = YA[0]/Aes; /*A1/A2*/
        double ZCs = pow((1-Zes), 2.0);/*ζ*/
        double Zs = DEN*pow(uys[0], 2.0)/2;/*丸め込むのがおかしい気がするちょっと誤差ある*/
        /*printf("Zs %e \n", Zs);*/      
		
/*面積が小さい側のサックより上流の損失合計*/
    double Fusums = Xs+Ys+Zs;
        /*printf("Fusums %e \n", Fusums);*/


/*サックより下流の損失合計*/
/*縮小損失*/
        double XXa = M_PI*pow(DS/2.0, 2.0);
        double XXas = XXa/NUM1;
        double XXrcs = 0.582+0.0148/(1.1-pow((ADN/XXas), 2.0)); /*A2/Ac*/
        double XXCs = 0.04+pow((1.0/XXrcs)-1.0, 2.0); /*ξ*/
        double XXs = XXCs*DEN*pow(VN, 2.0)/2.0; /*縮小損失。丸め込みに不安*/
        /*printf("Xs %e\n", Xs);*/ 

/*管摩擦損失Yの計算OK*/
        double YRes = VN*DN/NUE;
        double YLAMs = 0.3164*pow(YRes, -0.25); 
        double YYs = DEN*YLAMs*DL/DN*pow(VN, 2.0)/2.0;
            /*printf("%e %lf \n", Yss, uys[l]);*/

/*サックより下流側の損失合計*/

		double Fdsums = XXs+YYs;

/*損失合計*/
		double Fsums = Fusums + Fdsums;
		/*printf("%e \n", Fsums);*/
	    double Q = Pinj-Fsums;

    if(Q<0){
        VN2 = VN*0.95;/*Zが小さくなるほど1に限りなく近づける方が収束が早い*/
        printf(" if ");
    }
    else{
        VN2 = 2*pow(Q, 0.5)/DEN;
        printf(" else ");
    }
    
	
	/*printf("%lf %lf\n", VN[s], VN[s+1]);*/

    /*printf("%e %e %e %e %e %e %lf\n", Xs, Ys, Zs, XXs, YYs, Q, VN2);*/
    printf("%e ", Fusums);
    Xs = Ys = Zs = XXs = YYs =0;

}
	printf("done lift VN %lf %lf %e\n\n\n", liftper*ZD, VN2, Fusums);

}

return 0;
}
