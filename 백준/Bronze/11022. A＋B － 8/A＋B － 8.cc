#include <stdio.h>

int main(){
    int test_case, a, b, i, result;
    scanf("%d", &test_case);
    for (i = 0; i < test_case; i++){
        scanf("%d %d", &a, &b);
        result = a + b;
        printf("Case #%d: %d + %d = %d\n", i+1, a, b, result);
    }
}