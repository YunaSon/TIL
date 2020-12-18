#include <stdio.h>

//조건연산자에서 문자열 반환 부분 계속 에러 발생..

int main(void)
{
    double w, h, hm;
    double bmi;
    int a = 1, b = 0, res;

    printf("몸무게(kg)와 키(cm)를 입력: ");
    scanf("%lf%lf", &w, &h);
    printf("몸무게 %lf, 키 %lf", w, h);
 
    hm = h/100;

    bmi = (w/(hm*hm));
    printf("bmi지수는: %lf\n", bmi);

    res = (20 <= bmi && bmi < 25) ? a : b;
    printf("%d\n", res);

    return 0;
}
