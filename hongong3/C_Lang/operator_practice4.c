#include <stdio.h>

int main(void)
{
    int a = 20, b = 3;
    double res;

    res = ((double)a) / ((double)b);
    printf("a = %d, b = %d\n", a, b);
    printf("a / b의 결과: %.1lf\n", res);

    a = (int)res;
    printf("(int) %.1lf의 결과 : %d\n", res, a);

    int k = 10;
    double h = 3.4;

    printf("int형 변수의 크기: %lu\n", sizeof(k));
    printf("double형 변수의 크기: %lu\n", sizeof(h));
    printf("정수형 상수의 크기: %lu\n", sizeof(10));
    printf("수식의 결괏값의 크기: %lu\n", sizeof(1.5 + 3.4));
    printf("char 자료형의 크기: %lu\n", sizeof(char));

    return 0;

}