#include<stdio.h>

void C_fun(double * a, double * b, int n) {

    printf("C code called: a: %f b: %f\n", a[0], b[0]);
    
    for(int i=0; i < n; ++i) b[i] += a[i]; 
}
