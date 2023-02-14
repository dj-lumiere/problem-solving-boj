#include <iostream>

int main(){
    int N, i, max, min;
    int array[1000000];
    std::cin >> N;
    for (i = 0; i < N; i++){
        std::cin >> array[i];
    }
    max = array[0];
    min = array[0];
    for (i = 0; i < N; i++){
        if (array[i] > max)
            max = array[i];
        if (array[i] < min)
            min = array[i];
    }
    std::cout << min << " " << max;
}