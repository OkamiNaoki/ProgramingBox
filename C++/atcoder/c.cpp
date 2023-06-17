#include <stdio.h>
int max(int x, int y) {
    printf("max(%d, %d) is called¥n", x,y);
    if (x<y) return y;
    return x;
}
int main(int argc, char* argv[]) {
    int a = 10;
    int b = max(a*3, a+4);
    printf("result: %d¥n", b);
    return 0;
}