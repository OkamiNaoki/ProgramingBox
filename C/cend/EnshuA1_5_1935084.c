#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define ITERATION 2000 // Number of Iteration
#define ETA 0.003 // learning coeffcient
#define MAX_N_DATA 10000 // number of maximum input data size

float calc_y(float a, float b, float c, float d, float x)
{
    // calculate the result y of input x using parameters a, b, c and d
    float y_calc;
    
    // Need to change the formulation
    y_calc = a *x*x*x + b*x*x+c*x+d;

    return y_calc;

}

float get_loss(int n_data, float* x, float* y, float a, float b,float c, float d)
{
    float loss_total = 0;
    float y_calc, y_diff, loss;


    for (int i = 0; i < n_data; i++) {
        // Need to implementation
        y_diff=3*a*x[i]*x[i]+2*b*x[i]+c;
        // Calculation of y of input x using parameters
        y_calc=calc_y(a,b,c,d,x[i]);

        // the error is diference between the prediction and the real result y.
    
        // the loss is defined as the squared error.
       
        // sum up the loss
        loss_total+=(y_calc-y[i])*(y_calc-y[i]);
    }
    return loss_total / n_data; // return to mean square errors 
}

float get_grad_a(int n_data, float* x, float* y, float a, float b, float c, float d)
{
    float grad_total = 0;
    float y_calc,grad;

    for (int i = 0; i < n_data; i++) {
        // Need to implementation
        y_calc=calc_y(a,b,c,d,x[i]);
        grad_total+=2*x[i]*x[i]*x[i]*(y_calc-y[i]);

    }
    return grad_total / n_data; // return to gradient
}

float get_grad_b(int n_data, float* x, float* y, float a, float b,float c, float d)
{
    float grad_total = 0;
    float y_calc,grad;

    for (int i = 0; i < n_data; i++) {
        // Need to implementation
        y_calc=calc_y(a,b,c,d,x[i]);
        grad_total+=2*x[i]*x[i]*(y_calc-y[i]);

    }
    return grad_total / n_data; // return to gradient


}

float get_grad_c(int n_data, float* x, float* y, float a, float b,float c, float d)
{
    float grad_total = 0;
    float y_calc,grad;
    for (int i = 0; i < n_data; i++) {
        // Need to implementation like get_grad_a
        y_calc=calc_y(a,b,c,d,x[i]);
        grad_total+=2*x[i]*(y_calc-y[i]);

    }
    return grad_total / n_data; // return to gradient

}

float get_grad_d(int n_data, float* x, float* y, float a, float b,float c, float d)
{
    float grad_total = 0;
    float y_calc,grad;
    for (int i = 0; i < n_data; i++) {
        // Need to implementation like get_grad_a
        y_calc=calc_y(a,b,c,d,x[i]);
        grad_total+=2*(y_calc-y[i]);

    }
    return grad_total / n_data; // return to gradient

}


int load_data(float* x, float* y)
{
    // Data is loaded from "data_kadai.dat".
    FILE *fp;
    int n_data = 0;
    int n_data_loaded;

    if ((fp = fopen("kadai5_data.dat", "r")) == NULL) {
        printf("File data_kadai cannot be opened.\n");
    }
    // How many data is loaded
    while (1) {
        // A pair of measures is loaded.
        n_data_loaded = fscanf(fp, "%f %f\n", &x[n_data], &y[n_data]);
        // When no pair is loaded, break.
        if (n_data_loaded < 2) {
            break;
        }
        // The number of loaded pairs is incremented.
       // printf("%d: %lf %lf\n",n_data,x[n_data],y[n_data]);
        n_data++;
    }
    fclose(fp);

    // Return the number of data
    return n_data;
}
int main(void)
{
    // initialization
    float x[MAX_N_DATA],y[MAX_N_DATA];
    float a,b,c,d,e; // coefficient
    float loss, grad_a,grad_b,grad_c,grad_d;
    int n_data;


    n_data = load_data(x,y);
    //printf("%d pairs are loaded.\n", n_data);

    // initial parameter
    a = 1.0;
    b = 1.0;
    c = 1.0;
    d = 1.0;


    // main loop
    for (int t = 0; t < ITERATION; t++) {
        loss = get_loss(n_data, x, y, a, b,c,d);
        grad_a = get_grad_a(n_data, x, y, a, b,c,d);
        grad_b = get_grad_b(n_data, x, y, a, b,c,d);
        grad_c = get_grad_c(n_data, x, y, a, b,c,d);
        grad_d = get_grad_d(n_data, x, y, a, b,c,d);
        // Need to implementation for grad_b,grad_c and grad_d


        //printf("%d a=%1.5f, b=%1.5f, c=%1.5f, d=%1.5f, L=%1.5f\n", t, a, b, c,d,loss);

        // updata of coefficient using gradient 
        // Need to implementation
        a-=grad_a*ETA;
        b-=grad_b*ETA;
        c-=grad_c*ETA;
        d-=grad_d*ETA;
    }
   printf("y=%1.5fx^3+%1.5fx^2+%1.5fx+%1.5f\n", a, b, c,d); 

    return 0;
}