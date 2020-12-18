#include <stdio.h>

int main(void)
{
    int a;

    scanf("%d", &a);
    printf("입력된 값: %d\n", a);

    int age;
    double height;

    printf("나이와 키를 입력하세요 : ");
    scanf("%d%lf", &age, &height);
    printf("나이는 %d, 키는 %lf 입니다\n", age, height);

    char grade;
    char name[20];

    printf("학점입력: ");
    scanf("%c", &grade);
    printf("이름 입력: ");
    scanf("%s", name);
    printf("%s의 학점은 %c입니다. \n", name, grade);
    
    return 0;
}
